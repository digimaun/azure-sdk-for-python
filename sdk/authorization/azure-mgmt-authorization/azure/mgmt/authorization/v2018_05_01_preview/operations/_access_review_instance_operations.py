# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AccessReviewInstanceOperations(object):
    """AccessReviewInstanceOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.authorization.v2018_05_01_preview.models
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

    def stop(
        self,
        schedule_definition_id,  # type: str
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """An action to stop an access review instance.

        :param schedule_definition_id: The id of the access review schedule definition.
        :type schedule_definition_id: str
        :param id: The id of the access review instance.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.stop.metadata['url']  # type: ignore
        path_format_arguments = {
            'scheduleDefinitionId': self._serialize.url("schedule_definition_id", schedule_definition_id, 'str'),
            'id': self._serialize.url("id", id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    stop.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/stop'}  # type: ignore

    def reset_decisions(
        self,
        schedule_definition_id,  # type: str
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """An action to reset all decisions for an access review instance.

        :param schedule_definition_id: The id of the access review schedule definition.
        :type schedule_definition_id: str
        :param id: The id of the access review instance.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.reset_decisions.metadata['url']  # type: ignore
        path_format_arguments = {
            'scheduleDefinitionId': self._serialize.url("schedule_definition_id", schedule_definition_id, 'str'),
            'id': self._serialize.url("id", id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    reset_decisions.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/resetDecisions'}  # type: ignore

    def apply_decisions(
        self,
        schedule_definition_id,  # type: str
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """An action to apply all decisions for an access review instance.

        :param schedule_definition_id: The id of the access review schedule definition.
        :type schedule_definition_id: str
        :param id: The id of the access review instance.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.apply_decisions.metadata['url']  # type: ignore
        path_format_arguments = {
            'scheduleDefinitionId': self._serialize.url("schedule_definition_id", schedule_definition_id, 'str'),
            'id': self._serialize.url("id", id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    apply_decisions.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/applyDecisions'}  # type: ignore

    def send_reminders(
        self,
        schedule_definition_id,  # type: str
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """An action to send reminders for an access review instance.

        :param schedule_definition_id: The id of the access review schedule definition.
        :type schedule_definition_id: str
        :param id: The id of the access review instance.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.send_reminders.metadata['url']  # type: ignore
        path_format_arguments = {
            'scheduleDefinitionId': self._serialize.url("schedule_definition_id", schedule_definition_id, 'str'),
            'id': self._serialize.url("id", id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    send_reminders.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/sendReminders'}  # type: ignore

    def accept_recommendations(
        self,
        schedule_definition_id,  # type: str
        id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """An action to accept recommendations for decision in an access review instance.

        :param schedule_definition_id: The id of the access review schedule definition.
        :type schedule_definition_id: str
        :param id: The id of the access review instance.
        :type id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.accept_recommendations.metadata['url']  # type: ignore
        path_format_arguments = {
            'scheduleDefinitionId': self._serialize.url("schedule_definition_id", schedule_definition_id, 'str'),
            'id': self._serialize.url("id", id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    accept_recommendations.metadata = {'url': '/providers/Microsoft.Authorization/accessReviewScheduleDefinitions/{scheduleDefinitionId}/instances/{id}/acceptRecommendations'}  # type: ignore
