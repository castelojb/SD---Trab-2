# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from Protobuffer import messages_pb2 as Protobuffer_dot_messages__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class GatewayServiceStub(object):
    """Services definitions
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Identificate = channel.unary_unary(
                '/GatewayService/Identificate',
                request_serializer=Protobuffer_dot_messages__pb2.Identification.SerializeToString,
                response_deserializer=Protobuffer_dot_messages__pb2.Id.FromString,
                )
        self.ReceiveStatus = channel.unary_unary(
                '/GatewayService/ReceiveStatus',
                request_serializer=Protobuffer_dot_messages__pb2.Status.SerializeToString,
                response_deserializer=Protobuffer_dot_messages__pb2.Status.FromString,
                )
        self.EquipmentDied = channel.unary_unary(
                '/GatewayService/EquipmentDied',
                request_serializer=Protobuffer_dot_messages__pb2.Id.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class GatewayServiceServicer(object):
    """Services definitions
    """

    def Identificate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EquipmentDied(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Identificate': grpc.unary_unary_rpc_method_handler(
                    servicer.Identificate,
                    request_deserializer=Protobuffer_dot_messages__pb2.Identification.FromString,
                    response_serializer=Protobuffer_dot_messages__pb2.Id.SerializeToString,
            ),
            'ReceiveStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveStatus,
                    request_deserializer=Protobuffer_dot_messages__pb2.Status.FromString,
                    response_serializer=Protobuffer_dot_messages__pb2.Status.SerializeToString,
            ),
            'EquipmentDied': grpc.unary_unary_rpc_method_handler(
                    servicer.EquipmentDied,
                    request_deserializer=Protobuffer_dot_messages__pb2.Id.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GatewayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GatewayService(object):
    """Services definitions
    """

    @staticmethod
    def Identificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GatewayService/Identificate',
            Protobuffer_dot_messages__pb2.Identification.SerializeToString,
            Protobuffer_dot_messages__pb2.Id.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GatewayService/ReceiveStatus',
            Protobuffer_dot_messages__pb2.Status.SerializeToString,
            Protobuffer_dot_messages__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EquipmentDied(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GatewayService/EquipmentDied',
            Protobuffer_dot_messages__pb2.Id.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class EquipmentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Identificate = channel.unary_unary(
                '/EquipmentService/Identificate',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=Protobuffer_dot_messages__pb2.Identification.FromString,
                )
        self.ReceiveUpdate = channel.unary_unary(
                '/EquipmentService/ReceiveUpdate',
                request_serializer=Protobuffer_dot_messages__pb2.UpdateStatus.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetStatus = channel.unary_unary(
                '/EquipmentService/GetStatus',
                request_serializer=Protobuffer_dot_messages__pb2.FetchStatus.SerializeToString,
                response_deserializer=Protobuffer_dot_messages__pb2.Status.FromString,
                )


class EquipmentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Identificate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReceiveUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EquipmentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Identificate': grpc.unary_unary_rpc_method_handler(
                    servicer.Identificate,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=Protobuffer_dot_messages__pb2.Identification.SerializeToString,
            ),
            'ReceiveUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.ReceiveUpdate,
                    request_deserializer=Protobuffer_dot_messages__pb2.UpdateStatus.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStatus,
                    request_deserializer=Protobuffer_dot_messages__pb2.FetchStatus.FromString,
                    response_serializer=Protobuffer_dot_messages__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EquipmentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EquipmentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Identificate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EquipmentService/Identificate',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            Protobuffer_dot_messages__pb2.Identification.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReceiveUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EquipmentService/ReceiveUpdate',
            Protobuffer_dot_messages__pb2.UpdateStatus.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EquipmentService/GetStatus',
            Protobuffer_dot_messages__pb2.FetchStatus.SerializeToString,
            Protobuffer_dot_messages__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
