# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._custom_locations_enums import *


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class CustomLocation(TrackedResource):
    """Custom Locations definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param identity: Identity for the resource.
    :type identity: ~azure.mgmt.extendedlocation.v2021_08_15.models.Identity
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~azure.mgmt.extendedlocation.v2021_08_15.models.SystemData
    :param authentication: This is optional input that contains the authentication that should be
     used to generate the namespace.
    :type authentication:
     ~azure.mgmt.extendedlocation.v2021_08_15.models.CustomLocationPropertiesAuthentication
    :param cluster_extension_ids: Contains the reference to the add-on that contains charts to
     deploy CRDs and operators.
    :type cluster_extension_ids: list[str]
    :param display_name: Display name for the Custom Locations location.
    :type display_name: str
    :param host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will perform
     a checkAccess API for listAdminCredentials permissions.
    :type host_resource_id: str
    :param host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
     Possible values include: "Kubernetes".
    :type host_type: str or ~azure.mgmt.extendedlocation.v2021_08_15.models.HostType
    :param namespace: Kubernetes namespace that will be created on the specified cluster.
    :type namespace: str
    :param provisioning_state: Provisioning State for the Custom Location.
    :type provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'authentication': {'key': 'properties.authentication', 'type': 'CustomLocationPropertiesAuthentication'},
        'cluster_extension_ids': {'key': 'properties.clusterExtensionIds', 'type': '[str]'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'host_resource_id': {'key': 'properties.hostResourceId', 'type': 'str'},
        'host_type': {'key': 'properties.hostType', 'type': 'str'},
        'namespace': {'key': 'properties.namespace', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        identity: Optional["Identity"] = None,
        authentication: Optional["CustomLocationPropertiesAuthentication"] = None,
        cluster_extension_ids: Optional[List[str]] = None,
        display_name: Optional[str] = None,
        host_resource_id: Optional[str] = None,
        host_type: Optional[Union[str, "HostType"]] = None,
        namespace: Optional[str] = None,
        provisioning_state: Optional[str] = None,
        **kwargs
    ):
        super(CustomLocation, self).__init__(tags=tags, location=location, **kwargs)
        self.identity = identity
        self.system_data = None
        self.authentication = authentication
        self.cluster_extension_ids = cluster_extension_ids
        self.display_name = display_name
        self.host_resource_id = host_resource_id
        self.host_type = host_type
        self.namespace = namespace
        self.provisioning_state = provisioning_state


class CustomLocationListResult(msrest.serialization.Model):
    """The List Custom Locations operation response.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    :ivar value: The list of Custom Locations.
    :vartype value: list[~azure.mgmt.extendedlocation.v2021_08_15.models.CustomLocation]
    """

    _validation = {
        'next_link': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[CustomLocation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CustomLocationListResult, self).__init__(**kwargs)
        self.next_link = None
        self.value = None


class CustomLocationOperation(msrest.serialization.Model):
    """Custom Locations operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar is_data_action: Is this Operation a data plane operation.
    :vartype is_data_action: bool
    :ivar name: The name of the compute operation.
    :vartype name: str
    :ivar origin: The origin of the compute operation.
    :vartype origin: str
    :ivar description: The description of the operation.
    :vartype description: str
    :ivar operation: The display name of the compute operation.
    :vartype operation: str
    :ivar provider: The resource provider for the operation.
    :vartype provider: str
    :ivar resource: The display name of the resource the operation applies to.
    :vartype resource: str
    """

    _validation = {
        'is_data_action': {'readonly': True},
        'name': {'readonly': True},
        'origin': {'readonly': True},
        'description': {'readonly': True},
        'operation': {'readonly': True},
        'provider': {'readonly': True},
        'resource': {'readonly': True},
    }

    _attribute_map = {
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'description': {'key': 'display.description', 'type': 'str'},
        'operation': {'key': 'display.operation', 'type': 'str'},
        'provider': {'key': 'display.provider', 'type': 'str'},
        'resource': {'key': 'display.resource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CustomLocationOperation, self).__init__(**kwargs)
        self.is_data_action = None
        self.name = None
        self.origin = None
        self.description = None
        self.operation = None
        self.provider = None
        self.resource = None


class CustomLocationOperationsList(msrest.serialization.Model):
    """Lists of Custom Locations operations.

    All required parameters must be populated in order to send to Azure.

    :param next_link: Next page of operations.
    :type next_link: str
    :param value: Required. Array of customLocationOperation.
    :type value: list[~azure.mgmt.extendedlocation.v2021_08_15.models.CustomLocationOperation]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[CustomLocationOperation]'},
    }

    def __init__(
        self,
        *,
        value: List["CustomLocationOperation"],
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(CustomLocationOperationsList, self).__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class CustomLocationPropertiesAuthentication(msrest.serialization.Model):
    """This is optional input that contains the authentication that should be used to generate the namespace.

    :param type: The type of the Custom Locations authentication.
    :type type: str
    :param value: The kubeconfig value.
    :type value: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        super(CustomLocationPropertiesAuthentication, self).__init__(**kwargs)
        self.type = type
        self.value = value


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)


class EnabledResourceType(ProxyResource):
    """EnabledResourceType definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~azure.mgmt.extendedlocation.v2021_08_15.models.SystemData
    :param cluster_extension_id: Cluster Extension ID.
    :type cluster_extension_id: str
    :param extension_type: Cluster Extension Type.
    :type extension_type: str
    :param types_metadata: Metadata of the Resource Type.
    :type types_metadata:
     list[~azure.mgmt.extendedlocation.v2021_08_15.models.EnabledResourceTypePropertiesTypesMetadataItem]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'cluster_extension_id': {'key': 'properties.clusterExtensionId', 'type': 'str'},
        'extension_type': {'key': 'properties.extensionType', 'type': 'str'},
        'types_metadata': {'key': 'properties.typesMetadata', 'type': '[EnabledResourceTypePropertiesTypesMetadataItem]'},
    }

    def __init__(
        self,
        *,
        cluster_extension_id: Optional[str] = None,
        extension_type: Optional[str] = None,
        types_metadata: Optional[List["EnabledResourceTypePropertiesTypesMetadataItem"]] = None,
        **kwargs
    ):
        super(EnabledResourceType, self).__init__(**kwargs)
        self.system_data = None
        self.cluster_extension_id = cluster_extension_id
        self.extension_type = extension_type
        self.types_metadata = types_metadata


class EnabledResourceTypePropertiesTypesMetadataItem(msrest.serialization.Model):
    """Metadata of the Resource Type.

    :param api_version: Api Version of Resource Type.
    :type api_version: str
    :param resource_provider_namespace: Resource Provider Namespace of Resource Type.
    :type resource_provider_namespace: str
    :param resource_type: Resource Type.
    :type resource_type: str
    """

    _attribute_map = {
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'resource_provider_namespace': {'key': 'resourceProviderNamespace', 'type': 'str'},
        'resource_type': {'key': 'resourceType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        api_version: Optional[str] = None,
        resource_provider_namespace: Optional[str] = None,
        resource_type: Optional[str] = None,
        **kwargs
    ):
        super(EnabledResourceTypePropertiesTypesMetadataItem, self).__init__(**kwargs)
        self.api_version = api_version
        self.resource_provider_namespace = resource_provider_namespace
        self.resource_type = resource_type


class EnabledResourceTypesListResult(msrest.serialization.Model):
    """List of EnabledResourceTypes definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    :ivar value: The list of EnabledResourceTypes available for a customLocation.
    :vartype value: list[~azure.mgmt.extendedlocation.v2021_08_15.models.EnabledResourceType]
    """

    _validation = {
        'next_link': {'readonly': True},
        'value': {'readonly': True},
    }

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[EnabledResourceType]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(EnabledResourceTypesListResult, self).__init__(**kwargs)
        self.next_link = None
        self.value = None


class ErrorAdditionalInfo(msrest.serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: any
    """

    _validation = {
        'type': {'readonly': True},
        'info': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'info': {'key': 'info', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorAdditionalInfo, self).__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(msrest.serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.extendedlocation.v2021_08_15.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.extendedlocation.v2021_08_15.models.ErrorAdditionalInfo]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'additional_info': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetail]'},
        'additional_info': {'key': 'additionalInfo', 'type': '[ErrorAdditionalInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(msrest.serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).

    :param error: The error object.
    :type error: ~azure.mgmt.extendedlocation.v2021_08_15.models.ErrorDetail
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetail'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetail"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class Identity(msrest.serialization.Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: "SystemAssigned", "None".
    :type type: str or ~azure.mgmt.extendedlocation.v2021_08_15.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "ResourceIdentityType"]] = None,
        **kwargs
    ):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class PatchableCustomLocations(msrest.serialization.Model):
    """The Custom Locations patchable resource definition.

    :param identity: Identity for the resource.
    :type identity: ~azure.mgmt.extendedlocation.v2021_08_15.models.Identity
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param authentication: This is optional input that contains the authentication that should be
     used to generate the namespace.
    :type authentication:
     ~azure.mgmt.extendedlocation.v2021_08_15.models.CustomLocationPropertiesAuthentication
    :param cluster_extension_ids: Contains the reference to the add-on that contains charts to
     deploy CRDs and operators.
    :type cluster_extension_ids: list[str]
    :param display_name: Display name for the Custom Locations location.
    :type display_name: str
    :param host_resource_id: Connected Cluster or AKS Cluster. The Custom Locations RP will perform
     a checkAccess API for listAdminCredentials permissions.
    :type host_resource_id: str
    :param host_type: Type of host the Custom Locations is referencing (Kubernetes, etc...).
     Possible values include: "Kubernetes".
    :type host_type: str or ~azure.mgmt.extendedlocation.v2021_08_15.models.HostType
    :param namespace: Kubernetes namespace that will be created on the specified cluster.
    :type namespace: str
    :param provisioning_state: Provisioning State for the Custom Location.
    :type provisioning_state: str
    """

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'Identity'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'authentication': {'key': 'properties.authentication', 'type': 'CustomLocationPropertiesAuthentication'},
        'cluster_extension_ids': {'key': 'properties.clusterExtensionIds', 'type': '[str]'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'host_resource_id': {'key': 'properties.hostResourceId', 'type': 'str'},
        'host_type': {'key': 'properties.hostType', 'type': 'str'},
        'namespace': {'key': 'properties.namespace', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        identity: Optional["Identity"] = None,
        tags: Optional[Dict[str, str]] = None,
        authentication: Optional["CustomLocationPropertiesAuthentication"] = None,
        cluster_extension_ids: Optional[List[str]] = None,
        display_name: Optional[str] = None,
        host_resource_id: Optional[str] = None,
        host_type: Optional[Union[str, "HostType"]] = None,
        namespace: Optional[str] = None,
        provisioning_state: Optional[str] = None,
        **kwargs
    ):
        super(PatchableCustomLocations, self).__init__(**kwargs)
        self.identity = identity
        self.tags = tags
        self.authentication = authentication
        self.cluster_extension_ids = cluster_extension_ids
        self.display_name = display_name
        self.host_resource_id = host_resource_id
        self.host_type = host_type
        self.namespace = namespace
        self.provisioning_state = provisioning_state


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~azure.mgmt.extendedlocation.v2021_08_15.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or
     ~azure.mgmt.extendedlocation.v2021_08_15.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC).
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
