import datetime
import enum

from typing import Annotated, Optional
from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    Float,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)


from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]



class MarkDescription(Base):
    __tablename__ = 'mark_descr'

    id_mark: Mapped[intpk]
    name_mark: Mapped[str_256]
    description: Mapped[str_256] = mapped_column(nullable=True)

    # mark_coeff: Mapped[list["MarkCoefficient"]] = relationship()    #если связь o2m
    mark_coeff: Mapped["MarkCoefficient"] = relationship()          #если o2o, m2o
    lab_coeff: Mapped["LaboratoryCoefficient"] = relationship()
    impok_data: Mapped[list["ImpokData"]] = relationship(           #атрибут ссылается на таюлицу ImpokData
        back_populates="mark_descr",                                 #на атрибут mark_descer
       # backref ="mark_descr"                                      # аналогично back_populate неявно
        # создает атрибут  mark_descr , устаревший вариант
        #primaryjoin=" MarkDescription.id_mark == ImpokData.id_mark" #дефолтный join его бы писали для sql запроса т егоформирует алхимия
        #primaryjoin="and_MarkDescription.id_mark == ImpokData.id_mark, ImpokData.>3" #модернизированный join  допуслови среднеее imp больше 3
    )


# #насклько целесообразно вводить такую сущность
# class MarkRoll(Base):
#     __tablename__ = 'mark_roll'
#
#     #будет ли id_roll уникальным?
#     id_roll: Mapped[intpk]
#     id_mark: Mapped[int] = mapped_column(ForeignKey("mark_descr.id_mark"))


class MarkCoefficient(Base):
    __tablename__ = 'mark_coeff'

    id_coeff: Mapped[intpk]
    id_mark: Mapped[int] = mapped_column(ForeignKey("mark_descr.id_mark"))
    coeff_1: Mapped[float]
    coeff_2: Mapped[float]
    coeff_3: Mapped[float]
    data: Mapped[updated_at]    # crate_at or update_at  она обнавляеться ил добавляется новая запись

    repr_cols_num = 5
    repr_cols = {"data"}



# class CalculateCoefficient(Base):
#     __tablename__ = "calc_coeff"
#
#     id_mark: Mapped[int]    # primary key & fornge key
#     coeff_1: Mapped[float]
#     coeff_2: Mapped[float]
#     coeff_3: Mapped[float]
#     data: Mapped[created_at]    # crate_at or update_at  она обнавляеться ил добавляется новая запись
#     calculate coef  не имеет своего собственного ключа и содержит расчетные коэффициенты потому имеет смысл отнести все в  description

class LaboratoryCoefficient(Base):
    __tablename__ = "lab_coeff"
#   нужно хранить старые данные по лабораторным исследованиям если нет, то надо обединить с CalculateCoefficient(MarkDescription)?????

    id_lab: Mapped[intpk]
    id_roll: Mapped[int] = mapped_column(ForeignKey("impok_data.id_roll"))
    id_mark: Mapped[int] = mapped_column(ForeignKey("mark_descr.id_mark"))
    imp_1: Mapped[float]
    imp_2: Mapped[float]
    imp_3: Mapped[float]
    data: Mapped[created_at]

    repr_cols_num = 6
    repr_cols = {"data"}



class ImpokData(Base):
    __tablename__ = "impok_data"

    id_roll: Mapped[intpk]
    id_mark: Mapped[int] = mapped_column(ForeignKey("mark_descr.id_mark"))          # foreign key MarkDescription
    imp_min: Mapped[float]
    imp_ave: Mapped[float]
    imp_max: Mapped[float]            # min ave max  может быть float???
    calc_val_1: Mapped[float]
    calc_val_2: Mapped[float]
    calc_val_3: Mapped[float]
    date: Mapped[created_at]

    mark_descr: Mapped["MarkDescription"] = relationship(
        back_populates="impok_data"
    )

    repr_cols_num = 8
    repr_cols = {"data"}




class ImpokTrand(Base):
    __tablename__ = "impok_trand"

    id_trand: Mapped[intpk]
    id_roll: Mapped[int] = mapped_column(ForeignKey("impok_data.id_roll",))           # foreign key impok data
    imp: Mapped[float]
    data: Mapped[created_at]
