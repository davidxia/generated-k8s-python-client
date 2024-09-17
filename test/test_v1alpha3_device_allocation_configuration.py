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
from kubernetes.client.models.v1alpha3_device_allocation_configuration import V1alpha3DeviceAllocationConfiguration  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha3DeviceAllocationConfiguration(unittest.TestCase):
    """V1alpha3DeviceAllocationConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha3DeviceAllocationConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha3_device_allocation_configuration.V1alpha3DeviceAllocationConfiguration()  # noqa: E501
        if include_optional :
            return V1alpha3DeviceAllocationConfiguration(
                opaque = kubernetes.client.models.v1alpha3/opaque_device_configuration.v1alpha3.OpaqueDeviceConfiguration(
                    driver = '0', 
                    parameters = kubernetes.client.models.parameters.parameters(), ), 
                requests = [
                    '0'
                    ], 
                source = '0'
            )
        else :
            return V1alpha3DeviceAllocationConfiguration(
                source = '0',
        )

    def testV1alpha3DeviceAllocationConfiguration(self):
        """Test V1alpha3DeviceAllocationConfiguration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()