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
from kubernetes.client.models.v1_status_details import V1StatusDetails  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1StatusDetails(unittest.TestCase):
    """V1StatusDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1StatusDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_status_details.V1StatusDetails()  # noqa: E501
        if include_optional :
            return V1StatusDetails(
                causes = [
                    kubernetes.client.models.v1/status_cause.v1.StatusCause(
                        field = '0', 
                        message = '0', 
                        reason = '0', )
                    ], 
                group = '0', 
                kind = '0', 
                name = '0', 
                retry_after_seconds = 56, 
                uid = '0'
            )
        else :
            return V1StatusDetails(
        )

    def testV1StatusDetails(self):
        """Test V1StatusDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
