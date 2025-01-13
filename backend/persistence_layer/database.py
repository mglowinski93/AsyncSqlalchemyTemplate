from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
