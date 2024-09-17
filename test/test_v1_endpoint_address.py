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
from kubernetes.client.models.v1_endpoint_address import V1EndpointAddress  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1EndpointAddress(unittest.TestCase):
    """V1EndpointAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1EndpointAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_endpoint_address.V1EndpointAddress()  # noqa: E501
        if include_optional :
            return V1EndpointAddress(
                hostname = '0', 
                ip = '0', 
                node_name = '0', 
                target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                    api_version = '0', 
                    field_path = '0', 
                    kind = '0', 
                    name = '0', 
                    namespace = '0', 
                    resource_version = '0', 
                    uid = '0', )
            )
        else :
            return V1EndpointAddress(
                ip = '0',
        )

    def testV1EndpointAddress(self):
        """Test V1EndpointAddress"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()