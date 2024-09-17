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
from kubernetes.client.models.v1_http_get_action import V1HTTPGetAction  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1HTTPGetAction(unittest.TestCase):
    """V1HTTPGetAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1HTTPGetAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_http_get_action.V1HTTPGetAction()  # noqa: E501
        if include_optional :
            return V1HTTPGetAction(
                host = '0', 
                http_headers = [
                    kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                        name = '0', 
                        value = '0', )
                    ], 
                path = '0', 
                port = kubernetes.client.models.port.port(), 
                scheme = '0'
            )
        else :
            return V1HTTPGetAction(
                port = kubernetes.client.models.port.port(),
        )

    def testV1HTTPGetAction(self):
        """Test V1HTTPGetAction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()