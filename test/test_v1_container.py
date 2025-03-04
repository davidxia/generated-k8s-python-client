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
from kubernetes.client.models.v1_container import V1Container  # noqa: E501
from kubernetes.client.rest import ApiException

class TestV1Container(unittest.TestCase):
    """V1Container unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Container
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubernetes.client.models.v1_container.V1Container()  # noqa: E501
        if include_optional :
            return V1Container(
                args = [
                    '0'
                    ], 
                command = [
                    '0'
                    ], 
                env = [
                    kubernetes.client.models.v1/env_var.v1.EnvVar(
                        name = '0', 
                        value = '0', 
                        value_from = kubernetes.client.models.v1/env_var_source.v1.EnvVarSource(
                            config_map_key_ref = kubernetes.client.models.v1/config_map_key_selector.v1.ConfigMapKeySelector(
                                key = '0', 
                                name = '0', 
                                optional = True, ), 
                            field_ref = kubernetes.client.models.v1/object_field_selector.v1.ObjectFieldSelector(
                                api_version = '0', 
                                field_path = '0', ), 
                            resource_field_ref = kubernetes.client.models.v1/resource_field_selector.v1.ResourceFieldSelector(
                                container_name = '0', 
                                divisor = '0', 
                                resource = '0', ), 
                            secret_key_ref = kubernetes.client.models.v1/secret_key_selector.v1.SecretKeySelector(
                                key = '0', 
                                name = '0', 
                                optional = True, ), ), )
                    ], 
                env_from = [
                    kubernetes.client.models.v1/env_from_source.v1.EnvFromSource(
                        config_map_ref = kubernetes.client.models.v1/config_map_env_source.v1.ConfigMapEnvSource(
                            name = '0', 
                            optional = True, ), 
                        prefix = '0', 
                        secret_ref = kubernetes.client.models.v1/secret_env_source.v1.SecretEnvSource(
                            name = '0', 
                            optional = True, ), )
                    ], 
                image = '0', 
                image_pull_policy = '0', 
                lifecycle = kubernetes.client.models.v1/lifecycle.v1.Lifecycle(
                    post_start = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(
                        exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                            command = [
                                '0'
                                ], ), 
                        http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                            host = '0', 
                            http_headers = [
                                kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                    name = '0', 
                                    value = '0', )
                                ], 
                            path = '0', 
                            port = kubernetes.client.models.port.port(), 
                            scheme = '0', ), 
                        sleep = kubernetes.client.models.v1/sleep_action.v1.SleepAction(
                            seconds = 56, ), 
                        tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                            host = '0', 
                            port = kubernetes.client.models.port.port(), ), ), 
                    pre_stop = kubernetes.client.models.v1/lifecycle_handler.v1.LifecycleHandler(), ), 
                liveness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            '0'
                            ], ), 
                    failure_threshold = 56, 
                    grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                        port = 56, 
                        service = '0', ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '0', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '0', 
                                value = '0', )
                            ], 
                        path = '0', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '0', ), 
                    initial_delay_seconds = 56, 
                    period_seconds = 56, 
                    success_threshold = 56, 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '0', 
                        port = kubernetes.client.models.port.port(), ), 
                    termination_grace_period_seconds = 56, 
                    timeout_seconds = 56, ), 
                name = '0', 
                ports = [
                    kubernetes.client.models.v1/container_port.v1.ContainerPort(
                        container_port = 56, 
                        host_ip = '0', 
                        host_port = 56, 
                        name = '0', 
                        protocol = '0', )
                    ], 
                readiness_probe = kubernetes.client.models.v1/probe.v1.Probe(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            '0'
                            ], ), 
                    failure_threshold = 56, 
                    grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                        port = 56, 
                        service = '0', ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '0', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '0', 
                                value = '0', )
                            ], 
                        path = '0', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '0', ), 
                    initial_delay_seconds = 56, 
                    period_seconds = 56, 
                    success_threshold = 56, 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '0', 
                        port = kubernetes.client.models.port.port(), ), 
                    termination_grace_period_seconds = 56, 
                    timeout_seconds = 56, ), 
                resize_policy = [
                    kubernetes.client.models.v1/container_resize_policy.v1.ContainerResizePolicy(
                        resource_name = '0', 
                        restart_policy = '0', )
                    ], 
                resources = kubernetes.client.models.v1/resource_requirements.v1.ResourceRequirements(
                    claims = [
                        kubernetes.client.models.v1/resource_claim.v1.ResourceClaim(
                            name = '0', 
                            request = '0', )
                        ], 
                    limits = {
                        'key' : '0'
                        }, 
                    requests = {
                        'key' : '0'
                        }, ), 
                restart_policy = '0', 
                security_context = kubernetes.client.models.v1/security_context.v1.SecurityContext(
                    allow_privilege_escalation = True, 
                    app_armor_profile = kubernetes.client.models.v1/app_armor_profile.v1.AppArmorProfile(
                        localhost_profile = '0', 
                        type = '0', ), 
                    capabilities = kubernetes.client.models.v1/capabilities.v1.Capabilities(
                        add = [
                            '0'
                            ], 
                        drop = [
                            '0'
                            ], ), 
                    privileged = True, 
                    proc_mount = '0', 
                    read_only_root_filesystem = True, 
                    run_as_group = 56, 
                    run_as_non_root = True, 
                    run_as_user = 56, 
                    se_linux_options = kubernetes.client.models.v1/se_linux_options.v1.SELinuxOptions(
                        level = '0', 
                        role = '0', 
                        type = '0', 
                        user = '0', ), 
                    seccomp_profile = kubernetes.client.models.v1/seccomp_profile.v1.SeccompProfile(
                        localhost_profile = '0', 
                        type = '0', ), 
                    windows_options = kubernetes.client.models.v1/windows_security_context_options.v1.WindowsSecurityContextOptions(
                        gmsa_credential_spec = '0', 
                        gmsa_credential_spec_name = '0', 
                        host_process = True, 
                        run_as_user_name = '0', ), ), 
                startup_probe = kubernetes.client.models.v1/probe.v1.Probe(
                    exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                        command = [
                            '0'
                            ], ), 
                    failure_threshold = 56, 
                    grpc = kubernetes.client.models.v1/grpc_action.v1.GRPCAction(
                        port = 56, 
                        service = '0', ), 
                    http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                        host = '0', 
                        http_headers = [
                            kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                                name = '0', 
                                value = '0', )
                            ], 
                        path = '0', 
                        port = kubernetes.client.models.port.port(), 
                        scheme = '0', ), 
                    initial_delay_seconds = 56, 
                    period_seconds = 56, 
                    success_threshold = 56, 
                    tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                        host = '0', 
                        port = kubernetes.client.models.port.port(), ), 
                    termination_grace_period_seconds = 56, 
                    timeout_seconds = 56, ), 
                stdin = True, 
                stdin_once = True, 
                termination_message_path = '0', 
                termination_message_policy = '0', 
                tty = True, 
                volume_devices = [
                    kubernetes.client.models.v1/volume_device.v1.VolumeDevice(
                        device_path = '0', 
                        name = '0', )
                    ], 
                volume_mounts = [
                    kubernetes.client.models.v1/volume_mount.v1.VolumeMount(
                        mount_path = '0', 
                        mount_propagation = '0', 
                        name = '0', 
                        read_only = True, 
                        recursive_read_only = '0', 
                        sub_path = '0', 
                        sub_path_expr = '0', )
                    ], 
                working_dir = '0'
            )
        else :
            return V1Container(
                name = '0',
        )

    def testV1Container(self):
        """Test V1Container"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
