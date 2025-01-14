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
from kubernetes.client.models.v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1PersistentVolumeClaimStatus(unittest.TestCase):
    """V1PersistentVolumeClaimStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PersistentVolumeClaimStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_persistent_volume_claim_status.V1PersistentVolumeClaimStatus()  # noqa: E501
        if include_optional :
            return V1PersistentVolumeClaimStatus(
                access_modes = [
                    '0'
                    ], 
                allocated_resource_statuses = {
                    'key' : '0'
                    }, 
                allocated_resources = {
                    'key' : '0'
                    }, 
                capacity = {
                    'key' : '0'
                    }, 
                conditions = [
                    kubernetes.client.models.v1/persistent_volume_claim_condition.v1.PersistentVolumeClaimCondition(
                        last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                current_volume_attributes_class_name = '0', 
                modify_volume_status = kubernetes.client.models.v1/modify_volume_status.v1.ModifyVolumeStatus(
                    status = '0', 
                    target_volume_attributes_class_name = '0', ), 
                phase = '0'
            )
        else :
            return V1PersistentVolumeClaimStatus(
        )

    def testV1PersistentVolumeClaimStatus(self):
        """Test V1PersistentVolumeClaimStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
