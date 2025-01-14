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
from kubernetes.client.models.v1alpha1_storage_version_status import V1alpha1StorageVersionStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha1StorageVersionStatus(unittest.TestCase):
    """V1alpha1StorageVersionStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1StorageVersionStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha1_storage_version_status.V1alpha1StorageVersionStatus()  # noqa: E501
        if include_optional :
            return V1alpha1StorageVersionStatus(
                common_encoding_version = '0', 
                conditions = [
                    kubernetes.client.models.v1alpha1/storage_version_condition.v1alpha1.StorageVersionCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        observed_generation = 56, 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                storage_versions = [
                    kubernetes.client.models.v1alpha1/server_storage_version.v1alpha1.ServerStorageVersion(
                        api_server_id = '0', 
                        decodable_versions = [
                            '0'
                            ], 
                        encoding_version = '0', 
                        served_versions = [
                            '0'
                            ], )
                    ]
            )
        else :
            return V1alpha1StorageVersionStatus(
        )

    def testV1alpha1StorageVersionStatus(self):
        """Test V1alpha1StorageVersionStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
