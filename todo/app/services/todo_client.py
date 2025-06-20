import grpc
from google.protobuf.json_format import MessageToDict
from app.core.config import GRPC_TODO, GRPC_SERVER_PORT
from app.pb import todo_pb2_grpc, todo_pb2


class TodoClient(object):
    def __init__(self):
        self.channel = grpc.aio.insecure_channel(f"{GRPC_TODO}:{GRPC_SERVER_PORT}")
        self.stub = todo_pb2_grpc.TodoServiceStub(self.channel)

    async def create(
        self,
        title: str,
        description: str,
    ):
        todo_request = todo_pb2.Todo(
            title=title,
            description=description,
        )
        todo_response: todo_pb2.Todo = await self.stub.Create(
            todo_request,
        )
        return MessageToDict(todo_response)

    async def get(
        self,
        todo_id: int,
    ):
        todo_request = todo_pb2.Todo(
            id=todo_id,
        )
        todo_response: todo_pb2.Todo = await self.stub.Read(
            todo_request,
        )
        return MessageToDict(todo_response)

    async def update(
        self,
        todo_id: int,
        title: str,
        description: str,
        is_completed: bool,
        is_important: bool,
    ):
        todo_request = todo_pb2.Todo(
            id=todo_id,
            title=title,
            description=description,
            is_completed=is_completed,
            is_important=is_important,
        )
        todo_response: todo_pb2.Todo = await self.stub.Update(
            todo_request,
        )
        return MessageToDict(todo_response)

    async def delete(
        self,
        todo_id: int,
    ):
        todo_request = todo_pb2.Todo(
            id=todo_id,
        )
        todo_response: todo_pb2.Todo = await self.stub.Delete(
            todo_request,
        )
        return todo_response

    async def get_all(
        self,
    ):
        todos_response = await self.stub.List(todo_pb2.Todo())
        return MessageToDict(todos_response)


todo_client = TodoClient()
