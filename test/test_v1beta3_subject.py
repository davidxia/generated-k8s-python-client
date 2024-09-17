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
from kubernetes.client.models.v1beta3_subject import V1beta3Subject  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta3Subject(unittest.TestCase):
    """V1beta3Subject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta3Subject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta3_subject.V1beta3Subject()  # noqa: E501
        if include_optional :
            return V1beta3Subject(
                group = kubernetes.client.models.v1beta3/group_subject.v1beta3.GroupSubject(
                    name = '0', ), 
                kind = '0', 
                service_account = kubernetes.client.models.v1beta3/service_account_subject.v1beta3.ServiceAccountSubject(
                    name = '0', 
                    namespace = '0', ), 
                user = kubernetes.client.models.v1beta3/user_subject.v1beta3.UserSubject(
                    name = '0', )
            )
        else :
            return V1beta3Subject(
                kind = '0',
        )

    def testV1beta3Subject(self):
        """Test V1beta3Subject"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()