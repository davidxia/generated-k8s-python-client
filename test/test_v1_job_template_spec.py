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
from kubernetes.client.models.v1_job_template_spec import V1JobTemplateSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1JobTemplateSpec(unittest.TestCase):
    """V1JobTemplateSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1JobTemplateSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_job_template_spec.V1JobTemplateSpec()  # noqa: E501
        if include_optional :
            return V1JobTemplateSpec(
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
                spec = kubernetes.client.models.v1/job_spec.v1.JobSpec(
                    active_deadline_seconds = 56, 
                    backoff_limit = 56, 
                    backoff_limit_per_index = 56, 
                    completion_mode = '0', 
                    completions = 56, 
                    managed_by = '0', 
                    manual_selector = True, 
                    max_failed_indexes = 56, 
                    parallelism = 56, 
                    pod_failure_policy = kubernetes.client.models.v1/pod_failure_policy.v1.PodFailurePolicy(
                        rules = [
                            kubernetes.client.models.v1/pod_failure_policy_rule.v1.PodFailurePolicyRule(
                                action = '0', 
                                on_exit_codes = kubernetes.client.models.v1/pod_failure_policy_on_exit_codes_requirement.v1.PodFailurePolicyOnExitCodesRequirement(
                                    container_name = '0', 
                                    operator = '0', 
                                    values = [
                                        56
                                        ], ), 
                                on_pod_conditions = [
                                    kubernetes.client.models.v1/pod_failure_policy_on_pod_conditions_pattern.v1.PodFailurePolicyOnPodConditionsPattern(
                                        status = '0', 
                                        type = '0', )
                                    ], )
                            ], ), 
                    pod_replacement_policy = '0', 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                        match_expressions = [
                            kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                key = '0', 
                                operator = '0', )
                            ], 
                        match_labels = {
                            'key' : '0'
                            }, ), 
                    success_policy = kubernetes.client.models.v1/success_policy.v1.SuccessPolicy(
                        rules = [
                            kubernetes.client.models.v1/success_policy_rule.v1.SuccessPolicyRule(
                                succeeded_count = 56, 
                                succeeded_indexes = '0', )
                            ], ), 
                    suspend = True, 
                    template = kubernetes.client.models.v1/pod_template_spec.v1.PodTemplateSpec(
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
                            uid = '0', ), ), 
                    ttl_seconds_after_finished = 56, )
            )
        else :
            return V1JobTemplateSpec(
        )

    def testV1JobTemplateSpec(self):
        """Test V1JobTemplateSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
