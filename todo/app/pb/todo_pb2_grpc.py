# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from app.pb import todo_pb2 as todo__pb2

GRPC_GENERATED_VERSION = "1.73.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in todo_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
            "/todo.TodoService/Create",
            request_serializer=todo__pb2.TodoRequest.SerializeToString,
            response_deserializer=todo__pb2.Todo.FromString,
            _registered_method=True,
        )
        self.Read = channel.unary_unary(
            "/todo.TodoService/Read",
            request_serializer=todo__pb2.TodoRequest.SerializeToString,
            response_deserializer=todo__pb2.Todo.FromString,
            _registered_method=True,
        )
        self.Update = channel.unary_unary(
            "/todo.TodoService/Update",
            request_serializer=todo__pb2.TodoRequest.SerializeToString,
            response_deserializer=todo__pb2.Todo.FromString,
            _registered_method=True,
        )
        self.Delete = channel.unary_unary(
            "/todo.TodoService/Delete",
            request_serializer=todo__pb2.TodoRequest.SerializeToString,
            response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            _registered_method=True,
        )
        self.List = channel.unary_unary(
            "/todo.TodoService/List",
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=todo__pb2.TodoListResponse.FromString,
            _registered_method=True,
        )


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=todo__pb2.TodoRequest.FromString,
            response_serializer=todo__pb2.Todo.SerializeToString,
        ),
        "Read": grpc.unary_unary_rpc_method_handler(
            servicer.Read,
            request_deserializer=todo__pb2.TodoRequest.FromString,
            response_serializer=todo__pb2.Todo.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=todo__pb2.TodoRequest.FromString,
            response_serializer=todo__pb2.Todo.SerializeToString,
        ),
        "Delete": grpc.unary_unary_rpc_method_handler(
            servicer.Delete,
            request_deserializer=todo__pb2.TodoRequest.FromString,
            response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        ),
        "List": grpc.unary_unary_rpc_method_handler(
            servicer.List,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=todo__pb2.TodoListResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "todo.TodoService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("todo.TodoService", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(
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
            "/todo.TodoService/Create",
            todo__pb2.TodoRequest.SerializeToString,
            todo__pb2.Todo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Read(
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
            "/todo.TodoService/Read",
            todo__pb2.TodoRequest.SerializeToString,
            todo__pb2.Todo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Update(
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
            "/todo.TodoService/Update",
            todo__pb2.TodoRequest.SerializeToString,
            todo__pb2.Todo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def Delete(
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
            "/todo.TodoService/Delete",
            todo__pb2.TodoRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def List(
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
            "/todo.TodoService/List",
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            todo__pb2.TodoListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
