# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Protobuffer import messages_pb2 as Protobuffer_dot_messages__pb2


class ExampleServiceStub(object):
    """Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetId = channel.unary_unary(
                '/ExampleService/GetId',
                request_serializer=Protobuffer_dot_messages__pb2.Identification.SerializeToString,
                response_deserializer=Protobuffer_dot_messages__pb2.Identification.FromString,
                )


class ExampleServiceServicer(object):
    """Service definition
    """

    def GetId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExampleServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetId,
                    request_deserializer=Protobuffer_dot_messages__pb2.Identification.FromString,
                    response_serializer=Protobuffer_dot_messages__pb2.Identification.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ExampleService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ExampleService(object):
    """Service definition
    """

    @staticmethod
    def GetId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ExampleService/GetId',
            Protobuffer_dot_messages__pb2.Identification.SerializeToString,
            Protobuffer_dot_messages__pb2.Identification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
