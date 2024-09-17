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


class V2HorizontalPodAutoscalerBehavior(object):
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
        'scale_down': 'V2HPAScalingRules',
        'scale_up': 'V2HPAScalingRules'
    }

    attribute_map = {
        'scale_down': 'scaleDown',
        'scale_up': 'scaleUp'
    }

    def __init__(self, scale_down=None, scale_up=None, local_vars_configuration=None):  # noqa: E501
        """V2HorizontalPodAutoscalerBehavior - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scale_down = None
        self._scale_up = None
        self.discriminator = None

        if scale_down is not None:
            self.scale_down = scale_down
        if scale_up is not None:
            self.scale_up = scale_up

    @property
    def scale_down(self):
        """Gets the scale_down of this V2HorizontalPodAutoscalerBehavior.  # noqa: E501


        :return: The scale_down of this V2HorizontalPodAutoscalerBehavior.  # noqa: E501
        :rtype: V2HPAScalingRules
        """
        return self._scale_down

    @scale_down.setter
    def scale_down(self, scale_down):
        """Sets the scale_down of this V2HorizontalPodAutoscalerBehavior.


        :param scale_down: The scale_down of this V2HorizontalPodAutoscalerBehavior.  # noqa: E501
        :type: V2HPAScalingRules
        """

        self._scale_down = scale_down

    @property
    def scale_up(self):
        """Gets the scale_up of this V2HorizontalPodAutoscalerBehavior.  # noqa: E501


        :return: The scale_up of this V2HorizontalPodAutoscalerBehavior.  # noqa: E501
        :rtype: V2HPAScalingRules
        """
        return self._scale_up

    @scale_up.setter
    def scale_up(self, scale_up):
        """Sets the scale_up of this V2HorizontalPodAutoscalerBehavior.


        :param scale_up: The scale_up of this V2HorizontalPodAutoscalerBehavior.  # noqa: E501
        :type: V2HPAScalingRules
        """

        self._scale_up = scale_up

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
        if not isinstance(other, V2HorizontalPodAutoscalerBehavior):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2HorizontalPodAutoscalerBehavior):
            return True

        return self.to_dict() != other.to_dict()
