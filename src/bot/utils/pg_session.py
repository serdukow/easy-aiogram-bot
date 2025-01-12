from contextlib import asynccontextmanager

from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.bot.utils.postgres_settings import get_pg_settings


async_url = get_pg_settings().async_url
engine = create_async_engine(async_url,
                             pool_pre_ping=True,
                             poolclass=AsyncAdaptedQueuePool,
                             pool_size=1,
                             max_overflow=1)
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


@asynccontextmanager
async def get_pg_session() -> AsyncSession:
    session = session_maker()
    async with session.begin():
        yield session


async def shutdown() -> None:
    if engine is not None:
        await engine.dispose()
