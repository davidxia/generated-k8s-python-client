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
from kubernetes.client.models.v2_horizontal_pod_autoscaler_list import V2HorizontalPodAutoscalerList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV2HorizontalPodAutoscalerList(unittest.TestCase):
    """V2HorizontalPodAutoscalerList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2HorizontalPodAutoscalerList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v2_horizontal_pod_autoscaler_list.V2HorizontalPodAutoscalerList()  # noqa: E501
        if include_optional :
            return V2HorizontalPodAutoscalerList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.v2/horizontal_pod_autoscaler.v2.HorizontalPodAutoscaler(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    subresource = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.v2/horizontal_pod_autoscaler_spec.v2.HorizontalPodAutoscalerSpec(
                            behavior = kubernetes.client.models.v2/horizontal_pod_autoscaler_behavior.v2.HorizontalPodAutoscalerBehavior(
                                scale_down = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                                    policies = [
                                        kubernetes.client.models.v2/hpa_scaling_policy.v2.HPAScalingPolicy(
                                            period_seconds = 56, 
                                            type = '0', 
                                            value = 56, )
                                        ], 
                                    select_policy = '0', 
                                    stabilization_window_seconds = 56, ), 
                                scale_up = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                                    select_policy = '0', 
                                    stabilization_window_seconds = 56, ), ), 
                            max_replicas = 56, 
                            metrics = [
                                kubernetes.client.models.v2/metric_spec.v2.MetricSpec(
                                    container_resource = kubernetes.client.models.v2/container_resource_metric_source.v2.ContainerResourceMetricSource(
                                        container = '0', 
                                        name = '0', 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    external = kubernetes.client.models.v2/external_metric_source.v2.ExternalMetricSource(
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
                                            value = '0', ), ), 
                                    object = kubernetes.client.models.v2/object_metric_source.v2.ObjectMetricSource(
                                        described_object = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                                            api_version = '0', 
                                            kind = '0', 
                                            name = '0', ), 
                                        metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    pods = kubernetes.client.models.v2/pods_metric_source.v2.PodsMetricSource(
                                        metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    resource = kubernetes.client.models.v2/resource_metric_source.v2.ResourceMetricSource(
                                        name = '0', 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    type = '0', )
                                ], 
                            min_replicas = 56, 
                            scale_target_ref = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), ), 
                        status = kubernetes.client.models.v2/horizontal_pod_autoscaler_status.v2.HorizontalPodAutoscalerStatus(
                            conditions = [
                                kubernetes.client.models.v2/horizontal_pod_autoscaler_condition.v2.HorizontalPodAutoscalerCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            current_metrics = [
                                kubernetes.client.models.v2/metric_status.v2.MetricStatus(
                                    type = '0', )
                                ], 
                            current_replicas = 56, 
                            desired_replicas = 56, 
                            last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            observed_generation = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V2HorizontalPodAutoscalerList(
                items = [
                    kubernetes.client.models.v2/horizontal_pod_autoscaler.v2.HorizontalPodAutoscaler(
                        api_version = '0', 
                        kind = '0', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : '0'
                                }, 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                '0'
                                ], 
                            generate_name = '0', 
                            generation = 56, 
                            labels = {
                                'key' : '0'
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '0', 
                                    fields_type = '0', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '0', 
                                    operation = '0', 
                                    subresource = '0', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '0', 
                            namespace = '0', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '0', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '0', 
                                    name = '0', 
                                    uid = '0', )
                                ], 
                            resource_version = '0', 
                            self_link = '0', 
                            uid = '0', ), 
                        spec = kubernetes.client.models.v2/horizontal_pod_autoscaler_spec.v2.HorizontalPodAutoscalerSpec(
                            behavior = kubernetes.client.models.v2/horizontal_pod_autoscaler_behavior.v2.HorizontalPodAutoscalerBehavior(
                                scale_down = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                                    policies = [
                                        kubernetes.client.models.v2/hpa_scaling_policy.v2.HPAScalingPolicy(
                                            period_seconds = 56, 
                                            type = '0', 
                                            value = 56, )
                                        ], 
                                    select_policy = '0', 
                                    stabilization_window_seconds = 56, ), 
                                scale_up = kubernetes.client.models.v2/hpa_scaling_rules.v2.HPAScalingRules(
                                    select_policy = '0', 
                                    stabilization_window_seconds = 56, ), ), 
                            max_replicas = 56, 
                            metrics = [
                                kubernetes.client.models.v2/metric_spec.v2.MetricSpec(
                                    container_resource = kubernetes.client.models.v2/container_resource_metric_source.v2.ContainerResourceMetricSource(
                                        container = '0', 
                                        name = '0', 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    external = kubernetes.client.models.v2/external_metric_source.v2.ExternalMetricSource(
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
                                            value = '0', ), ), 
                                    object = kubernetes.client.models.v2/object_metric_source.v2.ObjectMetricSource(
                                        described_object = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                                            api_version = '0', 
                                            kind = '0', 
                                            name = '0', ), 
                                        metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    pods = kubernetes.client.models.v2/pods_metric_source.v2.PodsMetricSource(
                                        metric = kubernetes.client.models.v2/metric_identifier.v2.MetricIdentifier(
                                            name = '0', ), 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    resource = kubernetes.client.models.v2/resource_metric_source.v2.ResourceMetricSource(
                                        name = '0', 
                                        target = kubernetes.client.models.v2/metric_target.v2.MetricTarget(
                                            average_utilization = 56, 
                                            average_value = '0', 
                                            type = '0', 
                                            value = '0', ), ), 
                                    type = '0', )
                                ], 
                            min_replicas = 56, 
                            scale_target_ref = kubernetes.client.models.v2/cross_version_object_reference.v2.CrossVersionObjectReference(
                                api_version = '0', 
                                kind = '0', 
                                name = '0', ), ), 
                        status = kubernetes.client.models.v2/horizontal_pod_autoscaler_status.v2.HorizontalPodAutoscalerStatus(
                            conditions = [
                                kubernetes.client.models.v2/horizontal_pod_autoscaler_condition.v2.HorizontalPodAutoscalerCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            current_metrics = [
                                kubernetes.client.models.v2/metric_status.v2.MetricStatus(
                                    type = '0', )
                                ], 
                            current_replicas = 56, 
                            desired_replicas = 56, 
                            last_scale_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            observed_generation = 56, ), )
                    ],
        )

    def testV2HorizontalPodAutoscalerList(self):
        """Test V2HorizontalPodAutoscalerList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
