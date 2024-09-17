# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: master
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1Endpoint(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'addresses': 'list[str]',
        'conditions': 'V1EndpointConditions',
        'deprecated_topology': 'dict(str, str)',
        'hints': 'V1EndpointHints',
        'hostname': 'str',
        'node_name': 'str',
        'target_ref': 'V1ObjectReference',
        'zone': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'conditions': 'conditions',
        'deprecated_topology': 'deprecatedTopology',
        'hints': 'hints',
        'hostname': 'hostname',
        'node_name': 'nodeName',
        'target_ref': 'targetRef',
        'zone': 'zone'
    }

    def __init__(self, addresses=None, conditions=None, deprecated_topology=None, hints=None, hostname=None, node_name=None, target_ref=None, zone=None, local_vars_configuration=None):  # noqa: E501
        """V1Endpoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._conditions = None
        self._deprecated_topology = None
        self._hints = None
        self._hostname = None
        self._node_name = None
        self._target_ref = None
        self._zone = None
        self.discriminator = None

        self.addresses = addresses
        if conditions is not None:
            self.conditions = conditions
        if deprecated_topology is not None:
            self.deprecated_topology = deprecated_topology
        if hints is not None:
            self.hints = hints
        if hostname is not None:
            self.hostname = hostname
        if node_name is not None:
            self.node_name = node_name
        if target_ref is not None:
            self.target_ref = target_ref
        if zone is not None:
            self.zone = zone

    @property
    def addresses(self):
        """Gets the addresses of this V1Endpoint.  # noqa: E501

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267  # noqa: E501

        :return: The addresses of this V1Endpoint.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this V1Endpoint.

        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267  # noqa: E501

        :param addresses: The addresses of this V1Endpoint.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and addresses is None:  # noqa: E501
            raise ValueError("Invalid value for `addresses`, must not be `None`")  # noqa: E501

        self._addresses = addresses

    @property
    def conditions(self):
        """Gets the conditions of this V1Endpoint.  # noqa: E501


        :return: The conditions of this V1Endpoint.  # noqa: E501
        :rtype: V1EndpointConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1Endpoint.


        :param conditions: The conditions of this V1Endpoint.  # noqa: E501
        :type: V1EndpointConditions
        """

        self._conditions = conditions

    @property
    def deprecated_topology(self):
        """Gets the deprecated_topology of this V1Endpoint.  # noqa: E501

        deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.  # noqa: E501

        :return: The deprecated_topology of this V1Endpoint.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._deprecated_topology

    @deprecated_topology.setter
    def deprecated_topology(self, deprecated_topology):
        """Sets the deprecated_topology of this V1Endpoint.

        deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.  # noqa: E501

        :param deprecated_topology: The deprecated_topology of this V1Endpoint.  # noqa: E501
        :type: dict(str, str)
        """

        self._deprecated_topology = deprecated_topology

    @property
    def hints(self):
        """Gets the hints of this V1Endpoint.  # noqa: E501


        :return: The hints of this V1Endpoint.  # noqa: E501
        :rtype: V1EndpointHints
        """
        return self._hints

    @hints.setter
    def hints(self, hints):
        """Sets the hints of this V1Endpoint.


        :param hints: The hints of this V1Endpoint.  # noqa: E501
        :type: V1EndpointHints
        """

        self._hints = hints

    @property
    def hostname(self):
        """Gets the hostname of this V1Endpoint.  # noqa: E501

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.  # noqa: E501

        :return: The hostname of this V1Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this V1Endpoint.

        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.  # noqa: E501

        :param hostname: The hostname of this V1Endpoint.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def node_name(self):
        """Gets the node_name of this V1Endpoint.  # noqa: E501

        nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.  # noqa: E501

        :return: The node_name of this V1Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this V1Endpoint.

        nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.  # noqa: E501

        :param node_name: The node_name of this V1Endpoint.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

    @property
    def target_ref(self):
        """Gets the target_ref of this V1Endpoint.  # noqa: E501


        :return: The target_ref of this V1Endpoint.  # noqa: E501
        :rtype: V1ObjectReference
        """
        return self._target_ref

    @target_ref.setter
    def target_ref(self, target_ref):
        """Sets the target_ref of this V1Endpoint.


        :param target_ref: The target_ref of this V1Endpoint.  # noqa: E501
        :type: V1ObjectReference
        """

        self._target_ref = target_ref

    @property
    def zone(self):
        """Gets the zone of this V1Endpoint.  # noqa: E501

        zone is the name of the Zone this endpoint exists in.  # noqa: E501

        :return: The zone of this V1Endpoint.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this V1Endpoint.

        zone is the name of the Zone this endpoint exists in.  # noqa: E501

        :param zone: The zone of this V1Endpoint.  # noqa: E501
        :type: str
        """

        self._zone = zone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Endpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Endpoint):
            return True

        return self.to_dict() != other.to_dict()