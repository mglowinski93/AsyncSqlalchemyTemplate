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


"""
In an asynchronous application, implicit database activity cannot occur.
To address this, there is a need to set `expire_on_commit=False` on the `async_sessionmaker`
or use `AsyncAttrs` in the base class.

By default, SQLAlchemy attempts to refresh model objects from the database
when their attributes are accessed after a transaction is committed. 

To prevent issues during this process, one of the following solutions is necessary:
1) Setting `expire_on_commit` to False:
This prevents SQLAlchemy from automatically refreshing the object from the database after the transaction is committed.
Manual refreshes must be performed when needed.
2) Using `AsyncAttrs`: This approach awaits querying the database until the object's attributes are accessed,
ensuring compatibility with asynchronous workflows.

Choose the option that best suits your application's requirements to maintain proper behavior in an asynchronous context.

More details can be found here:
https://github.com/sqlalchemy/sqlalchemy/discussions/11495.
"""


@asynccontextmanager
async def get_async_session():
    async with async_sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )() as session:
        try:
            yield session
            await session.commit()
        except Exception as err:
            await session.rollback()
            raise err from err
        finally:
            await session.close()
