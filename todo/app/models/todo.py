from app.models import Base
from sqlalchemy import String, Boolean
from sqlalchemy.orm import mapped_column, Mapped


class TodoItem(Base):
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    is_completed: Mapped[bool] = mapped_column(Boolean)
    is_important: Mapped[bool] = mapped_column(Boolean)
