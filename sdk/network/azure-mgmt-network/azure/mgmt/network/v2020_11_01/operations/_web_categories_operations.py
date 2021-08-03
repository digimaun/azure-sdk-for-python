# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_request(
    name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    expand = kwargs.pop('expand', None)  # type: Optional[str]

    api_version = "2020-11-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Network/azureWebCategories/{name}')
    path_format_arguments = {
        'name': _SERIALIZER.url("name", name, 'str'),
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if expand is not None:
        query_parameters['$expand'] = _SERIALIZER.query("expand", expand, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_by_subscription_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2020-11-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.Network/azureWebCategories')
    path_format_arguments = {
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class WebCategoriesOperations(object):
    """WebCategoriesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2020_11_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get(
        self,
        name,  # type: str
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AzureWebCategory"
        """Gets the specified Azure Web Category.

        :param name: The name of the azureWebCategory.
        :type name: str
        :param expand: Expands resourceIds back referenced by the azureWebCategory resource.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AzureWebCategory, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2020_11_01.models.AzureWebCategory
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.AzureWebCategory"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            name=name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            template_url=self.get.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AzureWebCategory", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Network/azureWebCategories/{name}"}  # type: ignore

    def list_by_subscription(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.AzureWebCategoryListResult"]
        """Gets all the Azure Web Categories in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AzureWebCategoryListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.network.v2020_11_01.models.AzureWebCategoryListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.AzureWebCategoryListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_by_subscription.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AzureWebCategoryListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_subscription.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Network/azureWebCategories"}  # type: ignore
