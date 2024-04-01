import asyncio

from sqlalchemy import text, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta, sessionmaker

DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#Base: DeclarativeMeta = declarative_base()


sync_engine = create_engine(
    url=DATABASE_URL,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)


async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10
)


session_maker = sessionmaker(sync_engine)
async_session_maker = async_sessionmaker(async_engine)


# asyncio.run(get())
