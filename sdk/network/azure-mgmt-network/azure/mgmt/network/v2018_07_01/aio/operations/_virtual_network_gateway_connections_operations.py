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
from ...operations._virtual_network_gateway_connections_operations import (
    build_create_or_update_request_initial,
    build_delete_request_initial,
    build_get_request,
    build_get_shared_key_request,
    build_list_request,
    build_reset_shared_key_request_initial,
    build_set_shared_key_request_initial,
    build_update_tags_request_initial,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualNetworkGatewayConnectionsOperations:
    """VirtualNetworkGatewayConnectionsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2018_07_01.models
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

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.VirtualNetworkGatewayConnection",
        **kwargs: Any
    ) -> "_models.VirtualNetworkGatewayConnection":
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualNetworkGatewayConnection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "VirtualNetworkGatewayConnection")

        request = build_create_or_update_request_initial(
            resource_group_name=resource_group_name,
            virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
            subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("VirtualNetworkGatewayConnection", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("VirtualNetworkGatewayConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}"}  # type: ignore

    async def begin_create_or_update(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.VirtualNetworkGatewayConnection",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.VirtualNetworkGatewayConnection"]:
        """Creates or updates a virtual network gateway connection in the specified resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_network_gateway_connection_name: The name of the virtual network gateway
         connection.
        :type virtual_network_gateway_connection_name: str
        :param parameters: Parameters supplied to the create or update virtual network gateway
         connection operation.
        :type parameters: ~azure.mgmt.network.v2018_07_01.models.VirtualNetworkGatewayConnection
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualNetworkGatewayConnection or
         the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2018_07_01.models.VirtualNetworkGatewayConnection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualNetworkGatewayConnection"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("VirtualNetworkGatewayConnection", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, **kwargs)
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

    begin_create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}"}  # type: ignore

    async def get(
        self, resource_group_name: str, virtual_network_gateway_connection_name: str, **kwargs: Any
    ) -> "_models.VirtualNetworkGatewayConnection":
        """Gets the specified virtual network gateway connection by resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_network_gateway_connection_name: The name of the virtual network gateway
         connection.
        :type virtual_network_gateway_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualNetworkGatewayConnection, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2018_07_01.models.VirtualNetworkGatewayConnection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualNetworkGatewayConnection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            resource_group_name=resource_group_name,
            virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
            subscription_id=self._config.subscription_id,
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

        deserialized = self._deserialize("VirtualNetworkGatewayConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}"}  # type: ignore

    async def _delete_initial(
        self, resource_group_name: str, virtual_network_gateway_connection_name: str, **kwargs: Any
    ) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_delete_request_initial(
            resource_group_name=resource_group_name,
            virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
            subscription_id=self._config.subscription_id,
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

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}"}  # type: ignore

    async def begin_delete(
        self, resource_group_name: str, virtual_network_gateway_connection_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes the specified virtual network Gateway connection.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_network_gateway_connection_name: The name of the virtual network gateway
         connection.
        :type virtual_network_gateway_connection_name: str
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
                virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
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

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}"}  # type: ignore

    async def _update_tags_initial(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.TagsObject",
        **kwargs: Any
    ) -> "_models.VirtualNetworkGatewayConnection":
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualNetworkGatewayConnection"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "TagsObject")

        request = build_update_tags_request_initial(
            resource_group_name=resource_group_name,
            virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self._update_tags_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VirtualNetworkGatewayConnection", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_tags_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}"}  # type: ignore

    async def begin_update_tags(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.TagsObject",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.VirtualNetworkGatewayConnection"]:
        """Updates a virtual network gateway connection tags.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_network_gateway_connection_name: The name of the virtual network gateway
         connection.
        :type virtual_network_gateway_connection_name: str
        :param parameters: Parameters supplied to update virtual network gateway connection tags.
        :type parameters: ~azure.mgmt.network.v2018_07_01.models.TagsObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualNetworkGatewayConnection or
         the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2018_07_01.models.VirtualNetworkGatewayConnection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualNetworkGatewayConnection"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._update_tags_initial(
                resource_group_name=resource_group_name,
                virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("VirtualNetworkGatewayConnection", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, **kwargs)
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

    begin_update_tags.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}"}  # type: ignore

    async def _set_shared_key_initial(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.ConnectionSharedKey",
        **kwargs: Any
    ) -> "_models.ConnectionSharedKey":
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ConnectionSharedKey"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "ConnectionSharedKey")

        request = build_set_shared_key_request_initial(
            resource_group_name=resource_group_name,
            virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self._set_shared_key_initial.metadata["url"],
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
            deserialized = self._deserialize("ConnectionSharedKey", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ConnectionSharedKey", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _set_shared_key_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey"}  # type: ignore

    async def begin_set_shared_key(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.ConnectionSharedKey",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.ConnectionSharedKey"]:
        """The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway
        connection shared key for passed virtual network gateway connection in the specified resource
        group through Network resource provider.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_network_gateway_connection_name: The virtual network gateway connection name.
        :type virtual_network_gateway_connection_name: str
        :param parameters: Parameters supplied to the Begin Set Virtual Network Gateway connection
         Shared key operation throughNetwork resource provider.
        :type parameters: ~azure.mgmt.network.v2018_07_01.models.ConnectionSharedKey
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either ConnectionSharedKey or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2018_07_01.models.ConnectionSharedKey]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ConnectionSharedKey"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._set_shared_key_initial(
                resource_group_name=resource_group_name,
                virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("ConnectionSharedKey", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = AsyncARMPolling(lro_delay, **kwargs)
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

    begin_set_shared_key.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey"}  # type: ignore

    async def get_shared_key(
        self, resource_group_name: str, virtual_network_gateway_connection_name: str, **kwargs: Any
    ) -> "_models.ConnectionSharedKey":
        """The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the
        specified virtual network gateway connection shared key through Network resource provider.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_network_gateway_connection_name: The virtual network gateway connection shared
         key name.
        :type virtual_network_gateway_connection_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConnectionSharedKey, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2018_07_01.models.ConnectionSharedKey
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ConnectionSharedKey"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_shared_key_request(
            resource_group_name=resource_group_name,
            virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
            subscription_id=self._config.subscription_id,
            template_url=self.get_shared_key.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConnectionSharedKey", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_shared_key.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey"}  # type: ignore

    def list(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.VirtualNetworkGatewayConnectionListResult"]:
        """The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways
        connections created.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either VirtualNetworkGatewayConnectionListResult or the
         result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2018_07_01.models.VirtualNetworkGatewayConnectionListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualNetworkGatewayConnectionListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("VirtualNetworkGatewayConnectionListResult", pipeline_response)
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

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections"}  # type: ignore

    async def _reset_shared_key_initial(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.ConnectionResetSharedKey",
        **kwargs: Any
    ) -> Optional["_models.ConnectionResetSharedKey"]:
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.ConnectionResetSharedKey"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "ConnectionResetSharedKey")

        request = build_reset_shared_key_request_initial(
            resource_group_name=resource_group_name,
            virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self._reset_shared_key_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("ConnectionResetSharedKey", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _reset_shared_key_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey/reset"}  # type: ignore

    async def begin_reset_shared_key(
        self,
        resource_group_name: str,
        virtual_network_gateway_connection_name: str,
        parameters: "_models.ConnectionResetSharedKey",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.ConnectionResetSharedKey"]:
        """The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway
        connection shared key for passed virtual network gateway connection in the specified resource
        group through Network resource provider.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_network_gateway_connection_name: The virtual network gateway connection reset
         shared key Name.
        :type virtual_network_gateway_connection_name: str
        :param parameters: Parameters supplied to the begin reset virtual network gateway connection
         shared key operation through network resource provider.
        :type parameters: ~azure.mgmt.network.v2018_07_01.models.ConnectionResetSharedKey
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either ConnectionResetSharedKey or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2018_07_01.models.ConnectionResetSharedKey]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.ConnectionResetSharedKey"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._reset_shared_key_initial(
                resource_group_name=resource_group_name,
                virtual_network_gateway_connection_name=virtual_network_gateway_connection_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("ConnectionResetSharedKey", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

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

    begin_reset_shared_key.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey/reset"}  # type: ignore
