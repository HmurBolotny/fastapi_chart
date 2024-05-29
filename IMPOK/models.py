from sqlalchemy import MetaData, String, TIMESTAMP, ForeignKey, Table, Column, Integer, JSON, Float

metadata = MetaData()

impoc_val = Table(
    "impoc_val",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("hardness", Float, nullable=False),
    Column("impoc", Integer, nullable=False),
)
