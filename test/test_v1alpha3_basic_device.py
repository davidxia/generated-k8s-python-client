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
from kubernetes.client.models.v1alpha3_basic_device import V1alpha3BasicDevice  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1alpha3BasicDevice(unittest.TestCase):
    """V1alpha3BasicDevice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha3BasicDevice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1alpha3_basic_device.V1alpha3BasicDevice()  # noqa: E501
        if include_optional :
            return V1alpha3BasicDevice(
                attributes = {
                    'key' : kubernetes.client.models.v1alpha3/device_attribute.v1alpha3.DeviceAttribute(
                        bool = True, 
                        int = 56, 
                        string = '0', 
                        version = '0', )
                    }, 
                capacity = {
                    'key' : '0'
                    }
            )
        else :
            return V1alpha3BasicDevice(
        )

    def testV1alpha3BasicDevice(self):
        """Test V1alpha3BasicDevice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
