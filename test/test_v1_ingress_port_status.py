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
from kubernetes.client.models.v1_ingress_port_status import V1IngressPortStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1IngressPortStatus(unittest.TestCase):
    """V1IngressPortStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1IngressPortStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_ingress_port_status.V1IngressPortStatus()  # noqa: E501
        if include_optional :
            return V1IngressPortStatus(
                error = '0', 
                port = 56, 
                protocol = '0'
            )
        else :
            return V1IngressPortStatus(
                port = 56,
                protocol = '0',
        )

    def testV1IngressPortStatus(self):
        """Test V1IngressPortStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
