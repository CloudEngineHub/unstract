# flake8: noqa
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

from . import evaluation_pb2 as evaluation__pb2


class EvaluationServiceStub:
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Boolean = channel.unary_unary(
            "/flipt.evaluation.EvaluationService/Boolean",
            request_serializer=evaluation__pb2.EvaluationRequest.SerializeToString,
            response_deserializer=evaluation__pb2.BooleanEvaluationResponse.FromString,
        )
        self.Variant = channel.unary_unary(
            "/flipt.evaluation.EvaluationService/Variant",
            request_serializer=evaluation__pb2.EvaluationRequest.SerializeToString,
            response_deserializer=evaluation__pb2.VariantEvaluationResponse.FromString,
        )
        self.Batch = channel.unary_unary(
            "/flipt.evaluation.EvaluationService/Batch",
            request_serializer=evaluation__pb2.BatchEvaluationRequest.SerializeToString,
            response_deserializer=evaluation__pb2.BatchEvaluationResponse.FromString,
        )


class EvaluationServiceServicer:
    """Missing associated documentation comment in .proto file."""

    def Boolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Variant(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Batch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_EvaluationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Boolean": grpc.unary_unary_rpc_method_handler(
            servicer.Boolean,
            request_deserializer=evaluation__pb2.EvaluationRequest.FromString,
            response_serializer=evaluation__pb2.BooleanEvaluationResponse.SerializeToString,
        ),
        "Variant": grpc.unary_unary_rpc_method_handler(
            servicer.Variant,
            request_deserializer=evaluation__pb2.EvaluationRequest.FromString,
            response_serializer=evaluation__pb2.VariantEvaluationResponse.SerializeToString,
        ),
        "Batch": grpc.unary_unary_rpc_method_handler(
            servicer.Batch,
            request_deserializer=evaluation__pb2.BatchEvaluationRequest.FromString,
            response_serializer=evaluation__pb2.BatchEvaluationResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "flipt.evaluation.EvaluationService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class EvaluationService:
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Boolean(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/flipt.evaluation.EvaluationService/Boolean",
            evaluation__pb2.EvaluationRequest.SerializeToString,
            evaluation__pb2.BooleanEvaluationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Variant(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/flipt.evaluation.EvaluationService/Variant",
            evaluation__pb2.EvaluationRequest.SerializeToString,
            evaluation__pb2.VariantEvaluationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Batch(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/flipt.evaluation.EvaluationService/Batch",
            evaluation__pb2.BatchEvaluationRequest.SerializeToString,
            evaluation__pb2.BatchEvaluationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
