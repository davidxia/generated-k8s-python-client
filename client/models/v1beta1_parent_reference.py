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


class V1beta1ParentReference(object):
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
        'group': 'str',
        'name': 'str',
        'namespace': 'str',
        'resource': 'str'
    }

    attribute_map = {
        'group': 'group',
        'name': 'name',
        'namespace': 'namespace',
        'resource': 'resource'
    }

    def __init__(self, group=None, name=None, namespace=None, resource=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1ParentReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._name = None
        self._namespace = None
        self._resource = None
        self.discriminator = None

        if group is not None:
            self.group = group
        self.name = name
        if namespace is not None:
            self.namespace = namespace
        self.resource = resource

    @property
    def group(self):
        """Gets the group of this V1beta1ParentReference.  # noqa: E501

        Group is the group of the object being referenced.  # noqa: E501

        :return: The group of this V1beta1ParentReference.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1beta1ParentReference.

        Group is the group of the object being referenced.  # noqa: E501

        :param group: The group of this V1beta1ParentReference.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def name(self):
        """Gets the name of this V1beta1ParentReference.  # noqa: E501

        Name is the name of the object being referenced.  # noqa: E501

        :return: The name of this V1beta1ParentReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1ParentReference.

        Name is the name of the object being referenced.  # noqa: E501

        :param name: The name of this V1beta1ParentReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this V1beta1ParentReference.  # noqa: E501

        Namespace is the namespace of the object being referenced.  # noqa: E501

        :return: The namespace of this V1beta1ParentReference.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1beta1ParentReference.

        Namespace is the namespace of the object being referenced.  # noqa: E501

        :param namespace: The namespace of this V1beta1ParentReference.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def resource(self):
        """Gets the resource of this V1beta1ParentReference.  # noqa: E501

        Resource is the resource of the object being referenced.  # noqa: E501

        :return: The resource of this V1beta1ParentReference.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1beta1ParentReference.

        Resource is the resource of the object being referenced.  # noqa: E501

        :param resource: The resource of this V1beta1ParentReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

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
        if not isinstance(other, V1beta1ParentReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1ParentReference):
            return True

        return self.to_dict() != other.to_dict()
