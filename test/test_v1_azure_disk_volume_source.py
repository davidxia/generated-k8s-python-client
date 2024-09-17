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
from kubernetes.client.models.v1_azure_disk_volume_source import V1AzureDiskVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1AzureDiskVolumeSource(unittest.TestCase):
    """V1AzureDiskVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1AzureDiskVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_azure_disk_volume_source.V1AzureDiskVolumeSource()  # noqa: E501
        if include_optional :
            return V1AzureDiskVolumeSource(
                caching_mode = '0', 
                disk_name = '0', 
                disk_uri = '0', 
                fs_type = '0', 
                kind = '0', 
                read_only = True
            )
        else :
            return V1AzureDiskVolumeSource(
                disk_name = '0',
                disk_uri = '0',
        )

    def testV1AzureDiskVolumeSource(self):
        """Test V1AzureDiskVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
