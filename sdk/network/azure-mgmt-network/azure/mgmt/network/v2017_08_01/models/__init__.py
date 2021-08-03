# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AddressSpace
    from ._models_py3 import ApplicationGateway
    from ._models_py3 import ApplicationGatewayAuthenticationCertificate
    from ._models_py3 import ApplicationGatewayAvailableSslOptions
    from ._models_py3 import ApplicationGatewayAvailableSslPredefinedPolicies
    from ._models_py3 import ApplicationGatewayAvailableWafRuleSetsResult
    from ._models_py3 import ApplicationGatewayBackendAddress
    from ._models_py3 import ApplicationGatewayBackendAddressPool
    from ._models_py3 import ApplicationGatewayBackendHealth
    from ._models_py3 import ApplicationGatewayBackendHealthHttpSettings
    from ._models_py3 import ApplicationGatewayBackendHealthPool
    from ._models_py3 import ApplicationGatewayBackendHealthServer
    from ._models_py3 import ApplicationGatewayBackendHttpSettings
    from ._models_py3 import ApplicationGatewayConnectionDraining
    from ._models_py3 import ApplicationGatewayFirewallDisabledRuleGroup
    from ._models_py3 import ApplicationGatewayFirewallRule
    from ._models_py3 import ApplicationGatewayFirewallRuleGroup
    from ._models_py3 import ApplicationGatewayFirewallRuleSet
    from ._models_py3 import ApplicationGatewayFrontendIPConfiguration
    from ._models_py3 import ApplicationGatewayFrontendPort
    from ._models_py3 import ApplicationGatewayHttpListener
    from ._models_py3 import ApplicationGatewayIPConfiguration
    from ._models_py3 import ApplicationGatewayListResult
    from ._models_py3 import ApplicationGatewayPathRule
    from ._models_py3 import ApplicationGatewayProbe
    from ._models_py3 import ApplicationGatewayProbeHealthResponseMatch
    from ._models_py3 import ApplicationGatewayRedirectConfiguration
    from ._models_py3 import ApplicationGatewayRequestRoutingRule
    from ._models_py3 import ApplicationGatewaySku
    from ._models_py3 import ApplicationGatewaySslCertificate
    from ._models_py3 import ApplicationGatewaySslPolicy
    from ._models_py3 import ApplicationGatewaySslPredefinedPolicy
    from ._models_py3 import ApplicationGatewayUrlPathMap
    from ._models_py3 import ApplicationGatewayWebApplicationFirewallConfiguration
    from ._models_py3 import AuthorizationListResult
    from ._models_py3 import AzureAsyncOperationResult
    from ._models_py3 import BGPCommunity
    from ._models_py3 import BackendAddressPool
    from ._models_py3 import BgpPeerStatus
    from ._models_py3 import BgpPeerStatusListResult
    from ._models_py3 import BgpServiceCommunity
    from ._models_py3 import BgpServiceCommunityListResult
    from ._models_py3 import BgpSettings
    from ._models_py3 import ConnectionResetSharedKey
    from ._models_py3 import ConnectionSharedKey
    from ._models_py3 import ConnectivityDestination
    from ._models_py3 import ConnectivityHop
    from ._models_py3 import ConnectivityInformation
    from ._models_py3 import ConnectivityIssue
    from ._models_py3 import ConnectivityParameters
    from ._models_py3 import ConnectivitySource
    from ._models_py3 import DhcpOptions
    from ._models_py3 import DnsNameAvailabilityResult
    from ._models_py3 import EffectiveNetworkSecurityGroup
    from ._models_py3 import EffectiveNetworkSecurityGroupAssociation
    from ._models_py3 import EffectiveNetworkSecurityGroupListResult
    from ._models_py3 import EffectiveNetworkSecurityRule
    from ._models_py3 import EffectiveRoute
    from ._models_py3 import EffectiveRouteListResult
    from ._models_py3 import EndpointServiceResult
    from ._models_py3 import EndpointServicesListResult
    from ._models_py3 import Error
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ExpressRouteCircuit
    from ._models_py3 import ExpressRouteCircuitArpTable
    from ._models_py3 import ExpressRouteCircuitAuthorization
    from ._models_py3 import ExpressRouteCircuitListResult
    from ._models_py3 import ExpressRouteCircuitPeering
    from ._models_py3 import ExpressRouteCircuitPeeringConfig
    from ._models_py3 import ExpressRouteCircuitPeeringListResult
    from ._models_py3 import ExpressRouteCircuitRoutesTable
    from ._models_py3 import ExpressRouteCircuitRoutesTableSummary
    from ._models_py3 import ExpressRouteCircuitServiceProviderProperties
    from ._models_py3 import ExpressRouteCircuitSku
    from ._models_py3 import ExpressRouteCircuitStats
    from ._models_py3 import ExpressRouteCircuitsArpTableListResult
    from ._models_py3 import ExpressRouteCircuitsRoutesTableListResult
    from ._models_py3 import ExpressRouteCircuitsRoutesTableSummaryListResult
    from ._models_py3 import ExpressRouteServiceProvider
    from ._models_py3 import ExpressRouteServiceProviderBandwidthsOffered
    from ._models_py3 import ExpressRouteServiceProviderListResult
    from ._models_py3 import FlowLogInformation
    from ._models_py3 import FlowLogStatusParameters
    from ._models_py3 import FrontendIPConfiguration
    from ._models_py3 import GatewayRoute
    from ._models_py3 import GatewayRouteListResult
    from ._models_py3 import IPAddressAvailabilityResult
    from ._models_py3 import IPConfiguration
    from ._models_py3 import InboundNatPool
    from ._models_py3 import InboundNatRule
    from ._models_py3 import InboundNatRuleListResult
    from ._models_py3 import IpsecPolicy
    from ._models_py3 import Ipv6ExpressRouteCircuitPeeringConfig
    from ._models_py3 import LoadBalancer
    from ._models_py3 import LoadBalancerBackendAddressPoolListResult
    from ._models_py3 import LoadBalancerFrontendIPConfigurationListResult
    from ._models_py3 import LoadBalancerListResult
    from ._models_py3 import LoadBalancerLoadBalancingRuleListResult
    from ._models_py3 import LoadBalancerProbeListResult
    from ._models_py3 import LoadBalancerSku
    from ._models_py3 import LoadBalancingRule
    from ._models_py3 import LocalNetworkGateway
    from ._models_py3 import LocalNetworkGatewayListResult
    from ._models_py3 import NetworkInterface
    from ._models_py3 import NetworkInterfaceAssociation
    from ._models_py3 import NetworkInterfaceDnsSettings
    from ._models_py3 import NetworkInterfaceIPConfiguration
    from ._models_py3 import NetworkInterfaceIPConfigurationListResult
    from ._models_py3 import NetworkInterfaceListResult
    from ._models_py3 import NetworkInterfaceLoadBalancerListResult
    from ._models_py3 import NetworkSecurityGroup
    from ._models_py3 import NetworkSecurityGroupListResult
    from ._models_py3 import NetworkWatcher
    from ._models_py3 import NetworkWatcherListResult
    from ._models_py3 import NextHopParameters
    from ._models_py3 import NextHopResult
    from ._models_py3 import OutboundNatRule
    from ._models_py3 import PacketCapture
    from ._models_py3 import PacketCaptureFilter
    from ._models_py3 import PacketCaptureListResult
    from ._models_py3 import PacketCaptureParameters
    from ._models_py3 import PacketCaptureQueryStatusResult
    from ._models_py3 import PacketCaptureResult
    from ._models_py3 import PacketCaptureResultProperties
    from ._models_py3 import PacketCaptureStorageLocation
    from ._models_py3 import PatchRouteFilter
    from ._models_py3 import PatchRouteFilterRule
    from ._models_py3 import Probe
    from ._models_py3 import PublicIPAddress
    from ._models_py3 import PublicIPAddressDnsSettings
    from ._models_py3 import PublicIPAddressListResult
    from ._models_py3 import PublicIPAddressSku
    from ._models_py3 import QueryTroubleshootingParameters
    from ._models_py3 import Resource
    from ._models_py3 import ResourceNavigationLink
    from ._models_py3 import RetentionPolicyParameters
    from ._models_py3 import Route
    from ._models_py3 import RouteFilter
    from ._models_py3 import RouteFilterListResult
    from ._models_py3 import RouteFilterRule
    from ._models_py3 import RouteFilterRuleListResult
    from ._models_py3 import RouteListResult
    from ._models_py3 import RouteTable
    from ._models_py3 import RouteTableListResult
    from ._models_py3 import SecurityGroupNetworkInterface
    from ._models_py3 import SecurityGroupViewParameters
    from ._models_py3 import SecurityGroupViewResult
    from ._models_py3 import SecurityRule
    from ._models_py3 import SecurityRuleAssociations
    from ._models_py3 import SecurityRuleListResult
    from ._models_py3 import ServiceEndpointPropertiesFormat
    from ._models_py3 import SubResource
    from ._models_py3 import Subnet
    from ._models_py3 import SubnetAssociation
    from ._models_py3 import SubnetListResult
    from ._models_py3 import Topology
    from ._models_py3 import TopologyAssociation
    from ._models_py3 import TopologyParameters
    from ._models_py3 import TopologyResource
    from ._models_py3 import TroubleshootingDetails
    from ._models_py3 import TroubleshootingParameters
    from ._models_py3 import TroubleshootingRecommendedActions
    from ._models_py3 import TroubleshootingResult
    from ._models_py3 import TunnelConnectionHealth
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UsagesListResult
    from ._models_py3 import VerificationIPFlowParameters
    from ._models_py3 import VerificationIPFlowResult
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkConnectionGatewayReference
    from ._models_py3 import VirtualNetworkGateway
    from ._models_py3 import VirtualNetworkGatewayConnection
    from ._models_py3 import VirtualNetworkGatewayConnectionListEntity
    from ._models_py3 import VirtualNetworkGatewayConnectionListResult
    from ._models_py3 import VirtualNetworkGatewayIPConfiguration
    from ._models_py3 import VirtualNetworkGatewayListConnectionsResult
    from ._models_py3 import VirtualNetworkGatewayListResult
    from ._models_py3 import VirtualNetworkGatewaySku
    from ._models_py3 import VirtualNetworkListResult
    from ._models_py3 import VirtualNetworkListUsageResult
    from ._models_py3 import VirtualNetworkPeering
    from ._models_py3 import VirtualNetworkPeeringListResult
    from ._models_py3 import VirtualNetworkUsage
    from ._models_py3 import VirtualNetworkUsageName
    from ._models_py3 import VpnClientConfiguration
    from ._models_py3 import VpnClientParameters
    from ._models_py3 import VpnClientRevokedCertificate
    from ._models_py3 import VpnClientRootCertificate
except (SyntaxError, ImportError):
    from ._models import AddressSpace  # type: ignore
    from ._models import ApplicationGateway  # type: ignore
    from ._models import ApplicationGatewayAuthenticationCertificate  # type: ignore
    from ._models import ApplicationGatewayAvailableSslOptions  # type: ignore
    from ._models import ApplicationGatewayAvailableSslPredefinedPolicies  # type: ignore
    from ._models import ApplicationGatewayAvailableWafRuleSetsResult  # type: ignore
    from ._models import ApplicationGatewayBackendAddress  # type: ignore
    from ._models import ApplicationGatewayBackendAddressPool  # type: ignore
    from ._models import ApplicationGatewayBackendHealth  # type: ignore
    from ._models import ApplicationGatewayBackendHealthHttpSettings  # type: ignore
    from ._models import ApplicationGatewayBackendHealthPool  # type: ignore
    from ._models import ApplicationGatewayBackendHealthServer  # type: ignore
    from ._models import ApplicationGatewayBackendHttpSettings  # type: ignore
    from ._models import ApplicationGatewayConnectionDraining  # type: ignore
    from ._models import ApplicationGatewayFirewallDisabledRuleGroup  # type: ignore
    from ._models import ApplicationGatewayFirewallRule  # type: ignore
    from ._models import ApplicationGatewayFirewallRuleGroup  # type: ignore
    from ._models import ApplicationGatewayFirewallRuleSet  # type: ignore
    from ._models import ApplicationGatewayFrontendIPConfiguration  # type: ignore
    from ._models import ApplicationGatewayFrontendPort  # type: ignore
    from ._models import ApplicationGatewayHttpListener  # type: ignore
    from ._models import ApplicationGatewayIPConfiguration  # type: ignore
    from ._models import ApplicationGatewayListResult  # type: ignore
    from ._models import ApplicationGatewayPathRule  # type: ignore
    from ._models import ApplicationGatewayProbe  # type: ignore
    from ._models import ApplicationGatewayProbeHealthResponseMatch  # type: ignore
    from ._models import ApplicationGatewayRedirectConfiguration  # type: ignore
    from ._models import ApplicationGatewayRequestRoutingRule  # type: ignore
    from ._models import ApplicationGatewaySku  # type: ignore
    from ._models import ApplicationGatewaySslCertificate  # type: ignore
    from ._models import ApplicationGatewaySslPolicy  # type: ignore
    from ._models import ApplicationGatewaySslPredefinedPolicy  # type: ignore
    from ._models import ApplicationGatewayUrlPathMap  # type: ignore
    from ._models import ApplicationGatewayWebApplicationFirewallConfiguration  # type: ignore
    from ._models import AuthorizationListResult  # type: ignore
    from ._models import AzureAsyncOperationResult  # type: ignore
    from ._models import BGPCommunity  # type: ignore
    from ._models import BackendAddressPool  # type: ignore
    from ._models import BgpPeerStatus  # type: ignore
    from ._models import BgpPeerStatusListResult  # type: ignore
    from ._models import BgpServiceCommunity  # type: ignore
    from ._models import BgpServiceCommunityListResult  # type: ignore
    from ._models import BgpSettings  # type: ignore
    from ._models import ConnectionResetSharedKey  # type: ignore
    from ._models import ConnectionSharedKey  # type: ignore
    from ._models import ConnectivityDestination  # type: ignore
    from ._models import ConnectivityHop  # type: ignore
    from ._models import ConnectivityInformation  # type: ignore
    from ._models import ConnectivityIssue  # type: ignore
    from ._models import ConnectivityParameters  # type: ignore
    from ._models import ConnectivitySource  # type: ignore
    from ._models import DhcpOptions  # type: ignore
    from ._models import DnsNameAvailabilityResult  # type: ignore
    from ._models import EffectiveNetworkSecurityGroup  # type: ignore
    from ._models import EffectiveNetworkSecurityGroupAssociation  # type: ignore
    from ._models import EffectiveNetworkSecurityGroupListResult  # type: ignore
    from ._models import EffectiveNetworkSecurityRule  # type: ignore
    from ._models import EffectiveRoute  # type: ignore
    from ._models import EffectiveRouteListResult  # type: ignore
    from ._models import EndpointServiceResult  # type: ignore
    from ._models import EndpointServicesListResult  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorDetails  # type: ignore
    from ._models import ExpressRouteCircuit  # type: ignore
    from ._models import ExpressRouteCircuitArpTable  # type: ignore
    from ._models import ExpressRouteCircuitAuthorization  # type: ignore
    from ._models import ExpressRouteCircuitListResult  # type: ignore
    from ._models import ExpressRouteCircuitPeering  # type: ignore
    from ._models import ExpressRouteCircuitPeeringConfig  # type: ignore
    from ._models import ExpressRouteCircuitPeeringListResult  # type: ignore
    from ._models import ExpressRouteCircuitRoutesTable  # type: ignore
    from ._models import ExpressRouteCircuitRoutesTableSummary  # type: ignore
    from ._models import ExpressRouteCircuitServiceProviderProperties  # type: ignore
    from ._models import ExpressRouteCircuitSku  # type: ignore
    from ._models import ExpressRouteCircuitStats  # type: ignore
    from ._models import ExpressRouteCircuitsArpTableListResult  # type: ignore
    from ._models import ExpressRouteCircuitsRoutesTableListResult  # type: ignore
    from ._models import ExpressRouteCircuitsRoutesTableSummaryListResult  # type: ignore
    from ._models import ExpressRouteServiceProvider  # type: ignore
    from ._models import ExpressRouteServiceProviderBandwidthsOffered  # type: ignore
    from ._models import ExpressRouteServiceProviderListResult  # type: ignore
    from ._models import FlowLogInformation  # type: ignore
    from ._models import FlowLogStatusParameters  # type: ignore
    from ._models import FrontendIPConfiguration  # type: ignore
    from ._models import GatewayRoute  # type: ignore
    from ._models import GatewayRouteListResult  # type: ignore
    from ._models import IPAddressAvailabilityResult  # type: ignore
    from ._models import IPConfiguration  # type: ignore
    from ._models import InboundNatPool  # type: ignore
    from ._models import InboundNatRule  # type: ignore
    from ._models import InboundNatRuleListResult  # type: ignore
    from ._models import IpsecPolicy  # type: ignore
    from ._models import Ipv6ExpressRouteCircuitPeeringConfig  # type: ignore
    from ._models import LoadBalancer  # type: ignore
    from ._models import LoadBalancerBackendAddressPoolListResult  # type: ignore
    from ._models import LoadBalancerFrontendIPConfigurationListResult  # type: ignore
    from ._models import LoadBalancerListResult  # type: ignore
    from ._models import LoadBalancerLoadBalancingRuleListResult  # type: ignore
    from ._models import LoadBalancerProbeListResult  # type: ignore
    from ._models import LoadBalancerSku  # type: ignore
    from ._models import LoadBalancingRule  # type: ignore
    from ._models import LocalNetworkGateway  # type: ignore
    from ._models import LocalNetworkGatewayListResult  # type: ignore
    from ._models import NetworkInterface  # type: ignore
    from ._models import NetworkInterfaceAssociation  # type: ignore
    from ._models import NetworkInterfaceDnsSettings  # type: ignore
    from ._models import NetworkInterfaceIPConfiguration  # type: ignore
    from ._models import NetworkInterfaceIPConfigurationListResult  # type: ignore
    from ._models import NetworkInterfaceListResult  # type: ignore
    from ._models import NetworkInterfaceLoadBalancerListResult  # type: ignore
    from ._models import NetworkSecurityGroup  # type: ignore
    from ._models import NetworkSecurityGroupListResult  # type: ignore
    from ._models import NetworkWatcher  # type: ignore
    from ._models import NetworkWatcherListResult  # type: ignore
    from ._models import NextHopParameters  # type: ignore
    from ._models import NextHopResult  # type: ignore
    from ._models import OutboundNatRule  # type: ignore
    from ._models import PacketCapture  # type: ignore
    from ._models import PacketCaptureFilter  # type: ignore
    from ._models import PacketCaptureListResult  # type: ignore
    from ._models import PacketCaptureParameters  # type: ignore
    from ._models import PacketCaptureQueryStatusResult  # type: ignore
    from ._models import PacketCaptureResult  # type: ignore
    from ._models import PacketCaptureResultProperties  # type: ignore
    from ._models import PacketCaptureStorageLocation  # type: ignore
    from ._models import PatchRouteFilter  # type: ignore
    from ._models import PatchRouteFilterRule  # type: ignore
    from ._models import Probe  # type: ignore
    from ._models import PublicIPAddress  # type: ignore
    from ._models import PublicIPAddressDnsSettings  # type: ignore
    from ._models import PublicIPAddressListResult  # type: ignore
    from ._models import PublicIPAddressSku  # type: ignore
    from ._models import QueryTroubleshootingParameters  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceNavigationLink  # type: ignore
    from ._models import RetentionPolicyParameters  # type: ignore
    from ._models import Route  # type: ignore
    from ._models import RouteFilter  # type: ignore
    from ._models import RouteFilterListResult  # type: ignore
    from ._models import RouteFilterRule  # type: ignore
    from ._models import RouteFilterRuleListResult  # type: ignore
    from ._models import RouteListResult  # type: ignore
    from ._models import RouteTable  # type: ignore
    from ._models import RouteTableListResult  # type: ignore
    from ._models import SecurityGroupNetworkInterface  # type: ignore
    from ._models import SecurityGroupViewParameters  # type: ignore
    from ._models import SecurityGroupViewResult  # type: ignore
    from ._models import SecurityRule  # type: ignore
    from ._models import SecurityRuleAssociations  # type: ignore
    from ._models import SecurityRuleListResult  # type: ignore
    from ._models import ServiceEndpointPropertiesFormat  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import Subnet  # type: ignore
    from ._models import SubnetAssociation  # type: ignore
    from ._models import SubnetListResult  # type: ignore
    from ._models import Topology  # type: ignore
    from ._models import TopologyAssociation  # type: ignore
    from ._models import TopologyParameters  # type: ignore
    from ._models import TopologyResource  # type: ignore
    from ._models import TroubleshootingDetails  # type: ignore
    from ._models import TroubleshootingParameters  # type: ignore
    from ._models import TroubleshootingRecommendedActions  # type: ignore
    from ._models import TroubleshootingResult  # type: ignore
    from ._models import TunnelConnectionHealth  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import UsagesListResult  # type: ignore
    from ._models import VerificationIPFlowParameters  # type: ignore
    from ._models import VerificationIPFlowResult  # type: ignore
    from ._models import VirtualNetwork  # type: ignore
    from ._models import VirtualNetworkConnectionGatewayReference  # type: ignore
    from ._models import VirtualNetworkGateway  # type: ignore
    from ._models import VirtualNetworkGatewayConnection  # type: ignore
    from ._models import VirtualNetworkGatewayConnectionListEntity  # type: ignore
    from ._models import VirtualNetworkGatewayConnectionListResult  # type: ignore
    from ._models import VirtualNetworkGatewayIPConfiguration  # type: ignore
    from ._models import VirtualNetworkGatewayListConnectionsResult  # type: ignore
    from ._models import VirtualNetworkGatewayListResult  # type: ignore
    from ._models import VirtualNetworkGatewaySku  # type: ignore
    from ._models import VirtualNetworkListResult  # type: ignore
    from ._models import VirtualNetworkListUsageResult  # type: ignore
    from ._models import VirtualNetworkPeering  # type: ignore
    from ._models import VirtualNetworkPeeringListResult  # type: ignore
    from ._models import VirtualNetworkUsage  # type: ignore
    from ._models import VirtualNetworkUsageName  # type: ignore
    from ._models import VpnClientConfiguration  # type: ignore
    from ._models import VpnClientParameters  # type: ignore
    from ._models import VpnClientRevokedCertificate  # type: ignore
    from ._models import VpnClientRootCertificate  # type: ignore

from ._network_management_client_enums import (
    Access,
    ApplicationGatewayBackendHealthServerHealth,
    ApplicationGatewayCookieBasedAffinity,
    ApplicationGatewayFirewallMode,
    ApplicationGatewayOperationalState,
    ApplicationGatewayProtocol,
    ApplicationGatewayRedirectType,
    ApplicationGatewayRequestRoutingRuleType,
    ApplicationGatewaySkuName,
    ApplicationGatewaySslCipherSuite,
    ApplicationGatewaySslPolicyName,
    ApplicationGatewaySslPolicyType,
    ApplicationGatewaySslProtocol,
    ApplicationGatewayTier,
    AssociationType,
    AuthenticationMethod,
    AuthorizationUseStatus,
    BgpPeerState,
    ConnectionStatus,
    DhGroup,
    Direction,
    EffectiveRouteSource,
    EffectiveRouteState,
    EffectiveSecurityRuleProtocol,
    ExpressRouteCircuitPeeringAdvertisedPublicPrefixState,
    ExpressRouteCircuitPeeringState,
    ExpressRouteCircuitPeeringType,
    ExpressRouteCircuitSkuFamily,
    ExpressRouteCircuitSkuTier,
    IPAllocationMethod,
    IPVersion,
    IkeEncryption,
    IkeIntegrity,
    IpsecEncryption,
    IpsecIntegrity,
    IssueType,
    LoadBalancerSkuName,
    LoadDistribution,
    NetworkOperationStatus,
    NextHopType,
    Origin,
    PcError,
    PcProtocol,
    PcStatus,
    PfsGroup,
    ProbeProtocol,
    ProcessorArchitecture,
    Protocol,
    ProvisioningState,
    PublicIPAddressSkuName,
    RouteFilterRuleType,
    RouteNextHopType,
    SecurityRuleAccess,
    SecurityRuleDirection,
    SecurityRuleProtocol,
    ServiceProviderProvisioningState,
    Severity,
    TransportProtocol,
    UsageUnit,
    VirtualNetworkGatewayConnectionStatus,
    VirtualNetworkGatewayConnectionType,
    VirtualNetworkGatewaySkuName,
    VirtualNetworkGatewaySkuTier,
    VirtualNetworkGatewayType,
    VirtualNetworkPeeringState,
    VpnClientProtocol,
    VpnType,
)

__all__ = [
    "AddressSpace",
    "ApplicationGateway",
    "ApplicationGatewayAuthenticationCertificate",
    "ApplicationGatewayAvailableSslOptions",
    "ApplicationGatewayAvailableSslPredefinedPolicies",
    "ApplicationGatewayAvailableWafRuleSetsResult",
    "ApplicationGatewayBackendAddress",
    "ApplicationGatewayBackendAddressPool",
    "ApplicationGatewayBackendHealth",
    "ApplicationGatewayBackendHealthHttpSettings",
    "ApplicationGatewayBackendHealthPool",
    "ApplicationGatewayBackendHealthServer",
    "ApplicationGatewayBackendHttpSettings",
    "ApplicationGatewayConnectionDraining",
    "ApplicationGatewayFirewallDisabledRuleGroup",
    "ApplicationGatewayFirewallRule",
    "ApplicationGatewayFirewallRuleGroup",
    "ApplicationGatewayFirewallRuleSet",
    "ApplicationGatewayFrontendIPConfiguration",
    "ApplicationGatewayFrontendPort",
    "ApplicationGatewayHttpListener",
    "ApplicationGatewayIPConfiguration",
    "ApplicationGatewayListResult",
    "ApplicationGatewayPathRule",
    "ApplicationGatewayProbe",
    "ApplicationGatewayProbeHealthResponseMatch",
    "ApplicationGatewayRedirectConfiguration",
    "ApplicationGatewayRequestRoutingRule",
    "ApplicationGatewaySku",
    "ApplicationGatewaySslCertificate",
    "ApplicationGatewaySslPolicy",
    "ApplicationGatewaySslPredefinedPolicy",
    "ApplicationGatewayUrlPathMap",
    "ApplicationGatewayWebApplicationFirewallConfiguration",
    "AuthorizationListResult",
    "AzureAsyncOperationResult",
    "BGPCommunity",
    "BackendAddressPool",
    "BgpPeerStatus",
    "BgpPeerStatusListResult",
    "BgpServiceCommunity",
    "BgpServiceCommunityListResult",
    "BgpSettings",
    "ConnectionResetSharedKey",
    "ConnectionSharedKey",
    "ConnectivityDestination",
    "ConnectivityHop",
    "ConnectivityInformation",
    "ConnectivityIssue",
    "ConnectivityParameters",
    "ConnectivitySource",
    "DhcpOptions",
    "DnsNameAvailabilityResult",
    "EffectiveNetworkSecurityGroup",
    "EffectiveNetworkSecurityGroupAssociation",
    "EffectiveNetworkSecurityGroupListResult",
    "EffectiveNetworkSecurityRule",
    "EffectiveRoute",
    "EffectiveRouteListResult",
    "EndpointServiceResult",
    "EndpointServicesListResult",
    "Error",
    "ErrorDetails",
    "ExpressRouteCircuit",
    "ExpressRouteCircuitArpTable",
    "ExpressRouteCircuitAuthorization",
    "ExpressRouteCircuitListResult",
    "ExpressRouteCircuitPeering",
    "ExpressRouteCircuitPeeringConfig",
    "ExpressRouteCircuitPeeringListResult",
    "ExpressRouteCircuitRoutesTable",
    "ExpressRouteCircuitRoutesTableSummary",
    "ExpressRouteCircuitServiceProviderProperties",
    "ExpressRouteCircuitSku",
    "ExpressRouteCircuitStats",
    "ExpressRouteCircuitsArpTableListResult",
    "ExpressRouteCircuitsRoutesTableListResult",
    "ExpressRouteCircuitsRoutesTableSummaryListResult",
    "ExpressRouteServiceProvider",
    "ExpressRouteServiceProviderBandwidthsOffered",
    "ExpressRouteServiceProviderListResult",
    "FlowLogInformation",
    "FlowLogStatusParameters",
    "FrontendIPConfiguration",
    "GatewayRoute",
    "GatewayRouteListResult",
    "IPAddressAvailabilityResult",
    "IPConfiguration",
    "InboundNatPool",
    "InboundNatRule",
    "InboundNatRuleListResult",
    "IpsecPolicy",
    "Ipv6ExpressRouteCircuitPeeringConfig",
    "LoadBalancer",
    "LoadBalancerBackendAddressPoolListResult",
    "LoadBalancerFrontendIPConfigurationListResult",
    "LoadBalancerListResult",
    "LoadBalancerLoadBalancingRuleListResult",
    "LoadBalancerProbeListResult",
    "LoadBalancerSku",
    "LoadBalancingRule",
    "LocalNetworkGateway",
    "LocalNetworkGatewayListResult",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "NetworkInterfaceDnsSettings",
    "NetworkInterfaceIPConfiguration",
    "NetworkInterfaceIPConfigurationListResult",
    "NetworkInterfaceListResult",
    "NetworkInterfaceLoadBalancerListResult",
    "NetworkSecurityGroup",
    "NetworkSecurityGroupListResult",
    "NetworkWatcher",
    "NetworkWatcherListResult",
    "NextHopParameters",
    "NextHopResult",
    "OutboundNatRule",
    "PacketCapture",
    "PacketCaptureFilter",
    "PacketCaptureListResult",
    "PacketCaptureParameters",
    "PacketCaptureQueryStatusResult",
    "PacketCaptureResult",
    "PacketCaptureResultProperties",
    "PacketCaptureStorageLocation",
    "PatchRouteFilter",
    "PatchRouteFilterRule",
    "Probe",
    "PublicIPAddress",
    "PublicIPAddressDnsSettings",
    "PublicIPAddressListResult",
    "PublicIPAddressSku",
    "QueryTroubleshootingParameters",
    "Resource",
    "ResourceNavigationLink",
    "RetentionPolicyParameters",
    "Route",
    "RouteFilter",
    "RouteFilterListResult",
    "RouteFilterRule",
    "RouteFilterRuleListResult",
    "RouteListResult",
    "RouteTable",
    "RouteTableListResult",
    "SecurityGroupNetworkInterface",
    "SecurityGroupViewParameters",
    "SecurityGroupViewResult",
    "SecurityRule",
    "SecurityRuleAssociations",
    "SecurityRuleListResult",
    "ServiceEndpointPropertiesFormat",
    "SubResource",
    "Subnet",
    "SubnetAssociation",
    "SubnetListResult",
    "Topology",
    "TopologyAssociation",
    "TopologyParameters",
    "TopologyResource",
    "TroubleshootingDetails",
    "TroubleshootingParameters",
    "TroubleshootingRecommendedActions",
    "TroubleshootingResult",
    "TunnelConnectionHealth",
    "Usage",
    "UsageName",
    "UsagesListResult",
    "VerificationIPFlowParameters",
    "VerificationIPFlowResult",
    "VirtualNetwork",
    "VirtualNetworkConnectionGatewayReference",
    "VirtualNetworkGateway",
    "VirtualNetworkGatewayConnection",
    "VirtualNetworkGatewayConnectionListEntity",
    "VirtualNetworkGatewayConnectionListResult",
    "VirtualNetworkGatewayIPConfiguration",
    "VirtualNetworkGatewayListConnectionsResult",
    "VirtualNetworkGatewayListResult",
    "VirtualNetworkGatewaySku",
    "VirtualNetworkListResult",
    "VirtualNetworkListUsageResult",
    "VirtualNetworkPeering",
    "VirtualNetworkPeeringListResult",
    "VirtualNetworkUsage",
    "VirtualNetworkUsageName",
    "VpnClientConfiguration",
    "VpnClientParameters",
    "VpnClientRevokedCertificate",
    "VpnClientRootCertificate",
    "Access",
    "ApplicationGatewayBackendHealthServerHealth",
    "ApplicationGatewayCookieBasedAffinity",
    "ApplicationGatewayFirewallMode",
    "ApplicationGatewayOperationalState",
    "ApplicationGatewayProtocol",
    "ApplicationGatewayRedirectType",
    "ApplicationGatewayRequestRoutingRuleType",
    "ApplicationGatewaySkuName",
    "ApplicationGatewaySslCipherSuite",
    "ApplicationGatewaySslPolicyName",
    "ApplicationGatewaySslPolicyType",
    "ApplicationGatewaySslProtocol",
    "ApplicationGatewayTier",
    "AssociationType",
    "AuthenticationMethod",
    "AuthorizationUseStatus",
    "BgpPeerState",
    "ConnectionStatus",
    "DhGroup",
    "Direction",
    "EffectiveRouteSource",
    "EffectiveRouteState",
    "EffectiveSecurityRuleProtocol",
    "ExpressRouteCircuitPeeringAdvertisedPublicPrefixState",
    "ExpressRouteCircuitPeeringState",
    "ExpressRouteCircuitPeeringType",
    "ExpressRouteCircuitSkuFamily",
    "ExpressRouteCircuitSkuTier",
    "IPAllocationMethod",
    "IPVersion",
    "IkeEncryption",
    "IkeIntegrity",
    "IpsecEncryption",
    "IpsecIntegrity",
    "IssueType",
    "LoadBalancerSkuName",
    "LoadDistribution",
    "NetworkOperationStatus",
    "NextHopType",
    "Origin",
    "PcError",
    "PcProtocol",
    "PcStatus",
    "PfsGroup",
    "ProbeProtocol",
    "ProcessorArchitecture",
    "Protocol",
    "ProvisioningState",
    "PublicIPAddressSkuName",
    "RouteFilterRuleType",
    "RouteNextHopType",
    "SecurityRuleAccess",
    "SecurityRuleDirection",
    "SecurityRuleProtocol",
    "ServiceProviderProvisioningState",
    "Severity",
    "TransportProtocol",
    "UsageUnit",
    "VirtualNetworkGatewayConnectionStatus",
    "VirtualNetworkGatewayConnectionType",
    "VirtualNetworkGatewaySkuName",
    "VirtualNetworkGatewaySkuTier",
    "VirtualNetworkGatewayType",
    "VirtualNetworkPeeringState",
    "VpnClientProtocol",
    "VpnType",
]
