from fastapi import APIRouter, status
from app.services.todo_client import todo_client
from app.schemas.todo import TodoCreate, TodoUpdate

router = APIRouter()


@router.get("/list")
async def get_todos():
    return await todo_client.get_all()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def create_todo(
    todo_data: TodoCreate,
):
    return await todo_client.create(
        title=todo_data.title,
        description=todo_data.description,
    )


@router.get("/{id}")
async def get_todo(
    id: int,
):
    return await todo_client.get(
        todo_id=id,
    )


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
)
async def update_todo(
    id: int,
    todo_data: TodoUpdate,
):
    return await todo_client.update(
        todo_id=id,
        title=todo_data.title,
        description=todo_data.description,
        is_completed=todo_data.is_completed,
        is_important=todo_data.is_important,
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_todo(
    id: int,
):
    await todo_client.delete(
        todo_id=id,
    )
