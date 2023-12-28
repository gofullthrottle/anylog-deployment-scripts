# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import kvm_pb2 as kvm__pb2


class KVMStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registerAgentIdentity = channel.unary_unary(
                '/kvm.KVM/registerAgentIdentity',
                request_serializer=kvm__pb2.agentIdentity.SerializeToString,
                response_deserializer=kvm__pb2.status.FromString,
                )
        self.sendPolicy = channel.stream_stream(
                '/kvm.KVM/sendPolicy',
                request_serializer=kvm__pb2.status.SerializeToString,
                response_deserializer=kvm__pb2.policyData.FromString,
                )


class KVMServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registerAgentIdentity(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendPolicy(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KVMServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registerAgentIdentity': grpc.unary_unary_rpc_method_handler(
                    servicer.registerAgentIdentity,
                    request_deserializer=kvm__pb2.agentIdentity.FromString,
                    response_serializer=kvm__pb2.status.SerializeToString,
            ),
            'sendPolicy': grpc.stream_stream_rpc_method_handler(
                    servicer.sendPolicy,
                    request_deserializer=kvm__pb2.status.FromString,
                    response_serializer=kvm__pb2.policyData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kvm.KVM', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KVM(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registerAgentIdentity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kvm.KVM/registerAgentIdentity',
            kvm__pb2.agentIdentity.SerializeToString,
            kvm__pb2.status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendPolicy(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/kvm.KVM/sendPolicy',
            kvm__pb2.status.SerializeToString,
            kvm__pb2.policyData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
