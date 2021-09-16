# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import DataMigrationManagementClientConfiguration
from .operations import ResourceSkusOperations
from .operations import ServicesOperations
from .operations import TasksOperations
from .operations import ServiceTasksOperations
from .operations import ProjectsOperations
from .operations import UsagesOperations
from .operations import Operations
from .operations import FilesOperations
from . import models


class DataMigrationManagementClient(object):
    """Data Migration Client.

    :ivar resource_skus: ResourceSkusOperations operations
    :vartype resource_skus: azure.mgmt.datamigration.operations.ResourceSkusOperations
    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.datamigration.operations.ServicesOperations
    :ivar tasks: TasksOperations operations
    :vartype tasks: azure.mgmt.datamigration.operations.TasksOperations
    :ivar service_tasks: ServiceTasksOperations operations
    :vartype service_tasks: azure.mgmt.datamigration.operations.ServiceTasksOperations
    :ivar projects: ProjectsOperations operations
    :vartype projects: azure.mgmt.datamigration.operations.ProjectsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.datamigration.operations.UsagesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datamigration.operations.Operations
    :ivar files: FilesOperations operations
    :vartype files: azure.mgmt.datamigration.operations.FilesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Identifier of the subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataMigrationManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.resource_skus = ResourceSkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.services = ServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tasks = TasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.service_tasks = ServiceTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.projects = ProjectsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.files = FilesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataMigrationManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
