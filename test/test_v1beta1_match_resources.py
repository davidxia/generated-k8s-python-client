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
from kubernetes.client.models.v1beta1_match_resources import V1beta1MatchResources  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1MatchResources(unittest.TestCase):
    """V1beta1MatchResources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1MatchResources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_match_resources.V1beta1MatchResources()  # noqa: E501
        if include_optional :
            return V1beta1MatchResources(
                exclude_resource_rules = [
                    kubernetes.client.models.v1beta1/named_rule_with_operations.v1beta1.NamedRuleWithOperations(
                        api_groups = [
                            '0'
                            ], 
                        api_versions = [
                            '0'
                            ], 
                        operations = [
                            '0'
                            ], 
                        resource_names = [
                            '0'
                            ], 
                        resources = [
                            '0'
                            ], 
                        scope = '0', )
                    ], 
                match_policy = '0', 
                namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                resource_rules = [
                    kubernetes.client.models.v1beta1/named_rule_with_operations.v1beta1.NamedRuleWithOperations(
                        api_groups = [
                            '0'
                            ], 
                        api_versions = [
                            '0'
                            ], 
                        operations = [
                            '0'
                            ], 
                        resource_names = [
                            '0'
                            ], 
                        resources = [
                            '0'
                            ], 
                        scope = '0', )
                    ]
            )
        else :
            return V1beta1MatchResources(
        )

    def testV1beta1MatchResources(self):
        """Test V1beta1MatchResources"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
