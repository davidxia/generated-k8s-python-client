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
from kubernetes.client.models.v1_deployment_status import V1DeploymentStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1DeploymentStatus(unittest.TestCase):
    """V1DeploymentStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DeploymentStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_deployment_status.V1DeploymentStatus()  # noqa: E501
        if include_optional :
            return V1DeploymentStatus(
                available_replicas = 56, 
                collision_count = 56, 
                conditions = [
                    kubernetes.client.models.v1/deployment_condition.v1.DeploymentCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                observed_generation = 56, 
                ready_replicas = 56, 
                replicas = 56, 
                unavailable_replicas = 56, 
                updated_replicas = 56
            )
        else :
            return V1DeploymentStatus(
        )

    def testV1DeploymentStatus(self):
        """Test V1DeploymentStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
