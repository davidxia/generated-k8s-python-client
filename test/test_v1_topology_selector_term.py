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
from kubernetes.client.models.v1_topology_selector_term import V1TopologySelectorTerm  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1TopologySelectorTerm(unittest.TestCase):
    """V1TopologySelectorTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1TopologySelectorTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_topology_selector_term.V1TopologySelectorTerm()  # noqa: E501
        if include_optional :
            return V1TopologySelectorTerm(
                match_label_expressions = [
                    kubernetes.client.models.v1/topology_selector_label_requirement.v1.TopologySelectorLabelRequirement(
                        key = '0', 
                        values = [
                            '0'
                            ], )
                    ]
            )
        else :
            return V1TopologySelectorTerm(
        )

    def testV1TopologySelectorTerm(self):
        """Test V1TopologySelectorTerm"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
