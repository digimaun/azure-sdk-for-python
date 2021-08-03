# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ...operations._express_route_ports_operations import (
    build_create_or_update_request_initial,
    build_delete_request_initial,
    build_generate_loa_request,
    build_get_request,
    build_list_by_resource_group_request,
    build_list_request,
    build_update_tags_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ExpressRoutePortsOperations:
    """ExpressRoutePortsOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def _delete_initial(self, resource_group_name: str, express_route_port_name: str, **kwargs: Any) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_delete_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            express_route_port_name=express_route_port_name,
            template_url=self._delete_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}"}  # type: ignore

    async def begin_delete(
        self, resource_group_name: str, express_route_port_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes the specified ExpressRoutePort resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param express_route_port_name: The name of the ExpressRoutePort resource.
        :type express_route_port_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                express_route_port_name=express_route_port_name,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}"}  # type: ignore

    async def get(
        self, resource_group_name: str, express_route_port_name: str, **kwargs: Any
    ) -> "_models.ExpressRoutePort":
        """Retrieves the requested ExpressRoutePort resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param express_route_port_name: The name of ExpressRoutePort.
        :type express_route_port_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExpressRoutePort, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2020_11_01.models.ExpressRoutePort
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ExpressRoutePort"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            express_route_port_name=express_route_port_name,
            template_url=self.get.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExpressRoutePort", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}"}  # type: ignore

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        express_route_port_name: str,
        parameters: "_models.ExpressRoutePort",
        **kwargs: Any
    ) -> "_models.ExpressRoutePort":
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ExpressRoutePort"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "ExpressRoutePort")

        request = build_create_or_update_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            express_route_port_name=express_route_port_name,
            content_type=content_type,
            json=json,
            template_url=self._create_or_update_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ExpressRoutePort", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ExpressRoutePort", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}"}  # type: ignore

    async def begin_create_or_update(
        self,
        resource_group_name: str,
        express_route_port_name: str,
        parameters: "_models.ExpressRoutePort",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.ExpressRoutePort"]:
        """Creates or updates the specified ExpressRoutePort resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param express_route_port_name: The name of the ExpressRoutePort resource.
        :type express_route_port_name: str
        :param parameters: Parameters supplied to the create ExpressRoutePort operation.
        :type parameters: ~azure.mgmt.network.v2020_11_01.models.ExpressRoutePort
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either ExpressRoutePort or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2020_11_01.models.ExpressRoutePort]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ExpressRoutePort"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                express_route_port_name=express_route_port_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("ExpressRoutePort", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = AsyncARMPolling(
                lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs
            )
        elif polling is False:
            polling_method = AsyncNoPolling()
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}"}  # type: ignore

    async def update_tags(
        self, resource_group_name: str, express_route_port_name: str, parameters: "_models.TagsObject", **kwargs: Any
    ) -> "_models.ExpressRoutePort":
        """Update ExpressRoutePort tags.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param express_route_port_name: The name of the ExpressRoutePort resource.
        :type express_route_port_name: str
        :param parameters: Parameters supplied to update ExpressRoutePort resource tags.
        :type parameters: ~azure.mgmt.network.v2020_11_01.models.TagsObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExpressRoutePort, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2020_11_01.models.ExpressRoutePort
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ExpressRoutePort"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "TagsObject")

        request = build_update_tags_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            express_route_port_name=express_route_port_name,
            content_type=content_type,
            json=json,
            template_url=self.update_tags.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ExpressRoutePort", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update_tags.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}"}  # type: ignore

    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.ExpressRoutePortListResult"]:
        """List all the ExpressRoutePort resources in the specified resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ExpressRoutePortListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2020_11_01.models.ExpressRoutePortListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ExpressRoutePortListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    template_url=self.list_by_resource_group.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ExpressRoutePortListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts"}  # type: ignore

    def list(self, **kwargs: Any) -> AsyncIterable["_models.ExpressRoutePortListResult"]:
        """List all the ExpressRoutePort resources in the specified subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ExpressRoutePortListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2020_11_01.models.ExpressRoutePortListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ExpressRoutePortListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ExpressRoutePortListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePorts"}  # type: ignore

    async def generate_loa(
        self,
        resource_group_name: str,
        express_route_port_name: str,
        request: "_models.GenerateExpressRoutePortsLOARequest",
        **kwargs: Any
    ) -> "_models.GenerateExpressRoutePortsLOAResult":
        """Generate a letter of authorization for the requested ExpressRoutePort resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param express_route_port_name: The name of ExpressRoutePort.
        :type express_route_port_name: str
        :param request: Request parameters supplied to generate a letter of authorization.
        :type request: ~azure.mgmt.network.v2020_11_01.models.GenerateExpressRoutePortsLOARequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GenerateExpressRoutePortsLOAResult, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2020_11_01.models.GenerateExpressRoutePortsLOAResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.GenerateExpressRoutePortsLOAResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(request, "GenerateExpressRoutePortsLOARequest")

        request = build_generate_loa_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            express_route_port_name=express_route_port_name,
            content_type=content_type,
            json=json,
            template_url=self.generate_loa.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GenerateExpressRoutePortsLOAResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    generate_loa.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRoutePorts/{expressRoutePortName}/generateLoa"}  # type: ignore
