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
from kubernetes.client.models.v1_ingress_status import V1IngressStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1IngressStatus(unittest.TestCase):
    """V1IngressStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1IngressStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_ingress_status.V1IngressStatus()  # noqa: E501
        if include_optional :
            return V1IngressStatus(
                load_balancer = kubernetes.client.models.v1/ingress_load_balancer_status.v1.IngressLoadBalancerStatus(
                    ingress = [
                        kubernetes.client.models.v1/ingress_load_balancer_ingress.v1.IngressLoadBalancerIngress(
                            hostname = '0', 
                            ip = '0', 
                            ports = [
                                kubernetes.client.models.v1/ingress_port_status.v1.IngressPortStatus(
                                    error = '0', 
                                    port = 56, 
                                    protocol = '0', )
                                ], )
                        ], )
            )
        else :
            return V1IngressStatus(
        )

    def testV1IngressStatus(self):
        """Test V1IngressStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
