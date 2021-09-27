# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from __future__ import absolute_import
import logging
from typing import Iterator, Optional, Any, Union, TypeVar
import urllib3 # type: ignore
from urllib3.util.retry import Retry # type: ignore
from urllib3.exceptions import (
    DecodeError, ReadTimeoutError, ProtocolError
)
import requests

from azure.core.configuration import ConnectionConfiguration
from azure.core.exceptions import (
    ServiceRequestError,
    ServiceResponseError,
    IncompleteReadError,
)
from . import HttpRequest # pylint: disable=unused-import

from ._base import (
    HttpTransport,
    HttpResponse,
    _HttpResponseBase
)
from ._bigger_block_size_http_adapters import BiggerBlockSizeHTTPAdapter
from .._tools import get_block_size as _get_block_size, get_internal_response as _get_internal_response

PipelineType = TypeVar("PipelineType")

_LOGGER = logging.getLogger(__name__)

def _read_raw_stream(response, chunk_size=1):
    # Special case for urllib3.
    if hasattr(response.raw, 'stream'):
        try:
            for chunk in response.raw.stream(chunk_size, decode_content=False):
                yield chunk
        except ProtocolError as e:
            raise requests.exceptions.ChunkedEncodingError(e)
        except DecodeError as e:
            raise requests.exceptions.ContentDecodingError(e)
        except ReadTimeoutError as e:
            raise requests.exceptions.ConnectionError(e)
    else:
        # Standard file-like object.
        while True:
            chunk = response.raw.read(chunk_size)
            if not chunk:
                break
            yield chunk

    # following behavior from requests iter_content, we set content consumed to True
    # https://github.com/psf/requests/blob/master/requests/models.py#L774
    response._content_consumed = True  # pylint: disable=protected-access


def _set_enforce_content_length(request, *args, **kwargs):  # pylint: disable=unused-argument
    # type: (requests.Request, Any, Any) -> None
    """
    Hook to set urllib3's enforce_content_length
    """
    # Do not modify objects if they don't look like the urllib3 connections
    if hasattr(request.raw, "enforce_content_length"):
        request.raw.enforce_content_length = True


def _get_request_hooks(user_hooks):
    # type: (Optional[dict]) -> dict
    """
    Get an argument for the `hooks` parameter for `requests.Session.request` that
    sets the `enforce_content_length` on the underlying urllib3 connection.
    `user_hooks` are the hooks passed to Transport.send explicitly. They are called last,
    so users can override the default set here if they insist.
    """
    if user_hooks:
        merged_hooks = dict(user_hooks)
    else:
        merged_hooks = requests.hooks.default_hooks()
    user_response_hooks = merged_hooks.pop("response")
    if user_response_hooks is None:
        merged_response_hooks = [_set_enforce_content_length]
    elif callable(user_response_hooks):
        merged_response_hooks = [_set_enforce_content_length, user_response_hooks]
    else:
        merged_response_hooks = [_set_enforce_content_length] + user_response_hooks
    merged_hooks["response"] = merged_response_hooks
    return merged_hooks


class _RequestsTransportResponseBase(_HttpResponseBase):
    """Base class for accessing response data.

    :param HttpRequest request: The request.
    :param requests_response: The object returned from the HTTP library.
    :param int block_size: Size in bytes.
    """
    def __init__(self, request, requests_response, block_size=None):
        super(_RequestsTransportResponseBase, self).__init__(request, requests_response, block_size=block_size)
        self.status_code = requests_response.status_code
        self.headers = requests_response.headers
        self.reason = requests_response.reason
        self.content_type = requests_response.headers.get('content-type')

    def body(self):
        try:
            return self.internal_response.content
        except requests.exceptions.ChunkedEncodingError as err:
            error = IncompleteReadError(err, error=err)

    def text(self, encoding=None):
        # type: (Optional[str]) -> str
        """Return the whole body as a string.

        If encoding is not provided, mostly rely on requests auto-detection, except
        for BOM, that requests ignores. If we see a UTF8 BOM, we assumes UTF8 unlike requests.

        :param str encoding: The encoding to apply.
        """
        if not encoding:
            # There is a few situation where "requests" magic doesn't fit us:
            # - https://github.com/psf/requests/issues/654
            # - https://github.com/psf/requests/issues/1737
            # - https://github.com/psf/requests/issues/2086
            from codecs import BOM_UTF8
            if self.internal_response.content[:3] == BOM_UTF8:
                encoding = "utf-8-sig"

        if encoding:
            if encoding == "utf-8":
                encoding = "utf-8-sig"

            self.internal_response.encoding = encoding

        return self.internal_response.text


class StreamDownloadGenerator(object):
    """Generator for streaming response data.

    :param pipeline: The pipeline object
    :param response: The response object.
    :keyword bool decompress: If True which is default, will attempt to decode the body based
        on the *content-encoding* header.
    """
    def __init__(self, pipeline, response, **kwargs):
        self.pipeline = pipeline
        self.request = response.request
        self.response = response
        self.block_size = _get_block_size(response)
        decompress = kwargs.pop("decompress", True)
        if len(kwargs) > 0:
            raise TypeError("Got an unexpected keyword argument: {}".format(list(kwargs.keys())[0]))
        internal_response = _get_internal_response(response)
        if decompress:
            self.iter_content_func = internal_response.iter_content(self.block_size)
        else:
            self.iter_content_func = _read_raw_stream(internal_response, self.block_size)
        self.content_length = int(response.headers.get('Content-Length', 0))

    def __len__(self):
        return self.content_length

    def __iter__(self):
        return self

    def __next__(self):
        internal_response = _get_internal_response(self.response)
        try:
            chunk = next(self.iter_content_func)
            if not chunk:
                raise StopIteration()
            return chunk
        except StopIteration:
            internal_response.close()
            raise StopIteration()
        except requests.exceptions.StreamConsumedError:
            raise
        except requests.exceptions.ChunkedEncodingError as err:
            _LOGGER.warning("Incomplete download: %s", err)
            internal_response.close()
            raise IncompleteReadError(err, error=err)
        except Exception as err:
            _LOGGER.warning("Unable to stream download: %s", err)
            internal_response.close()
            raise
    next = __next__  # Python 2 compatibility.


class RequestsTransportResponse(HttpResponse, _RequestsTransportResponseBase):
    """Streaming of data from the response.
    """
    def stream_download(self, pipeline, **kwargs):
        # type: (PipelineType, **Any) -> Iterator[bytes]
        """Generator for streaming request body data."""
        return StreamDownloadGenerator(pipeline, self, **kwargs)


class RequestsTransport(HttpTransport):
    """Implements a basic requests HTTP sender.

    Since requests team recommends to use one session per requests, you should
    not consider this class as thread-safe, since it will use one Session
    per instance.

    In this simple implementation:
    - You provide the configured session if you want to, or a basic session is created.
    - All kwargs received by "send" are sent to session.request directly

    :keyword requests.Session session: Request session to use instead of the default one.
    :keyword bool session_owner: Decide if the session provided by user is owned by this transport. Default to True.
    :keyword bool use_env_settings: Uses proxy settings from environment. Defaults to True.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_sync.py
            :start-after: [START requests]
            :end-before: [END requests]
            :language: python
            :dedent: 4
            :caption: Synchronous transport with Requests.
    """

    _protocols = ['http://', 'https://']

    def __init__(self, **kwargs):
        # type: (Any) -> None
        self.session = kwargs.get('session', None)
        self._session_owner = kwargs.get('session_owner', True)
        self.connection_config = ConnectionConfiguration(**kwargs)
        self._use_env_settings = kwargs.pop('use_env_settings', True)

    def __enter__(self):
        # type: () -> RequestsTransport
        self.open()
        return self

    def __exit__(self, *args):  # pylint: disable=arguments-differ
        self.close()

    def _init_session(self, session):
        # type: (requests.Session) -> None
        """Init session level configuration of requests.

        This is initialization I want to do once only on a session.
        """
        session.trust_env = self._use_env_settings
        disable_retries = Retry(total=False, redirect=False, raise_on_status=False)
        adapter = BiggerBlockSizeHTTPAdapter(max_retries=disable_retries)
        for p in self._protocols:
            session.mount(p, adapter)

    def open(self):
        if not self.session and self._session_owner:
            self.session = requests.Session()
            self._init_session(self.session)

    def close(self):
        if self._session_owner and self.session:
            self.session.close()
            self._session_owner = False
            self.session = None

    def send(self, request, **kwargs): # type: ignore
        # type: (HttpRequest, Any) -> HttpResponse
        """Send request object according to configuration.

        :param request: The request object to be sent.
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: An HTTPResponse object.
        :rtype: ~azure.core.pipeline.transport.HttpResponse

        :keyword requests.Session session: will override the driver session and use yours.
         Should NOT be done unless really required. Anything else is sent straight to requests.
        :keyword dict proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """
        self.open()
        response = None
        error = None # type: Optional[Union[ServiceRequestError, ServiceResponseError]]

        try:
            connection_timeout = kwargs.pop('connection_timeout', self.connection_config.timeout)

            if isinstance(connection_timeout, tuple):
                if 'read_timeout' in kwargs:
                    raise ValueError('Cannot set tuple connection_timeout and read_timeout together')
                _LOGGER.warning("Tuple timeout setting is deprecated")
                timeout = connection_timeout
            else:
                read_timeout = kwargs.pop('read_timeout', self.connection_config.read_timeout)
                timeout = (connection_timeout, read_timeout)
            response = self.session.request(  # type: ignore
                request.method,
                request.url,
                headers=request.headers,
                data=request.data,
                files=request.files,
                verify=kwargs.pop('connection_verify', self.connection_config.verify),
                timeout=timeout,
                cert=kwargs.pop('connection_cert', self.connection_config.cert),
                allow_redirects=False,
                hooks=_get_request_hooks(kwargs.pop('hooks', None)),
                **kwargs)

        except (urllib3.exceptions.NewConnectionError, urllib3.exceptions.ConnectTimeoutError) as err:
            error = ServiceRequestError(err, error=err)
        except requests.exceptions.ReadTimeout as err:
            error = ServiceResponseError(err, error=err)
        except requests.exceptions.ConnectionError as err:
            if err.args and isinstance(err.args[0], urllib3.exceptions.ProtocolError):
                error = ServiceResponseError(err, error=err)
            else:
                error = ServiceRequestError(err, error=err)
        except requests.exceptions.ChunkedEncodingError as err:
            error = IncompleteReadError(err, error=err)
        except requests.RequestException as err:
            error = ServiceRequestError(err, error=err)

        if error:
            raise error
        return RequestsTransportResponse(request, response, self.connection_config.data_block_size)
