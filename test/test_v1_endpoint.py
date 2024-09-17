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
from kubernetes.client.models.v1_endpoint import V1Endpoint  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1Endpoint(unittest.TestCase):
    """V1Endpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Endpoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_endpoint.V1Endpoint()  # noqa: E501
        if include_optional :
            return V1Endpoint(
                addresses = [
                    '0'
                    ], 
                conditions = kubernetes.client.models.v1/endpoint_conditions.v1.EndpointConditions(
                    ready = True, 
                    serving = True, 
                    terminating = True, ), 
                deprecated_topology = {
                    'key' : '0'
                    }, 
                hints = kubernetes.client.models.v1/endpoint_hints.v1.EndpointHints(
                    for_zones = [
                        kubernetes.client.models.v1/for_zone.v1.ForZone(
                            name = '0', )
                        ], ), 
                hostname = '0', 
                node_name = '0', 
                target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                    api_version = '0', 
                    field_path = '0', 
                    kind = '0', 
                    name = '0', 
                    namespace = '0', 
                    resource_version = '0', 
                    uid = '0', ), 
                zone = '0'
            )
        else :
            return V1Endpoint(
                addresses = [
                    '0'
                    ],
        )

    def testV1Endpoint(self):
        """Test V1Endpoint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()