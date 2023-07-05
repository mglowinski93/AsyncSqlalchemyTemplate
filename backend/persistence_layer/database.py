from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
