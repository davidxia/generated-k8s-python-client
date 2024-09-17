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


class V1alpha3DeviceRequestAllocationResult(object):
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
        'device': 'str',
        'driver': 'str',
        'pool': 'str',
        'request': 'str'
    }

    attribute_map = {
        'device': 'device',
        'driver': 'driver',
        'pool': 'pool',
        'request': 'request'
    }

    def __init__(self, device=None, driver=None, pool=None, request=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha3DeviceRequestAllocationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device = None
        self._driver = None
        self._pool = None
        self._request = None
        self.discriminator = None

        self.device = device
        self.driver = driver
        self.pool = pool
        self.request = request

    @property
    def device(self):
        """Gets the device of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501

        Device references one device instance via its name in the driver's resource pool. It must be a DNS label.  # noqa: E501

        :return: The device of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this V1alpha3DeviceRequestAllocationResult.

        Device references one device instance via its name in the driver's resource pool. It must be a DNS label.  # noqa: E501

        :param device: The device of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def driver(self):
        """Gets the driver of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501

        Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.  # noqa: E501

        :return: The driver of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this V1alpha3DeviceRequestAllocationResult.

        Driver specifies the name of the DRA driver whose kubelet plugin should be invoked to process the allocation once the claim is needed on a node.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver.  # noqa: E501

        :param driver: The driver of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and driver is None:  # noqa: E501
            raise ValueError("Invalid value for `driver`, must not be `None`")  # noqa: E501

        self._driver = driver

    @property
    def pool(self):
        """Gets the pool of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501

        This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.  # noqa: E501

        :return: The pool of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this V1alpha3DeviceRequestAllocationResult.

        This name together with the driver name and the device name field identify which device was allocated (`<driver name>/<pool name>/<device name>`).  Must not be longer than 253 characters and may contain one or more DNS sub-domains separated by slashes.  # noqa: E501

        :param pool: The pool of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pool is None:  # noqa: E501
            raise ValueError("Invalid value for `pool`, must not be `None`")  # noqa: E501

        self._pool = pool

    @property
    def request(self):
        """Gets the request of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501

        Request is the name of the request in the claim which caused this device to be allocated. Multiple devices may have been allocated per request.  # noqa: E501

        :return: The request of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this V1alpha3DeviceRequestAllocationResult.

        Request is the name of the request in the claim which caused this device to be allocated. Multiple devices may have been allocated per request.  # noqa: E501

        :param request: The request of this V1alpha3DeviceRequestAllocationResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request is None:  # noqa: E501
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

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
        if not isinstance(other, V1alpha3DeviceRequestAllocationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha3DeviceRequestAllocationResult):
            return True

        return self.to_dict() != other.to_dict()
