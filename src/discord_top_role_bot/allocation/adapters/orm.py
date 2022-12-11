from __future__ import annotations

import typing as t

from sqlalchemy.orm import mapper
from sqlalchemy.sql import sqltypes, schema

from .. import models


sqlalchemy_metadata = schema.MetaData()
message_table = schema.Table(
    "message",
    sqlalchemy_metadata,
    schema.Column("id", sqltypes.Integer, primary_key=True, autoincrement=True),
    schema.Column("user_id", sqltypes.BigInteger, nullable=False),
    schema.Column("content", sqltypes.String, nullable=False),
)


def start_mapper() -> None:  # TODO: Maybe autorun
    mapper(models.Message, message_table)
