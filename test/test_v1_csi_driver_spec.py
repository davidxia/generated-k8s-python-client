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
from kubernetes.client.models.v1_csi_driver_spec import V1CSIDriverSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1CSIDriverSpec(unittest.TestCase):
    """V1CSIDriverSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CSIDriverSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_csi_driver_spec.V1CSIDriverSpec()  # noqa: E501
        if include_optional :
            return V1CSIDriverSpec(
                attach_required = True, 
                fs_group_policy = '0', 
                pod_info_on_mount = True, 
                requires_republish = True, 
                se_linux_mount = True, 
                storage_capacity = True, 
                token_requests = [
                    kubernetes.client.models.storage/v1/token_request.storage.v1.TokenRequest(
                        audience = '0', 
                        expiration_seconds = 56, )
                    ], 
                volume_lifecycle_modes = [
                    '0'
                    ]
            )
        else :
            return V1CSIDriverSpec(
        )

    def testV1CSIDriverSpec(self):
        """Test V1CSIDriverSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
