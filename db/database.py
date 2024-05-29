from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, String

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

from config import settings


database_url_sync = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
database_url_async = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


sync_engine = create_engine(
    url=database_url_sync,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


async_engine = create_async_engine(
    url=database_url_async,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)

def get_version():
    with engine.connect() as conn:
        res = conn.execute(text("select version()"))
        print(f"{res.first()=}")


sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


str_256 = Annotated[str, 256]


class Base(DeclarativeBase):            # базовый каласс от которого наследуемвсеклассымодели  содержит в себе методанные
    # всех потомков
    type_annotiation_map = {
        str_256: String(256)
    }

    #получение конкретных значений из модели
    # делает вывод данных читаемым , в противном случае показывает тип данных и указатель на ячейку памяти
    # def __repr__(self):
    #     cols = []                                            # пустой список под все столбцы
    #     for col in self.__table__.columns.keys():               # перибераем все начения столбцов в таблице
    #         cols.append(f"{col}={getattr(self, col)}")          # добавление id колонки = значение колонки (возвращается методом getattr)
    #     return f"<{self.__class__.__name__}{','.join(cols)}>"   # возвращаем собственное значение  и соединяем со списком значений



    # доработанная функция
    repr_cols_num = 3       # количество первых столбцов к выводу
    repr_cols = tuple()     # кортеж  дополнительных столбцоа
    # можно ли сделать исключение каких либо столбцов

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"
