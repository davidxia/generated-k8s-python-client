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
from kubernetes.client.models.v1alpha3_resource_claim_template_spec import V1alpha3ResourceClaimTemplateSpec  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha3ResourceClaimTemplateSpec(unittest.TestCase):
    """V1alpha3ResourceClaimTemplateSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha3ResourceClaimTemplateSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha3_resource_claim_template_spec.V1alpha3ResourceClaimTemplateSpec()  # noqa: E501
        if include_optional :
            return V1alpha3ResourceClaimTemplateSpec(
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
                spec = kubernetes.client.models.v1alpha3/resource_claim_spec.v1alpha3.ResourceClaimSpec(
                    controller = '0', 
                    devices = kubernetes.client.models.v1alpha3/device_claim.v1alpha3.DeviceClaim(
                        config = [
                            kubernetes.client.models.v1alpha3/device_claim_configuration.v1alpha3.DeviceClaimConfiguration(
                                opaque = kubernetes.client.models.v1alpha3/opaque_device_configuration.v1alpha3.OpaqueDeviceConfiguration(
                                    driver = '0', 
                                    parameters = kubernetes.client.models.parameters.parameters(), ), 
                                requests = [
                                    '0'
                                    ], )
                            ], 
                        constraints = [
                            kubernetes.client.models.v1alpha3/device_constraint.v1alpha3.DeviceConstraint(
                                match_attribute = '0', )
                            ], 
                        requests = [
                            kubernetes.client.models.v1alpha3/device_request.v1alpha3.DeviceRequest(
                                admin_access = True, 
                                allocation_mode = '0', 
                                count = 56, 
                                device_class_name = '0', 
                                name = '0', 
                                selectors = [
                                    kubernetes.client.models.v1alpha3/device_selector.v1alpha3.DeviceSelector(
                                        cel = kubernetes.client.models.v1alpha3/cel_device_selector.v1alpha3.CELDeviceSelector(
                                            expression = '0', ), )
                                    ], )
                            ], ), )
            )
        else :
            return V1alpha3ResourceClaimTemplateSpec(
                spec = kubernetes.client.models.v1alpha3/resource_claim_spec.v1alpha3.ResourceClaimSpec(
                    controller = '0', 
                    devices = kubernetes.client.models.v1alpha3/device_claim.v1alpha3.DeviceClaim(
                        config = [
                            kubernetes.client.models.v1alpha3/device_claim_configuration.v1alpha3.DeviceClaimConfiguration(
                                opaque = kubernetes.client.models.v1alpha3/opaque_device_configuration.v1alpha3.OpaqueDeviceConfiguration(
                                    driver = '0', 
                                    parameters = kubernetes.client.models.parameters.parameters(), ), 
                                requests = [
                                    '0'
                                    ], )
                            ], 
                        constraints = [
                            kubernetes.client.models.v1alpha3/device_constraint.v1alpha3.DeviceConstraint(
                                match_attribute = '0', )
                            ], 
                        requests = [
                            kubernetes.client.models.v1alpha3/device_request.v1alpha3.DeviceRequest(
                                admin_access = True, 
                                allocation_mode = '0', 
                                count = 56, 
                                device_class_name = '0', 
                                name = '0', 
                                selectors = [
                                    kubernetes.client.models.v1alpha3/device_selector.v1alpha3.DeviceSelector(
                                        cel = kubernetes.client.models.v1alpha3/cel_device_selector.v1alpha3.CELDeviceSelector(
                                            expression = '0', ), )
                                    ], )
                            ], ), ),
        )

    def testV1alpha3ResourceClaimTemplateSpec(self):
        """Test V1alpha3ResourceClaimTemplateSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
