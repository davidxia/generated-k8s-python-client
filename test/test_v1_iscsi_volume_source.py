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
from kubernetes.client.models.v1_iscsi_volume_source import V1ISCSIVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ISCSIVolumeSource(unittest.TestCase):
    """V1ISCSIVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ISCSIVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_iscsi_volume_source.V1ISCSIVolumeSource()  # noqa: E501
        if include_optional :
            return V1ISCSIVolumeSource(
                chap_auth_discovery = True, 
                chap_auth_session = True, 
                fs_type = '0', 
                initiator_name = '0', 
                iqn = '0', 
                iscsi_interface = '0', 
                lun = 56, 
                portals = [
                    '0'
                    ], 
                read_only = True, 
                secret_ref = kubernetes.client.models.v1/local_object_reference.v1.LocalObjectReference(
                    name = '0', ), 
                target_portal = '0'
            )
        else :
            return V1ISCSIVolumeSource(
                iqn = '0',
                lun = 56,
                target_portal = '0',
        )

    def testV1ISCSIVolumeSource(self):
        """Test V1ISCSIVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()