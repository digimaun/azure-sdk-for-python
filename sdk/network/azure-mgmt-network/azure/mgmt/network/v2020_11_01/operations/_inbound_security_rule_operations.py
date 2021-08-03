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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.pipeline.transport._base import _format_url_section
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling
from msrest import Serializer

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_create_or_update_request_initial(
    resource_group_name,  # type: str
    network_virtual_appliance_name,  # type: str
    rule_collection_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2020-11-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/inboundSecurityRules/{ruleCollectionName}')
    path_format_arguments = {
        'resourceGroupName': _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        'networkVirtualApplianceName': _SERIALIZER.url("network_virtual_appliance_name", network_virtual_appliance_name, 'str'),
        'ruleCollectionName': _SERIALIZER.url("rule_collection_name", rule_collection_name, 'str'),
        'subscriptionId': _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class InboundSecurityRuleOperations(object):
    """InboundSecurityRuleOperations operations.

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

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        network_virtual_appliance_name,  # type: str
        rule_collection_name,  # type: str
        parameters,  # type: "_models.InboundSecurityRule"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.InboundSecurityRule"
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.InboundSecurityRule"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(parameters, "InboundSecurityRule")

        request = build_create_or_update_request_initial(
            resource_group_name=resource_group_name,
            network_virtual_appliance_name=network_virtual_appliance_name,
            rule_collection_name=rule_collection_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            json=json,
            template_url=self._create_or_update_initial.metadata["url"],
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("InboundSecurityRule", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("InboundSecurityRule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/inboundSecurityRules/{ruleCollectionName}"}  # type: ignore

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        network_virtual_appliance_name,  # type: str
        rule_collection_name,  # type: str
        parameters,  # type: "_models.InboundSecurityRule"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.InboundSecurityRule"]
        """Creates or updates the specified Network Virtual Appliance Inbound Security Rules.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param network_virtual_appliance_name: The name of the Network Virtual Appliance.
        :type network_virtual_appliance_name: str
        :param rule_collection_name: The name of security rule collection.
        :type rule_collection_name: str
        :param parameters: Parameters supplied to the create or update Network Virtual Appliance
         Inbound Security Rules operation.
        :type parameters: ~azure.mgmt.network.v2020_11_01.models.InboundSecurityRule
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either InboundSecurityRule or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.network.v2020_11_01.models.InboundSecurityRule]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.InboundSecurityRule"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                resource_group_name=resource_group_name,
                network_virtual_appliance_name=network_virtual_appliance_name,
                rule_collection_name=rule_collection_name,
                parameters=parameters,
                content_type=content_type,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("InboundSecurityRule", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = ARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/inboundSecurityRules/{ruleCollectionName}"}  # type: ignore
