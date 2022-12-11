from __future__ import annotations

import typing as t
from unittest import IsolatedAsyncioTestCase

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from discord_top_role_bot.allocation import (
    SqlalchemyMessagesRepository,
    start_mapper,
    sqlalchemy_metadata,
)

start_mapper()


class SqlalchemyMessagesRepositoryTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        await self.set_up_session()
        self.repository = SqlalchemyMessagesRepository(session=self.session)

    async def asyncTearDown(self) -> None:
        await self.tear_down_session()

    async def set_up_session(self) -> None:
        self.engine = create_async_engine("postgresql+asyncpg://test:test@127.0.0.1:5433/test")
        self.session: AsyncSession = sessionmaker(bind=self.engine, class_=AsyncSession)()

        async with self.engine.begin() as connection:
            await connection.run_sync(sqlalchemy_metadata.create_all)

    async def tear_down_session(self) -> None:
        await self.session.close()

        async with self.engine.begin() as connection:
            await connection.run_sync(sqlalchemy_metadata.drop_all)

        await self.engine.dispose()

    async def test_add(self) -> None:
        ...

    async def test_get(self) -> None:
        ...

    async def test_get_user_top(self) -> None:
        ...
