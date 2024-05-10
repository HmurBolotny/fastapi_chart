"""
описывается интерфейс для работы с базой данных

функции:
создание подключения
создание таблици
удаление таблици
создание записи
узаленеи записи
чтение записи

выполнить синхронный и асинхронный метод
"""
from sqlalchemy import text, insert, select

from IMPOC.models import metadata, impoc_val
from db.database import async_engine, sync_engine


class SyncRepo:
    def create_tables(self):
        sync_engine.echo = False
        metadata.create_all(sync_engine)
        sync_engine.echo = True

    def delet_tabeles(self):
        sync_engine.echo = False
        metadata.drop_all(sync_engine)
        sync_engine.echo = True

    def insert_val(self, insert_dict):
        with sync_engine.connect() as conn:
            stmt = insert(impoc_val).values(
                [
                    insert_dict,
                ]
            )
            conn.execute(stmt)
            conn.commit()

    def select_val(self):
        with sync_engine.connect() as conn:
            query = select(impoc_val)  # SELECT * FROM workers
            result = conn.execute(query)
            return result.all()  #

    def select_last_val(self):
        res = None
        with sync_engine.connect() as conn:
            res = conn.execute(text("SELECT * FROM impoc_val WHERE id > (SELECT MAX(id) - 1 FROM impoc_val)"))
            conn.commit()
        return res.all()





async def get():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.all()=}")
        conn.commit()


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
        query = select(impoc_val)  # SELECT * FROM workers
        result = conn.execute(query)
        impoc = result.all()  #
        print(f"{impoc=}")
        print(f"{result.first()=}")


def select_last_val():
    res = None
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT * FROM impoc_val WHERE id > (SELECT MAX(id) - 1 FROM impoc_val)"))
        conn.commit()
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

