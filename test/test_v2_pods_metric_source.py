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
from kubernetes.client.models.v2_pods_metric_source import V2PodsMetricSource  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2PodsMetricSource(unittest.TestCase):
    """V2PodsMetricSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2PodsMetricSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2_pods_metric_source.V2PodsMetricSource()  # noqa: E501
        if include_optional :
            return V2PodsMetricSource(
                metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                    name = '0', 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                            }, ), ), 
                target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '0', 
                    type = '0', 
                    value = '0', )
            )
        else :
            return V2PodsMetricSource(
                metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                    name = '0', 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                            }, ), ),
                target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                    average_utilization = 56, 
                    average_value = '0', 
                    type = '0', 
                    value = '0', ),
        )

    def testV2PodsMetricSource(self):
        """Test V2PodsMetricSource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
