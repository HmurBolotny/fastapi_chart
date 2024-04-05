from sqlalchemy import text, insert, select

from IMPOC.models import metadata, impoc_val
from database import async_engine, sync_engine


async def get():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")
        conn.commit()


# def insert_val(impoc, hardness):
#     with sync_engine.connect() as conn:
#         stmt = insert(impoc_val).values(
#             [
#                 {"impoc": impoc, "hardness": hardness},
#             ]
#         )
#         conn.execute(stmt)
#         conn.commit()


def insert_val(insert_dict):
    with sync_engine.connect() as conn:
        stmt = insert(impoc_val).values(
            [
                insert_dict,
            ]
        )
        conn.execute(stmt)
        conn.commit()


def select_val():
    with sync_engine.connect() as conn:
        query = select(impoc_val) # SELECT * FROM workers
        result = conn.execute(query)
        impoc = result.all() #
        print(f"{impoc=}")
        print(f"{result.first()=}")


def select_last_val():
    res = None
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM impoc_val WHERE id > (SELECT MAX(id) - 1 FROM impoc_val)"))
        # print("!!!!!!")
        # print(res.all())
        conn.commit()
        # print(type(res))
        # print(type(res.all()))
    return res.all()


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


def ret():
    return 4

