# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: master
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.coordination_api import CoordinationApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCoordinationApi(unittest.TestCase):
    """CoordinationApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.coordination_api.CoordinationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_group(self):
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
