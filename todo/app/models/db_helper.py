from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from collections.abc import AsyncGenerator

from app.core.config import DB_URL


class DbHelper:
    def __init__(
        self,
        url: str,
        pool_size: int = 5,
        max_overflow: int = 10,
        echo: bool = True,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            pool_size=pool_size,
            max_overflow=max_overflow,
            echo=echo,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
            autocommit=False,
        )

    async def close(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DbHelper(
    url=str(DB_URL),
)
