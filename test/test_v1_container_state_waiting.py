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
from kubernetes.client.models.v1_container_state_waiting import V1ContainerStateWaiting  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ContainerStateWaiting(unittest.TestCase):
    """V1ContainerStateWaiting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ContainerStateWaiting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_container_state_waiting.V1ContainerStateWaiting()  # noqa: E501
        if include_optional :
            return V1ContainerStateWaiting(
                message = '0', 
                reason = '0'
            )
        else :
            return V1ContainerStateWaiting(
        )

    def testV1ContainerStateWaiting(self):
        """Test V1ContainerStateWaiting"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
