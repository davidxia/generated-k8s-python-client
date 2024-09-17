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
from kubernetes.client.models.v1_cinder_persistent_volume_source import V1CinderPersistentVolumeSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1CinderPersistentVolumeSource(unittest.TestCase):
    """V1CinderPersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CinderPersistentVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_cinder_persistent_volume_source.V1CinderPersistentVolumeSource()  # noqa: E501
        if include_optional :
            return V1CinderPersistentVolumeSource(
                fs_type = '0', 
                read_only = True, 
                secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '0', 
                    namespace = '0', ), 
                volume_id = '0'
            )
        else :
            return V1CinderPersistentVolumeSource(
                volume_id = '0',
        )

    def testV1CinderPersistentVolumeSource(self):
        """Test V1CinderPersistentVolumeSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
