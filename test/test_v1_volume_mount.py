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
from kubernetes.client.models.v1_volume_mount import V1VolumeMount  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1VolumeMount(unittest.TestCase):
    """V1VolumeMount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VolumeMount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_volume_mount.V1VolumeMount()  # noqa: E501
        if include_optional :
            return V1VolumeMount(
                mount_path = '0', 
                mount_propagation = '0', 
                name = '0', 
                read_only = True, 
                recursive_read_only = '0', 
                sub_path = '0', 
                sub_path_expr = '0'
            )
        else :
            return V1VolumeMount(
                mount_path = '0',
                name = '0',
        )

    def testV1VolumeMount(self):
        """Test V1VolumeMount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
