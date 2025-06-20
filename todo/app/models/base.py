from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declared_attr,
    mapped_column,
)

from app.utils.case_converter import convert_and_pluralize


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{convert_and_pluralize(cls.__name__)}"

    id: Mapped[int] = mapped_column(primary_key=True)
