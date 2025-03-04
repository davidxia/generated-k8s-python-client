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
from kubernetes.client.models.v1_job_status import V1JobStatus  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1JobStatus(unittest.TestCase):
    """V1JobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1JobStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_job_status.V1JobStatus()  # noqa: E501
        if include_optional :
            return V1JobStatus(
                active = 56, 
                completed_indexes = '0', 
                completion_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                conditions = [
                    kubernetes.client.models.v1/job_condition.v1.JobCondition(
                        last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '0', 
                        reason = '0', 
                        status = '0', 
                        type = '0', )
                    ], 
                failed = 56, 
                failed_indexes = '0', 
                ready = 56, 
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                succeeded = 56, 
                terminating = 56, 
                uncounted_terminated_pods = kubernetes.client.models.v1/uncounted_terminated_pods.v1.UncountedTerminatedPods(
                    failed = [
                        '0'
                        ], 
                    succeeded = [
                        '0'
                        ], )
            )
        else :
            return V1JobStatus(
        )

    def testV1JobStatus(self):
        """Test V1JobStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
