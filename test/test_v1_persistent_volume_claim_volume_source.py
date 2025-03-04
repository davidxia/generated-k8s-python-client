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
from kubernetes.client.models.v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1PersistentVolumeClaimVolumeSource(unittest.TestCase):
    """V1PersistentVolumeClaimVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PersistentVolumeClaimVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_persistent_volume_claim_volume_source.V1PersistentVolumeClaimVolumeSource()  # noqa: E501
        if include_optional :
            return V1PersistentVolumeClaimVolumeSource(
                claim_name = '0', 
                read_only = True
            )
        else :
            return V1PersistentVolumeClaimVolumeSource(
                claim_name = '0',
        )

    def testV1PersistentVolumeClaimVolumeSource(self):
        """Test V1PersistentVolumeClaimVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
