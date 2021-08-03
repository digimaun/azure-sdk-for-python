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
from ...operations._public_ip_addresses_operations import (
    build_create_or_update_request_initial,
    build_delete_request_initial,
    build_get_request,
    build_get_virtual_machine_scale_set_public_ip_address_request,
    build_list_all_request,
    build_list_request,
    build_list_virtual_machine_scale_set_public_ip_addresses_request,
    build_list_virtual_machine_scale_set_vm_public_ip_addresses_request,
    build_update_tags_request_initial,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PublicIPAddressesOperations:
    """PublicIPAddressesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.network.v2018_06_01.models
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

    async def _delete_initial(self, resource_group_name: str, public_ip_address_name: str, **kwargs: Any) -> None:
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_delete_request_initial(
            resource_group_name=resource_group_name,
            public_ip_address_name=public_ip_address_name,
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

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}"}  # type: ignore

    async def begin_delete(
        self, resource_group_name: str, public_ip_address_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes the specified public IP address.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the subnet.
        :type public_ip_address_name: str
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
                public_ip_address_name=public_ip_address_name,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

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

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}"}  # type: ignore

    async def get(
        self, resource_group_name: str, public_ip_address_name: str, expand: Optional[str] = None, **kwargs: Any
    ) -> "_models.PublicIPAddress":
        """Gets the specified public IP address in a specified resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the subnet.
        :type public_ip_address_name: str
        :param expand: Expands referenced resources.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PublicIPAddress, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2018_06_01.models.PublicIPAddress
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddress"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_request(
            resource_group_name=resource_group_name,
            public_ip_address_name=public_ip_address_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
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

        deserialized = self._deserialize("PublicIPAddress", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}"}  # type: ignore

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        public_ip_address_name: str,
        parameters: "_models.PublicIPAddress",
        **kwargs: Any
    ) -> "_models.PublicIPAddress":
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddress"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "PublicIPAddress")

        request = build_create_or_update_request_initial(
            resource_group_name=resource_group_name,
            public_ip_address_name=public_ip_address_name,
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
            deserialized = self._deserialize("PublicIPAddress", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("PublicIPAddress", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}"}  # type: ignore

    async def begin_create_or_update(
        self,
        resource_group_name: str,
        public_ip_address_name: str,
        parameters: "_models.PublicIPAddress",
        **kwargs: Any
    ) -> AsyncLROPoller["_models.PublicIPAddress"]:
        """Creates or updates a static or dynamic public IP address.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the public IP address.
        :type public_ip_address_name: str
        :param parameters: Parameters supplied to the create or update public IP address operation.
        :type parameters: ~azure.mgmt.network.v2018_06_01.models.PublicIPAddress
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either PublicIPAddress or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2018_06_01.models.PublicIPAddress]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddress"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                public_ip_address_name=public_ip_address_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("PublicIPAddress", pipeline_response)

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

    begin_create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}"}  # type: ignore

    async def _update_tags_initial(
        self, resource_group_name: str, public_ip_address_name: str, parameters: "_models.TagsObject", **kwargs: Any
    ) -> "_models.PublicIPAddress":
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddress"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "TagsObject")

        request = build_update_tags_request_initial(
            resource_group_name=resource_group_name,
            public_ip_address_name=public_ip_address_name,
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

        deserialized = self._deserialize("PublicIPAddress", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_tags_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}"}  # type: ignore

    async def begin_update_tags(
        self, resource_group_name: str, public_ip_address_name: str, parameters: "_models.TagsObject", **kwargs: Any
    ) -> AsyncLROPoller["_models.PublicIPAddress"]:
        """Updates public IP address tags.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param public_ip_address_name: The name of the public IP address.
        :type public_ip_address_name: str
        :param parameters: Parameters supplied to update public IP address tags.
        :type parameters: ~azure.mgmt.network.v2018_06_01.models.TagsObject
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either PublicIPAddress or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2018_06_01.models.PublicIPAddress]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddress"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._update_tags_initial(
                resource_group_name=resource_group_name,
                public_ip_address_name=public_ip_address_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("PublicIPAddress", pipeline_response)

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

    begin_update_tags.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses/{publicIpAddressName}"}  # type: ignore

    def list_all(self, **kwargs: Any) -> AsyncIterable["_models.PublicIPAddressListResult"]:
        """Gets all the public IP addresses in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PublicIPAddressListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2018_06_01.models.PublicIPAddressListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddressListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_all_request(
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_all.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_all_request(
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PublicIPAddressListResult", pipeline_response)
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

    list_all.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Network/publicIPAddresses"}  # type: ignore

    def list(self, resource_group_name: str, **kwargs: Any) -> AsyncIterable["_models.PublicIPAddressListResult"]:
        """Gets all public IP addresses in a resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PublicIPAddressListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2018_06_01.models.PublicIPAddressListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddressListResult"]
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
            deserialized = self._deserialize("PublicIPAddressListResult", pipeline_response)
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

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPAddresses"}  # type: ignore

    def list_virtual_machine_scale_set_public_ip_addresses(
        self, resource_group_name: str, virtual_machine_scale_set_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.PublicIPAddressListResult"]:
        """Gets information about all public IP addresses on a virtual machine scale set level.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
        :type virtual_machine_scale_set_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PublicIPAddressListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2018_06_01.models.PublicIPAddressListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddressListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_virtual_machine_scale_set_public_ip_addresses_request(
                    resource_group_name=resource_group_name,
                    virtual_machine_scale_set_name=virtual_machine_scale_set_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_virtual_machine_scale_set_public_ip_addresses.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_virtual_machine_scale_set_public_ip_addresses_request(
                    resource_group_name=resource_group_name,
                    virtual_machine_scale_set_name=virtual_machine_scale_set_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PublicIPAddressListResult", pipeline_response)
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

    list_virtual_machine_scale_set_public_ip_addresses.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/publicipaddresses"}  # type: ignore

    def list_virtual_machine_scale_set_vm_public_ip_addresses(
        self,
        resource_group_name: str,
        virtual_machine_scale_set_name: str,
        virtualmachine_index: str,
        network_interface_name: str,
        ip_configuration_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.PublicIPAddressListResult"]:
        """Gets information about all public IP addresses in a virtual machine IP configuration in a
        virtual machine scale set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
        :type virtual_machine_scale_set_name: str
        :param virtualmachine_index: The virtual machine index.
        :type virtualmachine_index: str
        :param network_interface_name: The network interface name.
        :type network_interface_name: str
        :param ip_configuration_name: The IP configuration name.
        :type ip_configuration_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PublicIPAddressListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2018_06_01.models.PublicIPAddressListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddressListResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_virtual_machine_scale_set_vm_public_ip_addresses_request(
                    resource_group_name=resource_group_name,
                    virtual_machine_scale_set_name=virtual_machine_scale_set_name,
                    virtualmachine_index=virtualmachine_index,
                    network_interface_name=network_interface_name,
                    ip_configuration_name=ip_configuration_name,
                    subscription_id=self._config.subscription_id,
                    template_url=self.list_virtual_machine_scale_set_vm_public_ip_addresses.metadata["url"],
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

            else:

                request = build_list_virtual_machine_scale_set_vm_public_ip_addresses_request(
                    resource_group_name=resource_group_name,
                    virtual_machine_scale_set_name=virtual_machine_scale_set_name,
                    virtualmachine_index=virtualmachine_index,
                    network_interface_name=network_interface_name,
                    ip_configuration_name=ip_configuration_name,
                    subscription_id=self._config.subscription_id,
                    template_url=next_link,
                )._to_pipeline_transport_request()
                request.url = self._client.format_url(request.url)

                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PublicIPAddressListResult", pipeline_response)
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

    list_virtual_machine_scale_set_vm_public_ip_addresses.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses"}  # type: ignore

    async def get_virtual_machine_scale_set_public_ip_address(
        self,
        resource_group_name: str,
        virtual_machine_scale_set_name: str,
        virtualmachine_index: str,
        network_interface_name: str,
        ip_configuration_name: str,
        public_ip_address_name: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.PublicIPAddress":
        """Get the specified public IP address in a virtual machine scale set.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param virtual_machine_scale_set_name: The name of the virtual machine scale set.
        :type virtual_machine_scale_set_name: str
        :param virtualmachine_index: The virtual machine index.
        :type virtualmachine_index: str
        :param network_interface_name: The name of the network interface.
        :type network_interface_name: str
        :param ip_configuration_name: The name of the IP configuration.
        :type ip_configuration_name: str
        :param public_ip_address_name: The name of the public IP Address.
        :type public_ip_address_name: str
        :param expand: Expands referenced resources.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PublicIPAddress, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2018_06_01.models.PublicIPAddress
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PublicIPAddress"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_virtual_machine_scale_set_public_ip_address_request(
            resource_group_name=resource_group_name,
            virtual_machine_scale_set_name=virtual_machine_scale_set_name,
            virtualmachine_index=virtualmachine_index,
            network_interface_name=network_interface_name,
            ip_configuration_name=ip_configuration_name,
            public_ip_address_name=public_ip_address_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            template_url=self.get_virtual_machine_scale_set_public_ip_address.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PublicIPAddress", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_virtual_machine_scale_set_public_ip_address.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines/{virtualmachineIndex}/networkInterfaces/{networkInterfaceName}/ipconfigurations/{ipConfigurationName}/publicipaddresses/{publicIpAddressName}"}  # type: ignore
