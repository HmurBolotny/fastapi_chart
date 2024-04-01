from sqlalchemy import text, insert, select

from IMPOC.models import metadata, impoc_val
from database import async_engine, sync_engine


async def get():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")
        conn.commit()


def insert_val():
    with sync_engine.connect() as conn:
        # stmt = """INSERT INTO workers (username) VALUES
        #     ('Jack'),
        #     ('Michael');"""
        stmt = insert(impoc_val).values(
            [
                {"hardness": 12, "impoc": 114},
            ]
        )
        conn.execute(stmt)
        conn.commit()


def select_val():
    with sync_engine.connect() as conn:
        query = select(impoc_val) # SELECT * FROM workers
        result = conn.execute(query)
        workers = result.all()
        print(f"{workers=}")



def create_tables():
    sync_engine.echo = False
    metadata.create_all(sync_engine)
    sync_engine.echo = True


def delete_tables():
    sync_engine.echo = False
    metadata.drop_all(sync_engine)
    sync_engine.echo = True


async def async_create_tables():
    echo = True
    async with async_engine.connect() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
        await conn.commit()


async def async_delete_tables():
    async with async_engine.connect() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.commit()


