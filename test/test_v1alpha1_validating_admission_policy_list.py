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
from kubernetes.client.models.v1alpha1_validating_admission_policy_list import V1alpha1ValidatingAdmissionPolicyList  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha1ValidatingAdmissionPolicyList(unittest.TestCase):
    """V1alpha1ValidatingAdmissionPolicyList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ValidatingAdmissionPolicyList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha1_validating_admission_policy_list.V1alpha1ValidatingAdmissionPolicyList()  # noqa: E501
        if include_optional :
            return V1alpha1ValidatingAdmissionPolicyList(
                api_version = '0', 
                items = [
                    kubernetes.client.models.v1alpha1/validating_admission_policy.v1alpha1.ValidatingAdmissionPolicy(
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
                        spec = kubernetes.client.models.v1alpha1/validating_admission_policy_spec.v1alpha1.ValidatingAdmissionPolicySpec(
                            audit_annotations = [
                                kubernetes.client.models.v1alpha1/audit_annotation.v1alpha1.AuditAnnotation(
                                    key = '0', 
                                    value_expression = '0', )
                                ], 
                            failure_policy = '0', 
                            match_conditions = [
                                kubernetes.client.models.v1alpha1/match_condition.v1alpha1.MatchCondition(
                                    expression = '0', 
                                    name = '0', )
                                ], 
                            match_constraints = kubernetes.client.models.v1alpha1/match_resources.v1alpha1.MatchResources(
                                exclude_resource_rules = [
                                    kubernetes.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
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
                                object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                                resource_rules = [
                                    kubernetes.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
                                        scope = '0', )
                                    ], ), 
                            param_kind = kubernetes.client.models.v1alpha1/param_kind.v1alpha1.ParamKind(
                                api_version = '0', 
                                kind = '0', ), 
                            validations = [
                                kubernetes.client.models.v1alpha1/validation.v1alpha1.Validation(
                                    expression = '0', 
                                    message = '0', 
                                    message_expression = '0', 
                                    reason = '0', )
                                ], 
                            variables = [
                                kubernetes.client.models.v1alpha1/variable.v1alpha1.Variable(
                                    expression = '0', 
                                    name = '0', )
                                ], ), 
                        status = kubernetes.client.models.v1alpha1/validating_admission_policy_status.v1alpha1.ValidatingAdmissionPolicyStatus(
                            conditions = [
                                kubernetes.client.models.v1/condition.v1.Condition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 56, 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, 
                            type_checking = kubernetes.client.models.v1alpha1/type_checking.v1alpha1.TypeChecking(
                                expression_warnings = [
                                    kubernetes.client.models.v1alpha1/expression_warning.v1alpha1.ExpressionWarning(
                                        field_ref = '0', 
                                        warning = '0', )
                                    ], ), ), )
                    ], 
                kind = '0', 
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '0', 
                    remaining_item_count = 56, 
                    resource_version = '0', 
                    self_link = '0', )
            )
        else :
            return V1alpha1ValidatingAdmissionPolicyList(
                items = [
                    kubernetes.client.models.v1alpha1/validating_admission_policy.v1alpha1.ValidatingAdmissionPolicy(
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
                        spec = kubernetes.client.models.v1alpha1/validating_admission_policy_spec.v1alpha1.ValidatingAdmissionPolicySpec(
                            audit_annotations = [
                                kubernetes.client.models.v1alpha1/audit_annotation.v1alpha1.AuditAnnotation(
                                    key = '0', 
                                    value_expression = '0', )
                                ], 
                            failure_policy = '0', 
                            match_conditions = [
                                kubernetes.client.models.v1alpha1/match_condition.v1alpha1.MatchCondition(
                                    expression = '0', 
                                    name = '0', )
                                ], 
                            match_constraints = kubernetes.client.models.v1alpha1/match_resources.v1alpha1.MatchResources(
                                exclude_resource_rules = [
                                    kubernetes.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
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
                                object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                                resource_rules = [
                                    kubernetes.client.models.v1alpha1/named_rule_with_operations.v1alpha1.NamedRuleWithOperations(
                                        scope = '0', )
                                    ], ), 
                            param_kind = kubernetes.client.models.v1alpha1/param_kind.v1alpha1.ParamKind(
                                api_version = '0', 
                                kind = '0', ), 
                            validations = [
                                kubernetes.client.models.v1alpha1/validation.v1alpha1.Validation(
                                    expression = '0', 
                                    message = '0', 
                                    message_expression = '0', 
                                    reason = '0', )
                                ], 
                            variables = [
                                kubernetes.client.models.v1alpha1/variable.v1alpha1.Variable(
                                    expression = '0', 
                                    name = '0', )
                                ], ), 
                        status = kubernetes.client.models.v1alpha1/validating_admission_policy_status.v1alpha1.ValidatingAdmissionPolicyStatus(
                            conditions = [
                                kubernetes.client.models.v1/condition.v1.Condition(
                                    last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    message = '0', 
                                    observed_generation = 56, 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            observed_generation = 56, 
                            type_checking = kubernetes.client.models.v1alpha1/type_checking.v1alpha1.TypeChecking(
                                expression_warnings = [
                                    kubernetes.client.models.v1alpha1/expression_warning.v1alpha1.ExpressionWarning(
                                        field_ref = '0', 
                                        warning = '0', )
                                    ], ), ), )
                    ],
        )

    def testV1alpha1ValidatingAdmissionPolicyList(self):
        """Test V1alpha1ValidatingAdmissionPolicyList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
