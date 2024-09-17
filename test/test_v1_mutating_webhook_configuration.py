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
from kubernetes.client.models.v1_mutating_webhook_configuration import V1MutatingWebhookConfiguration  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1MutatingWebhookConfiguration(unittest.TestCase):
    """V1MutatingWebhookConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1MutatingWebhookConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_mutating_webhook_configuration.V1MutatingWebhookConfiguration()  # noqa: E501
        if include_optional :
            return V1MutatingWebhookConfiguration(
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
                webhooks = [
                    kubernetes.client.models.v1/mutating_webhook.v1.MutatingWebhook(
                        admission_review_versions = [
                            '0'
                            ], 
                        kubernetes.client_config = kubernetes.client.models.admissionregistration/v1/webhook_client_config.admissionregistration.v1.WebhookClientConfig(
                            ca_bundle = 'YQ==', 
                            service = kubernetes.client.models.admissionregistration/v1/service_reference.admissionregistration.v1.ServiceReference(
                                name = '0', 
                                namespace = '0', 
                                path = '0', 
                                port = 56, ), 
                            url = '0', ), 
                        failure_policy = '0', 
                        match_conditions = [
                            kubernetes.client.models.v1/match_condition.v1.MatchCondition(
                                expression = '0', 
                                name = '0', )
                            ], 
                        match_policy = '0', 
                        name = '0', 
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
                        reinvocation_policy = '0', 
                        rules = [
                            kubernetes.client.models.v1/rule_with_operations.v1.RuleWithOperations(
                                api_groups = [
                                    '0'
                                    ], 
                                api_versions = [
                                    '0'
                                    ], 
                                operations = [
                                    '0'
                                    ], 
                                resources = [
                                    '0'
                                    ], 
                                scope = '0', )
                            ], 
                        side_effects = '0', 
                        timeout_seconds = 56, )
                    ]
            )
        else :
            return V1MutatingWebhookConfiguration(
        )

    def testV1MutatingWebhookConfiguration(self):
        """Test V1MutatingWebhookConfiguration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
