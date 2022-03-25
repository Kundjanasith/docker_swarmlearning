# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import transport_pb2 as flwr_dot_proto_dot_transport__pb2


class FlowerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Join = channel.stream_stream(
                '/flower.transport.FlowerService/Join',
                request_serializer=flwr_dot_proto_dot_transport__pb2.ClientMessage.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_transport__pb2.ServerMessage.FromString,
                )


class FlowerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Join(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FlowerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Join': grpc.stream_stream_rpc_method_handler(
                    servicer.Join,
                    request_deserializer=flwr_dot_proto_dot_transport__pb2.ClientMessage.FromString,
                    response_serializer=flwr_dot_proto_dot_transport__pb2.ServerMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flower.transport.FlowerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FlowerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Join(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/flower.transport.FlowerService/Join',
            flwr_dot_proto_dot_transport__pb2.ClientMessage.SerializeToString,
            flwr_dot_proto_dot_transport__pb2.ServerMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
