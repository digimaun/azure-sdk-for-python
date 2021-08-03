# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass


class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Access(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Access to be allowed or denied."""

    ALLOW = "Allow"
    DENY = "Deny"


class ApplicationGatewayBackendHealthServerHealth(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Health of backend server."""

    UNKNOWN = "Unknown"
    UP = "Up"
    DOWN = "Down"
    PARTIAL = "Partial"
    DRAINING = "Draining"


class ApplicationGatewayCookieBasedAffinity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Cookie based affinity."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ApplicationGatewayCustomErrorStatusCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status code of the application gateway customer error."""

    HTTP_STATUS403 = "HttpStatus403"
    HTTP_STATUS502 = "HttpStatus502"


class ApplicationGatewayFirewallMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Web application firewall mode."""

    DETECTION = "Detection"
    PREVENTION = "Prevention"


class ApplicationGatewayOperationalState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Operational state of the application gateway resource."""

    STOPPED = "Stopped"
    STARTING = "Starting"
    RUNNING = "Running"
    STOPPING = "Stopping"


class ApplicationGatewayProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Application Gateway protocol."""

    HTTP = "Http"
    HTTPS = "Https"


class ApplicationGatewayRedirectType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Redirect type enum."""

    PERMANENT = "Permanent"
    FOUND = "Found"
    SEE_OTHER = "SeeOther"
    TEMPORARY = "Temporary"


class ApplicationGatewayRequestRoutingRuleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Rule type."""

    BASIC = "Basic"
    PATH_BASED_ROUTING = "PathBasedRouting"


class ApplicationGatewaySkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of an application gateway SKU."""

    STANDARD_SMALL = "Standard_Small"
    STANDARD_MEDIUM = "Standard_Medium"
    STANDARD_LARGE = "Standard_Large"
    WAF_MEDIUM = "WAF_Medium"
    WAF_LARGE = "WAF_Large"
    STANDARD_V2 = "Standard_v2"
    WAF_V2 = "WAF_v2"


class ApplicationGatewaySslCipherSuite(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Ssl cipher suites enums."""

    TLS_ECDHE_RSA_WITH_AES256_CBC_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    TLS_ECDHE_RSA_WITH_AES128_CBC_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
    TLS_ECDHE_RSA_WITH_AES256_CBC_SHA = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"
    TLS_ECDHE_RSA_WITH_AES128_CBC_SHA = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"
    TLS_DHE_RSA_WITH_AES256_GCM_SHA384 = "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384"
    TLS_DHE_RSA_WITH_AES128_GCM_SHA256 = "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256"
    TLS_DHE_RSA_WITH_AES256_CBC_SHA = "TLS_DHE_RSA_WITH_AES_256_CBC_SHA"
    TLS_DHE_RSA_WITH_AES128_CBC_SHA = "TLS_DHE_RSA_WITH_AES_128_CBC_SHA"
    TLS_RSA_WITH_AES256_GCM_SHA384 = "TLS_RSA_WITH_AES_256_GCM_SHA384"
    TLS_RSA_WITH_AES128_GCM_SHA256 = "TLS_RSA_WITH_AES_128_GCM_SHA256"
    TLS_RSA_WITH_AES256_CBC_SHA256 = "TLS_RSA_WITH_AES_256_CBC_SHA256"
    TLS_RSA_WITH_AES128_CBC_SHA256 = "TLS_RSA_WITH_AES_128_CBC_SHA256"
    TLS_RSA_WITH_AES256_CBC_SHA = "TLS_RSA_WITH_AES_256_CBC_SHA"
    TLS_RSA_WITH_AES128_CBC_SHA = "TLS_RSA_WITH_AES_128_CBC_SHA"
    TLS_ECDHE_ECDSA_WITH_AES256_GCM_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
    TLS_ECDHE_ECDSA_WITH_AES128_GCM_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
    TLS_ECDHE_ECDSA_WITH_AES256_CBC_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384"
    TLS_ECDHE_ECDSA_WITH_AES128_CBC_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256"
    TLS_ECDHE_ECDSA_WITH_AES256_CBC_SHA = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA"
    TLS_ECDHE_ECDSA_WITH_AES128_CBC_SHA = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA"
    TLS_DHE_DSS_WITH_AES256_CBC_SHA256 = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256"
    TLS_DHE_DSS_WITH_AES128_CBC_SHA256 = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256"
    TLS_DHE_DSS_WITH_AES256_CBC_SHA = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA"
    TLS_DHE_DSS_WITH_AES128_CBC_SHA = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA"
    TLS_RSA_WITH3_DES_EDE_CBC_SHA = "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
    TLS_DHE_DSS_WITH3_DES_EDE_CBC_SHA = "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA"
    TLS_ECDHE_RSA_WITH_AES128_GCM_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
    TLS_ECDHE_RSA_WITH_AES256_GCM_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"


class ApplicationGatewaySslPolicyName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Ssl predefined policy name enums."""

    APP_GW_SSL_POLICY20150501 = "AppGwSslPolicy20150501"
    APP_GW_SSL_POLICY20170401 = "AppGwSslPolicy20170401"
    APP_GW_SSL_POLICY20170401_S = "AppGwSslPolicy20170401S"


class ApplicationGatewaySslPolicyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of Ssl Policy."""

    PREDEFINED = "Predefined"
    CUSTOM = "Custom"


class ApplicationGatewaySslProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Ssl protocol enums."""

    TL_SV1_0 = "TLSv1_0"
    TL_SV1_1 = "TLSv1_1"
    TL_SV1_2 = "TLSv1_2"


class ApplicationGatewayTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Tier of an application gateway."""

    STANDARD = "Standard"
    WAF = "WAF"
    STANDARD_V2 = "Standard_v2"
    WAF_V2 = "WAF_v2"


class AssociationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The association type of the child resource to the parent resource."""

    ASSOCIATED = "Associated"
    CONTAINS = "Contains"


class AuthenticationMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """VPN client authentication method."""

    EAPTLS = "EAPTLS"
    EAPMSCHA_PV2 = "EAPMSCHAPv2"


class AuthorizationUseStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The authorization use status."""

    AVAILABLE = "Available"
    IN_USE = "InUse"


class AzureFirewallApplicationRuleProtocolType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol type of a Application Rule resource."""

    HTTP = "Http"
    HTTPS = "Https"
    MSSQL = "Mssql"


class AzureFirewallNatRCActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The action type of a NAT rule collection."""

    SNAT = "Snat"
    DNAT = "Dnat"


class AzureFirewallNetworkRuleProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol of a Network Rule resource."""

    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"
    ICMP = "ICMP"


class AzureFirewallRCActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The action type of a rule collection."""

    ALLOW = "Allow"
    DENY = "Deny"


class AzureFirewallSkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of an Azure Firewall SKU."""

    AZFW_VNET = "AZFW_VNet"
    AZFW_HUB = "AZFW_Hub"


class AzureFirewallSkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Tier of an Azure Firewall."""

    STANDARD = "Standard"


class AzureFirewallThreatIntelMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operation mode for Threat Intel."""

    ALERT = "Alert"
    DENY = "Deny"
    OFF = "Off"


class BgpPeerState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The BGP peer state."""

    UNKNOWN = "Unknown"
    STOPPED = "Stopped"
    IDLE = "Idle"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"


class CircuitConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Express Route Circuit connection state."""

    CONNECTED = "Connected"
    CONNECTING = "Connecting"
    DISCONNECTED = "Disconnected"


class ConnectionMonitorSourceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of connection monitor source."""

    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class ConnectionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The connection state."""

    REACHABLE = "Reachable"
    UNREACHABLE = "Unreachable"
    UNKNOWN = "Unknown"


class ConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The connection status."""

    UNKNOWN = "Unknown"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    DEGRADED = "Degraded"


class DdosCustomPolicyProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol for which the DDoS protection policy is being customized."""

    TCP = "Tcp"
    UDP = "Udp"
    SYN = "Syn"


class DdosCustomPolicyTriggerSensitivityOverride(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The customized DDoS protection trigger rate sensitivity degrees. High: Trigger rate set with
    most sensitivity w.r.t. normal traffic. Default: Trigger rate set with moderate sensitivity
    w.r.t. normal traffic. Low: Trigger rate set with less sensitivity w.r.t. normal traffic.
    Relaxed: Trigger rate set with least sensitivity w.r.t. normal traffic.
    """

    RELAXED = "Relaxed"
    LOW = "Low"
    DEFAULT = "Default"
    HIGH = "High"


class DdosSettingsProtectionCoverage(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The DDoS protection policy customizability of the public IP. Only standard coverage will have
    the ability to be customized.
    """

    BASIC = "Basic"
    STANDARD = "Standard"


class DhGroup(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The DH Groups used in IKE Phase 1 for initial SA."""

    NONE = "None"
    DH_GROUP1 = "DHGroup1"
    DH_GROUP2 = "DHGroup2"
    DH_GROUP14 = "DHGroup14"
    DH_GROUP2048 = "DHGroup2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    DH_GROUP24 = "DHGroup24"


class Direction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The direction of the traffic."""

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class EffectiveRouteSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Who created the route."""

    UNKNOWN = "Unknown"
    USER = "User"
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    DEFAULT = "Default"


class EffectiveRouteState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The value of effective route."""

    ACTIVE = "Active"
    INVALID = "Invalid"


class EffectiveSecurityRuleProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The network protocol this rule applies to."""

    TCP = "Tcp"
    UDP = "Udp"
    ALL = "All"


class EvaluationState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Connectivity analysis evaluation state."""

    NOT_STARTED = "NotStarted"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"


class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The advertised public prefix state of the Peering resource."""

    NOT_CONFIGURED = "NotConfigured"
    CONFIGURING = "Configuring"
    CONFIGURED = "Configured"
    VALIDATION_NEEDED = "ValidationNeeded"


class ExpressRouteCircuitPeeringState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of peering."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRouteCircuitSkuFamily(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The family of the SKU."""

    UNLIMITED_DATA = "UnlimitedData"
    METERED_DATA = "MeteredData"


class ExpressRouteCircuitSkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The tier of the SKU."""

    STANDARD = "Standard"
    PREMIUM = "Premium"
    BASIC = "Basic"
    LOCAL = "Local"


class ExpressRouteLinkAdminState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Administrative state of the physical port."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExpressRouteLinkConnectorType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Physical fiber port type."""

    LC = "LC"
    SC = "SC"


class ExpressRouteLinkMacSecCipher(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Mac security cipher."""

    GCM_AES128 = "gcm-aes-128"
    GCM_AES256 = "gcm-aes-256"


class ExpressRoutePeeringState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The state of peering."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRoutePeeringType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The peering type."""

    AZURE_PUBLIC_PEERING = "AzurePublicPeering"
    AZURE_PRIVATE_PEERING = "AzurePrivatePeering"
    MICROSOFT_PEERING = "MicrosoftPeering"


class ExpressRoutePortsEncapsulation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Encapsulation method on physical ports."""

    DOT1_Q = "Dot1Q"
    QIN_Q = "QinQ"


class FirewallPolicyFilterRuleActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The action type of a rule."""

    ALLOW = "Allow"
    DENY = "Deny"


class FirewallPolicyNatRuleActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The action type of a rule."""

    DNAT = "DNAT"


class FirewallPolicyRuleConditionApplicationProtocolType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The application protocol type of a Rule condition."""

    HTTP = "Http"
    HTTPS = "Https"


class FirewallPolicyRuleConditionNetworkProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Network protocol of a Rule condition."""

    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"
    ICMP = "ICMP"


class FirewallPolicyRuleConditionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Rule Condition Type."""

    APPLICATION_RULE_CONDITION = "ApplicationRuleCondition"
    NETWORK_RULE_CONDITION = "NetworkRuleCondition"


class FirewallPolicyRuleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the rule."""

    FIREWALL_POLICY_NAT_RULE = "FirewallPolicyNatRule"
    FIREWALL_POLICY_FILTER_RULE = "FirewallPolicyFilterRule"


class FlowLogFormatType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The file type of flow log."""

    JSON = "JSON"


class HTTPMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """HTTP method."""

    GET = "Get"


class HubVirtualNetworkConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the VirtualHub to vnet connection."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class IkeEncryption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The IKE encryption algorithm (IKE phase 2)."""

    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IkeIntegrity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The IKE integrity algorithm (IKE phase 2)."""

    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IPAllocationMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """IP address allocation method."""

    STATIC = "Static"
    DYNAMIC = "Dynamic"


class IpFlowProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Protocol to be verified on."""

    TCP = "TCP"
    UDP = "UDP"


class IpsecEncryption(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The IPSec encryption algorithm (IKE phase 1)."""

    NONE = "None"
    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class IpsecIntegrity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The IPSec integrity algorithm (IKE phase 1)."""

    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class IPVersion(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """IP address version."""

    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class IssueType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of issue."""

    UNKNOWN = "Unknown"
    AGENT_STOPPED = "AgentStopped"
    GUEST_FIREWALL = "GuestFirewall"
    DNS_RESOLUTION = "DnsResolution"
    SOCKET_BIND = "SocketBind"
    NETWORK_SECURITY_RULE = "NetworkSecurityRule"
    USER_DEFINED_ROUTE = "UserDefinedRoute"
    PORT_THROTTLED = "PortThrottled"
    PLATFORM = "Platform"


class LoadBalancerOutboundRuleProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol for the outbound rule in load balancer."""

    TCP = "Tcp"
    UDP = "Udp"
    ALL = "All"


class LoadBalancerSkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of a load balancer SKU."""

    BASIC = "Basic"
    STANDARD = "Standard"


class LoadDistribution(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The load distribution policy for this rule."""

    DEFAULT = "Default"
    SOURCE_IP = "SourceIP"
    SOURCE_IP_PROTOCOL = "SourceIPProtocol"


class ManagedRuleEnabledState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes the state of the managed rule. Defaults to Disabled if not specified."""

    DISABLED = "Disabled"


class NatGatewaySkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of Nat Gateway SKU."""

    STANDARD = "Standard"


class NetworkOperationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the Azure async operation."""

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class NextHopType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Next hop type."""

    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    HYPER_NET_GATEWAY = "HyperNetGateway"
    NONE = "None"


class OfficeTrafficCategory(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The office traffic category."""

    OPTIMIZE = "Optimize"
    OPTIMIZE_AND_ALLOW = "OptimizeAndAllow"
    ALL = "All"
    NONE = "None"


class Origin(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The origin of the issue."""

    LOCAL = "Local"
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class OwaspCrsExclusionEntryMatchVariable(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The variable to be excluded."""

    REQUEST_HEADER_NAMES = "RequestHeaderNames"
    REQUEST_COOKIE_NAMES = "RequestCookieNames"
    REQUEST_ARG_NAMES = "RequestArgNames"


class OwaspCrsExclusionEntrySelectorMatchOperator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """When matchVariable is a collection, operate on the selector to specify which elements in the
    collection this exclusion applies to.
    """

    EQUALS = "Equals"
    CONTAINS = "Contains"
    STARTS_WITH = "StartsWith"
    ENDS_WITH = "EndsWith"
    EQUALS_ANY = "EqualsAny"


class PcError(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    INTERNAL_ERROR = "InternalError"
    AGENT_STOPPED = "AgentStopped"
    CAPTURE_FAILED = "CaptureFailed"
    LOCAL_FILE_FAILED = "LocalFileFailed"
    STORAGE_FAILED = "StorageFailed"


class PcProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Protocol to be filtered on."""

    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"


class PcStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the packet capture session."""

    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    STOPPED = "Stopped"
    ERROR = "Error"
    UNKNOWN = "Unknown"


class PfsGroup(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Pfs Groups used in IKE Phase 2 for new child SA."""

    NONE = "None"
    PFS1 = "PFS1"
    PFS2 = "PFS2"
    PFS2048 = "PFS2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    PFS24 = "PFS24"
    PFS14 = "PFS14"
    PFSMM = "PFSMM"


class ProbeProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The protocol of the end point. If 'Tcp' is specified, a received ACK is required for the probe
    to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI
    is required for the probe to be successful.
    """

    HTTP = "Http"
    TCP = "Tcp"
    HTTPS = "Https"


class ProcessorArchitecture(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """VPN client Processor Architecture."""

    AMD64 = "Amd64"
    X86 = "X86"


class Protocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Network protocol."""

    TCP = "Tcp"
    HTTP = "Http"
    HTTPS = "Https"
    ICMP = "Icmp"


class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PublicIPAddressSkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of a public IP address SKU."""

    BASIC = "Basic"
    STANDARD = "Standard"


class PublicIPPrefixSkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of a public IP prefix SKU."""

    STANDARD = "Standard"


class ResourceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes
    both an implicitly created identity and a set of user assigned identities. The type 'None' will
    remove any identities from the virtual machine.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class RouteFilterRuleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The rule type of the rule."""

    COMMUNITY = "Community"


class RouteNextHopType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of Azure hop the packet should be sent to."""

    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    NONE = "None"


class SecurityRuleAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether network traffic is allowed or denied."""

    ALLOW = "Allow"
    DENY = "Deny"


class SecurityRuleDirection(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The direction of the rule. The direction specifies if rule will be evaluated on incoming or
    outgoing traffic.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityRuleProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Network protocol this rule applies to."""

    TCP = "Tcp"
    UDP = "Udp"
    ICMP = "Icmp"
    ESP = "Esp"
    ASTERISK = "*"
    AH = "Ah"


class ServiceProviderProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The ServiceProviderProvisioningState state of the resource."""

    NOT_PROVISIONED = "NotProvisioned"
    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    DEPROVISIONING = "Deprovisioning"


class Severity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The severity of the issue."""

    ERROR = "Error"
    WARNING = "Warning"


class TransportProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The transport protocol for the endpoint."""

    UDP = "Udp"
    TCP = "Tcp"
    ALL = "All"


class TunnelConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the tunnel."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class UsageUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """An enum describing the unit of measurement."""

    COUNT = "Count"


class VerbosityLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Verbosity level."""

    NORMAL = "Normal"
    MINIMUM = "Minimum"
    FULL = "Full"


class VirtualNetworkGatewayConnectionProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gateway connection protocol."""

    IK_EV2 = "IKEv2"
    IK_EV1 = "IKEv1"


class VirtualNetworkGatewayConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Virtual Network Gateway connection status."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class VirtualNetworkGatewayConnectionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gateway connection type."""

    I_PSEC = "IPsec"
    VNET2_VNET = "Vnet2Vnet"
    EXPRESS_ROUTE = "ExpressRoute"
    VPN_CLIENT = "VPNClient"


class VirtualNetworkGatewaySkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gateway SKU name."""

    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"
    VPN_GW1 = "VpnGw1"
    VPN_GW2 = "VpnGw2"
    VPN_GW3 = "VpnGw3"
    VPN_GW4 = "VpnGw4"
    VPN_GW5 = "VpnGw5"
    VPN_GW1_AZ = "VpnGw1AZ"
    VPN_GW2_AZ = "VpnGw2AZ"
    VPN_GW3_AZ = "VpnGw3AZ"
    VPN_GW4_AZ = "VpnGw4AZ"
    VPN_GW5_AZ = "VpnGw5AZ"
    ER_GW1_AZ = "ErGw1AZ"
    ER_GW2_AZ = "ErGw2AZ"
    ER_GW3_AZ = "ErGw3AZ"


class VirtualNetworkGatewaySkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gateway SKU tier."""

    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"
    VPN_GW1 = "VpnGw1"
    VPN_GW2 = "VpnGw2"
    VPN_GW3 = "VpnGw3"
    VPN_GW4 = "VpnGw4"
    VPN_GW5 = "VpnGw5"
    VPN_GW1_AZ = "VpnGw1AZ"
    VPN_GW2_AZ = "VpnGw2AZ"
    VPN_GW3_AZ = "VpnGw3AZ"
    VPN_GW4_AZ = "VpnGw4AZ"
    VPN_GW5_AZ = "VpnGw5AZ"
    ER_GW1_AZ = "ErGw1AZ"
    ER_GW2_AZ = "ErGw2AZ"
    ER_GW3_AZ = "ErGw3AZ"


class VirtualNetworkGatewayType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of this virtual network gateway."""

    VPN = "Vpn"
    EXPRESS_ROUTE = "ExpressRoute"


class VirtualNetworkPeeringState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the virtual network peering."""

    INITIATED = "Initiated"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"


class VirtualWanSecurityProviderType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The virtual wan security provider type."""

    EXTERNAL = "External"
    NATIVE = "Native"


class VpnAuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """VPN authentication types enabled for the VpnServerConfiguration."""

    CERTIFICATE = "Certificate"
    RADIUS = "Radius"
    AAD = "AAD"


class VpnClientProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """VPN client protocol enabled for the virtual network gateway."""

    IKE_V2 = "IkeV2"
    SSTP = "SSTP"
    OPEN_VPN = "OpenVPN"


class VpnConnectionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the vpn connection."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class VpnGatewayGeneration(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN."""

    NONE = "None"
    GENERATION1 = "Generation1"
    GENERATION2 = "Generation2"


class VpnGatewayTunnelingProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """VPN protocol enabled for the VpnServerConfiguration."""

    IKE_V2 = "IkeV2"
    OPEN_VPN = "OpenVPN"


class VpnType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of this virtual network gateway."""

    POLICY_BASED = "PolicyBased"
    ROUTE_BASED = "RouteBased"


class WebApplicationFirewallAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of Actions."""

    ALLOW = "Allow"
    BLOCK = "Block"
    LOG = "Log"


class WebApplicationFirewallEnabledState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes if the policy is in enabled state or disabled state."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class WebApplicationFirewallMatchVariable(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Match Variable."""

    REMOTE_ADDR = "RemoteAddr"
    REQUEST_METHOD = "RequestMethod"
    QUERY_STRING = "QueryString"
    POST_ARGS = "PostArgs"
    REQUEST_URI = "RequestUri"
    REQUEST_HEADERS = "RequestHeaders"
    REQUEST_BODY = "RequestBody"
    REQUEST_COOKIES = "RequestCookies"


class WebApplicationFirewallMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes if it is in detection mode or prevention mode at policy level."""

    PREVENTION = "Prevention"
    DETECTION = "Detection"


class WebApplicationFirewallOperator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes operator to be matched."""

    IP_MATCH = "IPMatch"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    REGEX = "Regex"


class WebApplicationFirewallPolicyResourceState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Resource status of the policy."""

    CREATING = "Creating"
    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    DELETING = "Deleting"


class WebApplicationFirewallRuleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes type of rule."""

    MATCH_RULE = "MatchRule"
    INVALID = "Invalid"


class WebApplicationFirewallTransform(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes what transforms applied before matching."""

    LOWERCASE = "Lowercase"
    TRIM = "Trim"
    URL_DECODE = "UrlDecode"
    URL_ENCODE = "UrlEncode"
    REMOVE_NULLS = "RemoveNulls"
    HTML_ENTITY_DECODE = "HtmlEntityDecode"
