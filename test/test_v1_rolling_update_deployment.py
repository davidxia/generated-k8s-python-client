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
from kubernetes.client.models.v1_rolling_update_deployment import V1RollingUpdateDeployment  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1RollingUpdateDeployment(unittest.TestCase):
    """V1RollingUpdateDeployment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1RollingUpdateDeployment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_rolling_update_deployment.V1RollingUpdateDeployment()  # noqa: E501
        if include_optional :
            return V1RollingUpdateDeployment(
                max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable()
            )
        else :
            return V1RollingUpdateDeployment(
        )

    def testV1RollingUpdateDeployment(self):
        """Test V1RollingUpdateDeployment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
