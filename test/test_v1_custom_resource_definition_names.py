# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: master
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kubernetes.client
from kubernetes.client.models.v1_custom_resource_definition_names import V1CustomResourceDefinitionNames  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1CustomResourceDefinitionNames(unittest.TestCase):
    """V1CustomResourceDefinitionNames unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CustomResourceDefinitionNames
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_custom_resource_definition_names.V1CustomResourceDefinitionNames()  # noqa: E501
        if include_optional :
            return V1CustomResourceDefinitionNames(
                categories = [
                    '0'
                    ], 
                kind = '0', 
                list_kind = '0', 
                plural = '0', 
                short_names = [
                    '0'
                    ], 
                singular = '0'
            )
        else :
            return V1CustomResourceDefinitionNames(
                kind = '0',
                plural = '0',
        )

    def testV1CustomResourceDefinitionNames(self):
        """Test V1CustomResourceDefinitionNames"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
