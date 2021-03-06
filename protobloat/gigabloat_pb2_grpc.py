# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import gigabloat_pb2 as gigabloat__pb2


class GigabloatStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ScanTarget = channel.unary_unary(
            "/gigabloat.Gigabloat/ScanTarget",
            request_serializer=gigabloat__pb2.Target.SerializeToString,
            response_deserializer=gigabloat__pb2.TargetStats.FromString,
        )
        self.GetRoot = channel.unary_unary(
            "/gigabloat.Gigabloat/GetRoot",
            request_serializer=gigabloat__pb2.Target.SerializeToString,
            response_deserializer=gigabloat__pb2.Directory.FromString,
        )


class GigabloatServicer(object):
    """Missing associated documentation comment in .proto file"""

    def ScanTarget(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetRoot(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GigabloatServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ScanTarget": grpc.unary_unary_rpc_method_handler(
            servicer.ScanTarget,
            request_deserializer=gigabloat__pb2.Target.FromString,
            response_serializer=gigabloat__pb2.TargetStats.SerializeToString,
        ),
        "GetRoot": grpc.unary_unary_rpc_method_handler(
            servicer.GetRoot,
            request_deserializer=gigabloat__pb2.Target.FromString,
            response_serializer=gigabloat__pb2.Directory.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "gigabloat.Gigabloat", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Gigabloat(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def ScanTarget(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/gigabloat.Gigabloat/ScanTarget",
            gigabloat__pb2.Target.SerializeToString,
            gigabloat__pb2.TargetStats.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetRoot(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/gigabloat.Gigabloat/GetRoot",
            gigabloat__pb2.Target.SerializeToString,
            gigabloat__pb2.Directory.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
