import typing as t

from sqlalchemy.sql import sqltypes, schema
from sqlalchemy.orm import declarative_base


Base: t.Any = declarative_base()


class Message(Base):
    __tablename__ = "message"

    id: int = schema.Column(sqltypes.Integer, primary_key=True, autoincrement=True)  # type: ignore
    user_id: int = schema.Column(sqltypes.BigInteger, nullable=False)  # type: ignore
    content: str = schema.Column(sqltypes.String, nullable=False)  # type: ignore
