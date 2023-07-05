import os
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_async_engine(
    DATABASE_URL,
    future=True,
)


@asynccontextmanager
async def get_async_session():
    async with async_sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
