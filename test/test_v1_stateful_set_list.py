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
from kubernetes.client.models.v1_stateful_set_list import V1StatefulSetList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1StatefulSetList(unittest.TestCase):
    """V1StatefulSetList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1StatefulSetList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_stateful_set_list.V1StatefulSetList()  # noqa: E501
        if include_optional :
            return V1StatefulSetList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.v1/stateful_set.v1.StatefulSet(
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
                        spec = kubernetes.client.models.v1/stateful_set_spec.v1.StatefulSetSpec(
                            min_ready_seconds = 56, 
                            ordinals = kubernetes.client.models.v1/stateful_set_ordinals.v1.StatefulSetOrdinals(
                                start = 56, ), 
                            persistent_volume_claim_retention_policy = kubernetes.client.models.v1/stateful_set_persistent_volume_claim_retention_policy.v1.StatefulSetPersistentVolumeClaimRetentionPolicy(
                                when_deleted = '0', 
                                when_scaled = '0', ), 
                            pod_management_policy = '0', 
                            replicas = 56, 
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
                            service_name = '0', 
                            template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            update_strategy = kubernetes.client.models.v1/stateful_set_update_strategy.v1.StatefulSetUpdateStrategy(
                                rolling_update = kubernetes.client.models.v1/rolling_update_stateful_set_strategy.v1.RollingUpdateStatefulSetStrategy(
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), 
                                    partition = 56, ), 
                                type = '0', ), 
                            volume_claim_templates = [
                                kubernetes.client.models.v1/persistent_volume_claim.v1.PersistentVolumeClaim(
                                    api_version = '0', 
                                    kind = '0', 
                                    status = kubernetes.client.models.v1/persistent_volume_claim_status.v1.PersistentVolumeClaimStatus(
                                        access_modes = [
                                            '0'
                                            ], 
                                        allocated_resource_statuses = {
                                            'key' : '0'
                                            }, 
                                        allocated_resources = {
                                            'key' : '0'
                                            }, 
                                        capacity = {
                                            'key' : '0'
                                            }, 
                                        conditions = [
                                            kubernetes.client.models.v1/persistent_volume_claim_condition.v1.PersistentVolumeClaimCondition(
                                                last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                message = '0', 
                                                reason = '0', 
                                                status = '0', 
                                                type = '0', )
                                            ], 
                                        current_volume_attributes_class_name = '0', 
                                        modify_volume_status = kubernetes.client.models.v1/modify_volume_status.v1.ModifyVolumeStatus(
                                            status = '0', 
                                            target_volume_attributes_class_name = '0', ), 
                                        phase = '0', ), )
                                ], ), 
                        status = kubernetes.client.models.v1/stateful_set_status.v1.StatefulSetStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            current_replicas = 56, 
                            current_revision = '0', 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            update_revision = '0', 
                            updated_replicas = 56, ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V1StatefulSetList(
                items = [
                    kubernetes.client.models.v1/stateful_set.v1.StatefulSet(
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
                        spec = kubernetes.client.models.v1/stateful_set_spec.v1.StatefulSetSpec(
                            min_ready_seconds = 56, 
                            ordinals = kubernetes.client.models.v1/stateful_set_ordinals.v1.StatefulSetOrdinals(
                                start = 56, ), 
                            persistent_volume_claim_retention_policy = kubernetes.client.models.v1/stateful_set_persistent_volume_claim_retention_policy.v1.StatefulSetPersistentVolumeClaimRetentionPolicy(
                                when_deleted = '0', 
                                when_scaled = '0', ), 
                            pod_management_policy = '0', 
                            replicas = 56, 
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
                            service_name = '0', 
                            template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(), 
                            update_strategy = kubernetes.client.models.v1/stateful_set_update_strategy.v1.StatefulSetUpdateStrategy(
                                rolling_update = kubernetes.client.models.v1/rolling_update_stateful_set_strategy.v1.RollingUpdateStatefulSetStrategy(
                                    max_unavailable = kubernetes.client.models.max_unavailable.maxUnavailable(), 
                                    partition = 56, ), 
                                type = '0', ), 
                            volume_claim_templates = [
                                kubernetes.client.models.v1/persistent_volume_claim.v1.PersistentVolumeClaim(
                                    api_version = '0', 
                                    kind = '0', 
                                    status = kubernetes.client.models.v1/persistent_volume_claim_status.v1.PersistentVolumeClaimStatus(
                                        access_modes = [
                                            '0'
                                            ], 
                                        allocated_resource_statuses = {
                                            'key' : '0'
                                            }, 
                                        allocated_resources = {
                                            'key' : '0'
                                            }, 
                                        capacity = {
                                            'key' : '0'
                                            }, 
                                        conditions = [
                                            kubernetes.client.models.v1/persistent_volume_claim_condition.v1.PersistentVolumeClaimCondition(
                                                last_probe_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                message = '0', 
                                                reason = '0', 
                                                status = '0', 
                                                type = '0', )
                                            ], 
                                        current_volume_attributes_class_name = '0', 
                                        modify_volume_status = kubernetes.client.models.v1/modify_volume_status.v1.ModifyVolumeStatus(
                                            status = '0', 
                                            target_volume_attributes_class_name = '0', ), 
                                        phase = '0', ), )
                                ], ), 
                        status = kubernetes.client.models.v1/stateful_set_status.v1.StatefulSetStatus(
                            available_replicas = 56, 
                            collision_count = 56, 
                            current_replicas = 56, 
                            current_revision = '0', 
                            observed_generation = 56, 
                            ready_replicas = 56, 
                            replicas = 56, 
                            update_revision = '0', 
                            updated_replicas = 56, ), )
                    ],
        )

    def testV1StatefulSetList(self):
        """Test V1StatefulSetList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()