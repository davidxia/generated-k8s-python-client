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
from kubernetes.client.models.v1_container_state import V1ContainerState  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1ContainerState(unittest.TestCase):
    """V1ContainerState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ContainerState
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_container_state.V1ContainerState()  # noqa: E501
        if include_optional :
            return V1ContainerState(
                running = kubernetes.client.models.v1/container_state_running.v1.ContainerStateRunning(
                    started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                terminated = kubernetes.client.models.v1/container_state_terminated.v1.ContainerStateTerminated(
                    container_id = '0', 
                    exit_code = 56, 
                    finished_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    message = '0', 
                    reason = '0', 
                    signal = 56, 
                    started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                waiting = kubernetes.client.models.v1/container_state_waiting.v1.ContainerStateWaiting(
                    message = '0', 
                    reason = '0', )
            )
        else :
            return V1ContainerState(
        )

    def testV1ContainerState(self):
        """Test V1ContainerState"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()