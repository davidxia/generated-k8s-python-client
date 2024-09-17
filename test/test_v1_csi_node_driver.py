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
from kubernetes.client.models.v1_csi_node_driver import V1CSINodeDriver  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1CSINodeDriver(unittest.TestCase):
    """V1CSINodeDriver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CSINodeDriver
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_csi_node_driver.V1CSINodeDriver()  # noqa: E501
        if include_optional :
            return V1CSINodeDriver(
                allocatable = kubernetes.client.models.v1/volume_node_resources.v1.VolumeNodeResources(
                    count = 56, ), 
                name = '0', 
                node_id = '0', 
                topology_keys = [
                    '0'
                    ]
            )
        else :
            return V1CSINodeDriver(
                name = '0',
                node_id = '0',
        )

    def testV1CSINodeDriver(self):
        """Test V1CSINodeDriver"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()