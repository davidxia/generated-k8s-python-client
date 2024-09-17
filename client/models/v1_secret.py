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


class V1Secret(object):
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
        'data': 'dict(str, str)',
        'immutable': 'bool',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'string_data': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'data': 'data',
        'immutable': 'immutable',
        'kind': 'kind',
        'metadata': 'metadata',
        'string_data': 'stringData',
        'type': 'type'
    }

    def __init__(self, api_version=None, data=None, immutable=None, kind=None, metadata=None, string_data=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1Secret - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._data = None
        self._immutable = None
        self._kind = None
        self._metadata = None
        self._string_data = None
        self._type = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if data is not None:
            self.data = data
        if immutable is not None:
            self.immutable = immutable
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if string_data is not None:
            self.string_data = string_data
        if type is not None:
            self.type = type

    @property
    def api_version(self):
        """Gets the api_version of this V1Secret.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1Secret.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1Secret.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1Secret.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def data(self):
        """Gets the data of this V1Secret.  # noqa: E501

        Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4  # noqa: E501

        :return: The data of this V1Secret.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this V1Secret.

        Data contains the secret data. Each key must consist of alphanumeric characters, '-', '_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in https://tools.ietf.org/html/rfc4648#section-4  # noqa: E501

        :param data: The data of this V1Secret.  # noqa: E501
        :type: dict(str, str)
        """

        self._data = data

    @property
    def immutable(self):
        """Gets the immutable of this V1Secret.  # noqa: E501

        Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil.  # noqa: E501

        :return: The immutable of this V1Secret.  # noqa: E501
        :rtype: bool
        """
        return self._immutable

    @immutable.setter
    def immutable(self, immutable):
        """Sets the immutable of this V1Secret.

        Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil.  # noqa: E501

        :param immutable: The immutable of this V1Secret.  # noqa: E501
        :type: bool
        """

        self._immutable = immutable

    @property
    def kind(self):
        """Gets the kind of this V1Secret.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1Secret.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1Secret.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1Secret.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1Secret.  # noqa: E501


        :return: The metadata of this V1Secret.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1Secret.


        :param metadata: The metadata of this V1Secret.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def string_data(self):
        """Gets the string_data of this V1Secret.  # noqa: E501

        stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API.  # noqa: E501

        :return: The string_data of this V1Secret.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._string_data

    @string_data.setter
    def string_data(self, string_data):
        """Sets the string_data of this V1Secret.

        stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API.  # noqa: E501

        :param string_data: The string_data of this V1Secret.  # noqa: E501
        :type: dict(str, str)
        """

        self._string_data = string_data

    @property
    def type(self):
        """Gets the type of this V1Secret.  # noqa: E501

        Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types  # noqa: E501

        :return: The type of this V1Secret.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1Secret.

        Used to facilitate programmatic handling of secret data. More info: https://kubernetes.io/docs/concepts/configuration/secret/#secret-types  # noqa: E501

        :param type: The type of this V1Secret.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, V1Secret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Secret):
            return True

        return self.to_dict() != other.to_dict()
