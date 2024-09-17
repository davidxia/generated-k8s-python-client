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
from kubernetes.client.models.v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1WeightedPodAffinityTerm(unittest.TestCase):
    """V1WeightedPodAffinityTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1WeightedPodAffinityTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_weighted_pod_affinity_term.V1WeightedPodAffinityTerm()  # noqa: E501
        if include_optional :
            return V1WeightedPodAffinityTerm(
                pod_affinity_term = kubernetes.client.models.v1/pod_affinity_term.v1.PodAffinityTerm(
                    label_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                        match_expressions = [
                            kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                key = '0', 
                                operator = '0', 
                                values = [
                                    '0'
                                    ], )
                            ], 
                        match_labels = {
                            'key' : '0'
                            }, ), 
                    match_label_keys = [
                        '0'
                        ], 
                    mismatch_label_keys = [
                        '0'
                        ], 
                    namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                    namespaces = [
                        '0'
                        ], 
                    topology_key = '0', ), 
                weight = 56
            )
        else :
            return V1WeightedPodAffinityTerm(
                pod_affinity_term = kubernetes.client.models.v1/pod_affinity_term.v1.PodAffinityTerm(
                    label_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                        match_expressions = [
                            kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                key = '0', 
                                operator = '0', 
                                values = [
                                    '0'
                                    ], )
                            ], 
                        match_labels = {
                            'key' : '0'
                            }, ), 
                    match_label_keys = [
                        '0'
                        ], 
                    mismatch_label_keys = [
                        '0'
                        ], 
                    namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                    namespaces = [
                        '0'
                        ], 
                    topology_key = '0', ),
                weight = 56,
        )

    def testV1WeightedPodAffinityTerm(self):
        """Test V1WeightedPodAffinityTerm"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()