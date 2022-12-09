from __future__ import annotations

import typing as t

from sqlalchemy.sql import select

from ..abc import ABCMessagesRepository
from ... import models
from ...adapters import orm

if t.TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class SqlalchemyMessagesRepository(ABCMessagesRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, data: models.Message) -> None:
        message = orm.Message(user_id=data.user_id, content=data.content)
        self._session.add(message)

    async def get(self, user_id: int) -> models.Message:
        sql = select(orm.Message).where(orm.Message.user_id == user_id)
        scalar = await self._session.scalars(sql)
        raw_message: orm.Message = scalar.one()

        return models.Message(user_id=raw_message.user_id, content=raw_message.content)
