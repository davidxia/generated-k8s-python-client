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
from kubernetes.client.models.v1_container_image import V1ContainerImage  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ContainerImage(unittest.TestCase):
    """V1ContainerImage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ContainerImage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_container_image.V1ContainerImage()  # noqa: E501
        if include_optional :
            return V1ContainerImage(
                names = [
                    '0'
                    ], 
                size_bytes = 56
            )
        else :
            return V1ContainerImage(
        )

    def testV1ContainerImage(self):
        """Test V1ContainerImage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()