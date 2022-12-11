from __future__ import annotations

import typing as t

from async_scheduler_object import AsyncSchedulerEvent

if t.TYPE_CHECKING:
    from hikari import GatewayBot
    from discord_top_role_bot.allocation import ABCMessagesRepository


class UpdateDiscordRoles(AsyncSchedulerEvent):
    def __init__(
        self,
        bot: GatewayBot,
        message_repository: ABCMessagesRepository,
        guild_id: int,
        role_id: int,
        top_count: int,
    ) -> None:
        self._bot = bot
        self._message_repository = message_repository
        self._guild_id = guild_id
        self._role_id = role_id
        self._top_count = top_count

    async def run(self) -> None:
        self._bot
