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
from kubernetes.client.models.v1_daemon_set_list import V1DaemonSetList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1DaemonSetList(unittest.TestCase):
    """V1DaemonSetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DaemonSetList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_daemon_set_list.V1DaemonSetList()  # noqa: E501
        if include_optional :
            return V1DaemonSetList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.v1/daemon_set.v1.DaemonSet(
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
                        spec = kubernetes.client.models.v1/daemon_set_spec.v1.DaemonSetSpec(
                            min_ready_seconds = 56, 
                            revision_history_limit = 56, 
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
                                    }, ), 
                            template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            update_strategy = kubernetes.client.models.v1/daemon_set_update_strategy.v1.DaemonSetUpdateStrategy(
                                rolling_update = kubernetes.client.models.v1/rolling_update_daemon_set.v1.RollingUpdateDaemonSet(
                                    max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), ), 
                        status = kubernetes.client.models.v1/daemon_set_status.v1.DaemonSetStatus(
                            collision_count = 56, 
                            conditions = [
                                kubernetes.client.models.v1/daemon_set_condition.v1.DaemonSetCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            current_number_scheduled = 56, 
                            desired_number_scheduled = 56, 
                            number_available = 56, 
                            number_misscheduled = 56, 
                            number_ready = 56, 
                            number_unavailable = 56, 
                            observed_generation = 56, 
                            updated_number_scheduled = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V1DaemonSetList(
                items = [
                    kubernetes.client.models.v1/daemon_set.v1.DaemonSet(
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
                        spec = kubernetes.client.models.v1/daemon_set_spec.v1.DaemonSetSpec(
                            min_ready_seconds = 56, 
                            revision_history_limit = 56, 
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
                                    }, ), 
                            template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            update_strategy = kubernetes.client.models.v1/daemon_set_update_strategy.v1.DaemonSetUpdateStrategy(
                                rolling_update = kubernetes.client.models.v1/rolling_update_daemon_set.v1.RollingUpdateDaemonSet(
                                    max_surge = kubernetes.client.models.max_surge.maxSurge(), 
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), ), 
                                type = '0', ), ), 
                        status = kubernetes.client.models.v1/daemon_set_status.v1.DaemonSetStatus(
                            collision_count = 56, 
                            conditions = [
                                kubernetes.client.models.v1/daemon_set_condition.v1.DaemonSetCondition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            current_number_scheduled = 56, 
                            desired_number_scheduled = 56, 
                            number_available = 56, 
                            number_misscheduled = 56, 
                            number_ready = 56, 
                            number_unavailable = 56, 
                            observed_generation = 56, 
                            updated_number_scheduled = 56, ), )
                    ],
        )

    def testV1DaemonSetList(self):
        """Test V1DaemonSetList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
