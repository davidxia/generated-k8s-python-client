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


class V1alpha1LeaseCandidateSpec(object):
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
        'binary_version': 'str',
        'emulation_version': 'str',
        'lease_name': 'str',
        'ping_time': 'datetime',
        'preferred_strategies': 'list[str]',
        'renew_time': 'datetime'
    }

    attribute_map = {
        'binary_version': 'binaryVersion',
        'emulation_version': 'emulationVersion',
        'lease_name': 'leaseName',
        'ping_time': 'pingTime',
        'preferred_strategies': 'preferredStrategies',
        'renew_time': 'renewTime'
    }

    def __init__(self, binary_version=None, emulation_version=None, lease_name=None, ping_time=None, preferred_strategies=None, renew_time=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1LeaseCandidateSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._binary_version = None
        self._emulation_version = None
        self._lease_name = None
        self._ping_time = None
        self._preferred_strategies = None
        self._renew_time = None
        self.discriminator = None

        if binary_version is not None:
            self.binary_version = binary_version
        if emulation_version is not None:
            self.emulation_version = emulation_version
        self.lease_name = lease_name
        if ping_time is not None:
            self.ping_time = ping_time
        self.preferred_strategies = preferred_strategies
        if renew_time is not None:
            self.renew_time = renew_time

    @property
    def binary_version(self):
        """Gets the binary_version of this V1alpha1LeaseCandidateSpec.  # noqa: E501

        BinaryVersion is the binary version. It must be in a semver format without leading `v`. This field is required when strategy is \"OldestEmulationVersion\"  # noqa: E501

        :return: The binary_version of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :rtype: str
        """
        return self._binary_version

    @binary_version.setter
    def binary_version(self, binary_version):
        """Sets the binary_version of this V1alpha1LeaseCandidateSpec.

        BinaryVersion is the binary version. It must be in a semver format without leading `v`. This field is required when strategy is \"OldestEmulationVersion\"  # noqa: E501

        :param binary_version: The binary_version of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :type: str
        """

        self._binary_version = binary_version

    @property
    def emulation_version(self):
        """Gets the emulation_version of this V1alpha1LeaseCandidateSpec.  # noqa: E501

        EmulationVersion is the emulation version. It must be in a semver format without leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is \"OldestEmulationVersion\"  # noqa: E501

        :return: The emulation_version of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :rtype: str
        """
        return self._emulation_version

    @emulation_version.setter
    def emulation_version(self, emulation_version):
        """Sets the emulation_version of this V1alpha1LeaseCandidateSpec.

        EmulationVersion is the emulation version. It must be in a semver format without leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is \"OldestEmulationVersion\"  # noqa: E501

        :param emulation_version: The emulation_version of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :type: str
        """

        self._emulation_version = emulation_version

    @property
    def lease_name(self):
        """Gets the lease_name of this V1alpha1LeaseCandidateSpec.  # noqa: E501

        LeaseName is the name of the lease for which this candidate is contending. This field is immutable.  # noqa: E501

        :return: The lease_name of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :rtype: str
        """
        return self._lease_name

    @lease_name.setter
    def lease_name(self, lease_name):
        """Sets the lease_name of this V1alpha1LeaseCandidateSpec.

        LeaseName is the name of the lease for which this candidate is contending. This field is immutable.  # noqa: E501

        :param lease_name: The lease_name of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and lease_name is None:  # noqa: E501
            raise ValueError("Invalid value for `lease_name`, must not be `None`")  # noqa: E501

        self._lease_name = lease_name

    @property
    def ping_time(self):
        """Gets the ping_time of this V1alpha1LeaseCandidateSpec.  # noqa: E501

        PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime.  # noqa: E501

        :return: The ping_time of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._ping_time

    @ping_time.setter
    def ping_time(self, ping_time):
        """Sets the ping_time of this V1alpha1LeaseCandidateSpec.

        PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime.  # noqa: E501

        :param ping_time: The ping_time of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :type: datetime
        """

        self._ping_time = ping_time

    @property
    def preferred_strategies(self):
        """Gets the preferred_strategies of this V1alpha1LeaseCandidateSpec.  # noqa: E501

        PreferredStrategies indicates the list of strategies for picking the leader for coordinated leader election. The list is ordered, and the first strategy supersedes all other strategies. The list is used by coordinated leader election to make a decision about the final election strategy. This follows as - If all clients have strategy X as the first element in this list, strategy X will be used. - If a candidate has strategy [X] and another candidate has strategy [Y, X], Y supersedes X and strategy Y   will be used. - If a candidate has strategy [X, Y] and another candidate has strategy [Y, X], this is a user error and leader   election will not operate the Lease until resolved. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled.  # noqa: E501

        :return: The preferred_strategies of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._preferred_strategies

    @preferred_strategies.setter
    def preferred_strategies(self, preferred_strategies):
        """Sets the preferred_strategies of this V1alpha1LeaseCandidateSpec.

        PreferredStrategies indicates the list of strategies for picking the leader for coordinated leader election. The list is ordered, and the first strategy supersedes all other strategies. The list is used by coordinated leader election to make a decision about the final election strategy. This follows as - If all clients have strategy X as the first element in this list, strategy X will be used. - If a candidate has strategy [X] and another candidate has strategy [Y, X], Y supersedes X and strategy Y   will be used. - If a candidate has strategy [X, Y] and another candidate has strategy [Y, X], this is a user error and leader   election will not operate the Lease until resolved. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled.  # noqa: E501

        :param preferred_strategies: The preferred_strategies of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and preferred_strategies is None:  # noqa: E501
            raise ValueError("Invalid value for `preferred_strategies`, must not be `None`")  # noqa: E501

        self._preferred_strategies = preferred_strategies

    @property
    def renew_time(self):
        """Gets the renew_time of this V1alpha1LeaseCandidateSpec.  # noqa: E501

        RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates.  # noqa: E501

        :return: The renew_time of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._renew_time

    @renew_time.setter
    def renew_time(self, renew_time):
        """Sets the renew_time of this V1alpha1LeaseCandidateSpec.

        RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates.  # noqa: E501

        :param renew_time: The renew_time of this V1alpha1LeaseCandidateSpec.  # noqa: E501
        :type: datetime
        """

        self._renew_time = renew_time

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
        if not isinstance(other, V1alpha1LeaseCandidateSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1LeaseCandidateSpec):
            return True

        return self.to_dict() != other.to_dict()
