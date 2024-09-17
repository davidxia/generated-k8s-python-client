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


class V2HorizontalPodAutoscalerStatus(object):
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
        'conditions': 'list[V2HorizontalPodAutoscalerCondition]',
        'current_metrics': 'list[V2MetricStatus]',
        'current_replicas': 'int',
        'desired_replicas': 'int',
        'last_scale_time': 'datetime',
        'observed_generation': 'int'
    }

    attribute_map = {
        'conditions': 'conditions',
        'current_metrics': 'currentMetrics',
        'current_replicas': 'currentReplicas',
        'desired_replicas': 'desiredReplicas',
        'last_scale_time': 'lastScaleTime',
        'observed_generation': 'observedGeneration'
    }

    def __init__(self, conditions=None, current_metrics=None, current_replicas=None, desired_replicas=None, last_scale_time=None, observed_generation=None, local_vars_configuration=None):  # noqa: E501
        """V2HorizontalPodAutoscalerStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._current_metrics = None
        self._current_replicas = None
        self._desired_replicas = None
        self._last_scale_time = None
        self._observed_generation = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if current_metrics is not None:
            self.current_metrics = current_metrics
        if current_replicas is not None:
            self.current_replicas = current_replicas
        self.desired_replicas = desired_replicas
        if last_scale_time is not None:
            self.last_scale_time = last_scale_time
        if observed_generation is not None:
            self.observed_generation = observed_generation

    @property
    def conditions(self):
        """Gets the conditions of this V2HorizontalPodAutoscalerStatus.  # noqa: E501

        conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.  # noqa: E501

        :return: The conditions of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: list[V2HorizontalPodAutoscalerCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V2HorizontalPodAutoscalerStatus.

        conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.  # noqa: E501

        :param conditions: The conditions of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: list[V2HorizontalPodAutoscalerCondition]
        """

        self._conditions = conditions

    @property
    def current_metrics(self):
        """Gets the current_metrics of this V2HorizontalPodAutoscalerStatus.  # noqa: E501

        currentMetrics is the last read state of the metrics used by this autoscaler.  # noqa: E501

        :return: The current_metrics of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: list[V2MetricStatus]
        """
        return self._current_metrics

    @current_metrics.setter
    def current_metrics(self, current_metrics):
        """Sets the current_metrics of this V2HorizontalPodAutoscalerStatus.

        currentMetrics is the last read state of the metrics used by this autoscaler.  # noqa: E501

        :param current_metrics: The current_metrics of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: list[V2MetricStatus]
        """

        self._current_metrics = current_metrics

    @property
    def current_replicas(self):
        """Gets the current_replicas of this V2HorizontalPodAutoscalerStatus.  # noqa: E501

        currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.  # noqa: E501

        :return: The current_replicas of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """Sets the current_replicas of this V2HorizontalPodAutoscalerStatus.

        currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.  # noqa: E501

        :param current_replicas: The current_replicas of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: int
        """

        self._current_replicas = current_replicas

    @property
    def desired_replicas(self):
        """Gets the desired_replicas of this V2HorizontalPodAutoscalerStatus.  # noqa: E501

        desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.  # noqa: E501

        :return: The desired_replicas of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._desired_replicas

    @desired_replicas.setter
    def desired_replicas(self, desired_replicas):
        """Sets the desired_replicas of this V2HorizontalPodAutoscalerStatus.

        desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.  # noqa: E501

        :param desired_replicas: The desired_replicas of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and desired_replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `desired_replicas`, must not be `None`")  # noqa: E501

        self._desired_replicas = desired_replicas

    @property
    def last_scale_time(self):
        """Gets the last_scale_time of this V2HorizontalPodAutoscalerStatus.  # noqa: E501

        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.  # noqa: E501

        :return: The last_scale_time of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scale_time

    @last_scale_time.setter
    def last_scale_time(self, last_scale_time):
        """Sets the last_scale_time of this V2HorizontalPodAutoscalerStatus.

        lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.  # noqa: E501

        :param last_scale_time: The last_scale_time of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: datetime
        """

        self._last_scale_time = last_scale_time

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V2HorizontalPodAutoscalerStatus.  # noqa: E501

        observedGeneration is the most recent generation observed by this autoscaler.  # noqa: E501

        :return: The observed_generation of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V2HorizontalPodAutoscalerStatus.

        observedGeneration is the most recent generation observed by this autoscaler.  # noqa: E501

        :param observed_generation: The observed_generation of this V2HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

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
        if not isinstance(other, V2HorizontalPodAutoscalerStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2HorizontalPodAutoscalerStatus):
            return True

        return self.to_dict() != other.to_dict()
