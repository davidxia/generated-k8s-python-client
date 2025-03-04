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
from kubernetes.client.models.v1_volume_node_affinity import V1VolumeNodeAffinity  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1VolumeNodeAffinity(unittest.TestCase):
    """V1VolumeNodeAffinity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1VolumeNodeAffinity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_volume_node_affinity.V1VolumeNodeAffinity()  # noqa: E501
        if include_optional :
            return V1VolumeNodeAffinity(
                required = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                    node_selector_terms = [
                        kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                            match_expressions = [
                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '0', 
                                    operator = '0', 
                                    values = [
                                        '0'
                                        ], )
                                ], 
                            match_fields = [
                                kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                    key = '0', 
                                    operator = '0', )
                                ], )
                        ], )
            )
        else :
            return V1VolumeNodeAffinity(
        )

    def testV1VolumeNodeAffinity(self):
        """Test V1VolumeNodeAffinity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
