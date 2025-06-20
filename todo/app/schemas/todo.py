from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str
    is_completed: bool
    is_important: bool


class TodoCreate(TodoBase):
    pass


class TodoRead(TodoBase):
    id: int


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
    is_important: bool | None = None
