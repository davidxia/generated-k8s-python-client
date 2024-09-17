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
from kubernetes.client.models.v1_lifecycle import V1Lifecycle  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1Lifecycle(unittest.TestCase):
    """V1Lifecycle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Lifecycle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_lifecycle.V1Lifecycle()  # noqa: E501
        if include_optional :
            return V1Lifecycle(
                post_start = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            '0'
                            ], ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '0', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '0', 
                                value = '0', )
                            ], 
                        path = '0', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '0', ), 
                    sleep = kubernetes.client.models.v1/sleep_action.v1.SleepAction(
                        seconds = 56, ), 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '0', 
                        port = kubernetes.client.models.port.port(), ), ), 
                pre_stop = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            '0'
                            ], ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '0', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '0', 
                                value = '0', )
                            ], 
                        path = '0', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '0', ), 
                    sleep = kubernetes.client.models.v1/sleep_action.v1.SleepAction(
                        seconds = 56, ), 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '0', 
                        port = kubernetes.client.models.port.port(), ), )
            )
        else :
            return V1Lifecycle(
        )

    def testV1Lifecycle(self):
        """Test V1Lifecycle"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
