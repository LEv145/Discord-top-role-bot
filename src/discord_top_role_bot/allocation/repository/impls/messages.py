from __future__ import annotations

import typing as t

from sqlalchemy.sql import func, select

from ..abc import ABCMessagesRepository
from ... import models
from ...adapters import orm

if t.TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class SqlalchemyMessagesRepository(ABCMessagesRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add(self, data: models.Message) -> None:
        self._session.add(data)

    async def get(self, user_id: int) -> models.Message:
        sql = orm.message_table.select().where(orm.message_table.c.user_id == user_id)
        scalar = await self._session.scalars(sql)

        return scalar.one()

    async def get_user_top(self, count: int) -> None:
        sql = select(
            orm.message_table.c.user_id,
            func.sum(orm.message_table.c.content),
        ).group_by(orm.message_table.c.user_id)
        scalar = await self._session.scalars(sql)
