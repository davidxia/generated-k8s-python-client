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


class V1OwnerReference(object):
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
        'api_version': 'str',
        'block_owner_deletion': 'bool',
        'controller': 'bool',
        'kind': 'str',
        'name': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'block_owner_deletion': 'blockOwnerDeletion',
        'controller': 'controller',
        'kind': 'kind',
        'name': 'name',
        'uid': 'uid'
    }

    def __init__(self, api_version=None, block_owner_deletion=None, controller=None, kind=None, name=None, uid=None, local_vars_configuration=None):  # noqa: E501
        """V1OwnerReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._block_owner_deletion = None
        self._controller = None
        self._kind = None
        self._name = None
        self._uid = None
        self.discriminator = None

        self.api_version = api_version
        if block_owner_deletion is not None:
            self.block_owner_deletion = block_owner_deletion
        if controller is not None:
            self.controller = controller
        self.kind = kind
        self.name = name
        self.uid = uid

    @property
    def api_version(self):
        """Gets the api_version of this V1OwnerReference.  # noqa: E501

        API version of the referent.  # noqa: E501

        :return: The api_version of this V1OwnerReference.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1OwnerReference.

        API version of the referent.  # noqa: E501

        :param api_version: The api_version of this V1OwnerReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and api_version is None:  # noqa: E501
            raise ValueError("Invalid value for `api_version`, must not be `None`")  # noqa: E501

        self._api_version = api_version

    @property
    def block_owner_deletion(self):
        """Gets the block_owner_deletion of this V1OwnerReference.  # noqa: E501

        If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs \"delete\" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.  # noqa: E501

        :return: The block_owner_deletion of this V1OwnerReference.  # noqa: E501
        :rtype: bool
        """
        return self._block_owner_deletion

    @block_owner_deletion.setter
    def block_owner_deletion(self, block_owner_deletion):
        """Sets the block_owner_deletion of this V1OwnerReference.

        If true, AND if the owner has the \"foregroundDeletion\" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs \"delete\" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.  # noqa: E501

        :param block_owner_deletion: The block_owner_deletion of this V1OwnerReference.  # noqa: E501
        :type: bool
        """

        self._block_owner_deletion = block_owner_deletion

    @property
    def controller(self):
        """Gets the controller of this V1OwnerReference.  # noqa: E501

        If true, this reference points to the managing controller.  # noqa: E501

        :return: The controller of this V1OwnerReference.  # noqa: E501
        :rtype: bool
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this V1OwnerReference.

        If true, this reference points to the managing controller.  # noqa: E501

        :param controller: The controller of this V1OwnerReference.  # noqa: E501
        :type: bool
        """

        self._controller = controller

    @property
    def kind(self):
        """Gets the kind of this V1OwnerReference.  # noqa: E501

        Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1OwnerReference.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1OwnerReference.

        Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1OwnerReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this V1OwnerReference.  # noqa: E501

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names  # noqa: E501

        :return: The name of this V1OwnerReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1OwnerReference.

        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names  # noqa: E501

        :param name: The name of this V1OwnerReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this V1OwnerReference.  # noqa: E501

        UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids  # noqa: E501

        :return: The uid of this V1OwnerReference.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this V1OwnerReference.

        UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids  # noqa: E501

        :param uid: The uid of this V1OwnerReference.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uid is None:  # noqa: E501
            raise ValueError("Invalid value for `uid`, must not be `None`")  # noqa: E501

        self._uid = uid

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
        if not isinstance(other, V1OwnerReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1OwnerReference):
            return True

        return self.to_dict() != other.to_dict()
