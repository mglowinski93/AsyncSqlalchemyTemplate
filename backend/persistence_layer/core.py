import os
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}"
    f"@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/"
    f"{os.environ['DATABASE_NAME']}"
)
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
