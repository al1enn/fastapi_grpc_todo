import grpc
from app.pb import todo_pb2, todo_pb2_grpc
from app.models import db_helper
from google.protobuf.empty_pb2 import Empty
from sqlalchemy import text


class TodoServicer(todo_pb2_grpc.TodoServiceServicer):

    async def Create(
        self,
        request: todo_pb2.TodoRequest,
        context: grpc.aio.ServicerContext,
    ) -> todo_pb2.Todo:
        async with db_helper.session_factory() as session:
            query = text(
                """
                   INSERT INTO todo_items (title, description, is_completed, is_important)
                   VALUES (:title, :description, :is_completed, :is_important)
                   RETURNING id, title, description, is_completed, is_important
                   """
            )
            result = await session.execute(
                query,
                {
                    "title": request.title,
                    "description": request.description,
                    "is_completed": request.is_completed,
                    "is_important": request.is_important,
                },
            )

            row = result.mappings().fetchone()
            await session.commit()
            return todo_pb2.Todo(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                is_completed=row["is_completed"],
                is_important=row["is_important"],
            )

    async def Read(
        self,
        request: todo_pb2.TodoRequest,
        context: grpc.aio.ServicerContext,
    ) -> todo_pb2.Todo:
        async with db_helper.session_factory() as session:
            query = text(
                """
            SELECT
                t.id,t.title, t.description, t.is_completed,is_important
            FROM todo_items t
            WHERE t.id = :todo_id
        """
            )
            result = await session.execute(
                query,
                {
                    "todo_id": request.id,
                },
            )

            row = result.mappings().fetchone()
            await session.commit()
            return todo_pb2.Todo(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                is_completed=row["is_completed"],
                is_important=row["is_important"],
            )

    async def Delete(
        self,
        request: todo_pb2.TodoRequest,
        context: grpc.aio.ServicerContext,
    ) -> Empty:
        async with db_helper.session_factory() as session:
            query = text(
                """
            DELETE 
            FROM todo_items t
            WHERE t.id = :todo_id
        """
            )
            await session.execute(
                query,
                {
                    "todo_id": request.id,
                },
            )
            await session.commit()
            return Empty()

    async def List(
        self,
        request: todo_pb2.TodoRequest,
        context: grpc.aio.ServicerContext,
    ) -> todo_pb2.TodoListResponse:
        async with db_helper.session_factory() as session:
            query = text(
                """
                SELECT t.id, t.title, t.description, t.is_completed, t.is_important
                FROM todo_items t
            """
            )
            result = await session.execute(query)
            rows = result.mappings().all()
            await session.commit()

            todos = [
                todo_pb2.Todo(
                    id=todo["id"],
                    title=todo["title"],
                    description=todo["description"],
                    is_completed=todo["is_completed"],
                    is_important=todo["is_important"],
                )
                for todo in rows
            ]
            return todo_pb2.TodoListResponse(
                todos=todos,
            )

    async def Update(
        self,
        request: todo_pb2.TodoRequest,
        context: grpc.aio.ServicerContext,
    ) -> todo_pb2.Todo:
        async with db_helper.session_factory() as session:
            query = text(
                """
                UPDATE todo_items
                SET title = :title,
                    description = :description,
                    is_completed = :is_completed,
                    is_important = :is_important
                WHERE id = :todo_id
                RETURNING id, title, description, is_completed, is_important
            """
            )
            result = await session.execute(
                query,
                {
                    "title": request.title,
                    "description": request.description,
                    "is_completed": request.is_completed,
                    "is_important": request.is_important,
                    "todo_id": request.id,
                },
            )
            row = result.mappings().fetchone()
            await session.commit()
            return todo_pb2.Todo(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                is_completed=row["is_completed"],
                is_important=row["is_important"],
            )
