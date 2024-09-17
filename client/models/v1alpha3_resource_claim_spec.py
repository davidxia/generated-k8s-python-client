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


class V1alpha3ResourceClaimSpec(object):
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
        'controller': 'str',
        'devices': 'V1alpha3DeviceClaim'
    }

    attribute_map = {
        'controller': 'controller',
        'devices': 'devices'
    }

    def __init__(self, controller=None, devices=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha3ResourceClaimSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._controller = None
        self._devices = None
        self.discriminator = None

        if controller is not None:
            self.controller = controller
        if devices is not None:
            self.devices = devices

    @property
    def controller(self):
        """Gets the controller of this V1alpha3ResourceClaimSpec.  # noqa: E501

        Controller is the name of the DRA driver that is meant to handle allocation of this claim. If empty, allocation is handled by the scheduler while scheduling a pod.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.  This is an alpha field and requires enabling the DRAControlPlaneController feature gate.  # noqa: E501

        :return: The controller of this V1alpha3ResourceClaimSpec.  # noqa: E501
        :rtype: str
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this V1alpha3ResourceClaimSpec.

        Controller is the name of the DRA driver that is meant to handle allocation of this claim. If empty, allocation is handled by the scheduler while scheduling a pod.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.  This is an alpha field and requires enabling the DRAControlPlaneController feature gate.  # noqa: E501

        :param controller: The controller of this V1alpha3ResourceClaimSpec.  # noqa: E501
        :type: str
        """

        self._controller = controller

    @property
    def devices(self):
        """Gets the devices of this V1alpha3ResourceClaimSpec.  # noqa: E501


        :return: The devices of this V1alpha3ResourceClaimSpec.  # noqa: E501
        :rtype: V1alpha3DeviceClaim
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this V1alpha3ResourceClaimSpec.


        :param devices: The devices of this V1alpha3ResourceClaimSpec.  # noqa: E501
        :type: V1alpha3DeviceClaim
        """

        self._devices = devices

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
        if not isinstance(other, V1alpha3ResourceClaimSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha3ResourceClaimSpec):
            return True

        return self.to_dict() != other.to_dict()