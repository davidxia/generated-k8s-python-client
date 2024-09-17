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
from kubernetes.client.models.v1beta1_validating_admission_policy_binding import V1beta1ValidatingAdmissionPolicyBinding  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1beta1ValidatingAdmissionPolicyBinding(unittest.TestCase):
    """V1beta1ValidatingAdmissionPolicyBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1ValidatingAdmissionPolicyBinding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1beta1_validating_admission_policy_binding.V1beta1ValidatingAdmissionPolicyBinding()  # noqa: E501
        if include_optional :
            return V1beta1ValidatingAdmissionPolicyBinding(
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
                spec = kubernetes.client.models.v1beta1/validating_admission_policy_binding_spec.v1beta1.ValidatingAdmissionPolicyBindingSpec(
                    match_resources = kubernetes.client.models.v1beta1/match_resources.v1beta1.MatchResources(
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
                        object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                        resource_rules = [
                            kubernetes.client.models.v1beta1/named_rule_with_operations.v1beta1.NamedRuleWithOperations(
                                scope = '0', )
                            ], ), 
                    param_ref = kubernetes.client.models.v1beta1/param_ref.v1beta1.ParamRef(
                        name = '0', 
                        namespace = '0', 
                        parameter_not_found_action = '0', 
                        selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), ), 
                    policy_name = '0', 
                    validation_actions = [
                        '0'
                        ], )
            )
        else :
            return V1beta1ValidatingAdmissionPolicyBinding(
        )

    def testV1beta1ValidatingAdmissionPolicyBinding(self):
        """Test V1beta1ValidatingAdmissionPolicyBinding"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
