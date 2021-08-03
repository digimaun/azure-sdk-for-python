# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ...operations._network_management_client_operations import (
    build_check_dns_name_availability_request,
    build_supported_security_providers_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class NetworkManagementClientOperationsMixin:
    async def check_dns_name_availability(
        self, location: str, domain_name_label: str, **kwargs: Any
    ) -> "_models.DnsNameAvailabilityResult":
        """Checks whether a domain name in the cloudapp.azure.com zone is available for use.

        :param location: The location of the domain name.
        :type location: str
        :param domain_name_label: The domain name to be verified. It must conform to the following
         regular expression: ^[a-z][a-z0-9-]{1,61}[a-z0-9]$.
        :type domain_name_label: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DnsNameAvailabilityResult, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2019_06_01.models.DnsNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DnsNameAvailabilityResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_check_dns_name_availability_request(
            location=location,
            subscription_id=self._config.subscription_id,
            domain_name_label=domain_name_label,
            template_url=self.check_dns_name_availability.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DnsNameAvailabilityResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_dns_name_availability.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/CheckDnsNameAvailability"}  # type: ignore

    async def supported_security_providers(
        self, resource_group_name: str, virtual_wan_name: str, **kwargs: Any
    ) -> "_models.VirtualWanSecurityProviders":
        """Gives the supported security providers for the virtual wan.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param virtual_wan_name: The name of the VirtualWAN for which supported security providers are
         needed.
        :type virtual_wan_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualWanSecurityProviders, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2019_06_01.models.VirtualWanSecurityProviders
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.VirtualWanSecurityProviders"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_supported_security_providers_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            virtual_wan_name=virtual_wan_name,
            template_url=self.supported_security_providers.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("VirtualWanSecurityProviders", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    supported_security_providers.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{virtualWANName}/supportedSecurityProviders"}  # type: ignore
