import typing as t

from hikari import GuildMessageCreateEvent

from ..base import BaseEvent

if t.TYPE_CHECKING:
    from hikari import GatewayBot

    from discord_top_role_bot.allocation import ABCMessagesRepository, Message


class MessageLoggerEvent(BaseEvent):
    def __init__(self, bot: GatewayBot, message_repository: ABCMessagesRepository) -> None:
        super().__init__(bot=bot)

        self._message_repository = message_repository

    def subscribe(self) -> None:
        self._bot.subscribe(GuildMessageCreateEvent, self._on_message)

    async def _on_message(self, event: GuildMessageCreateEvent) -> None:
        if not event.is_human or event.message.content is None:
            return

        await self._message_repository.add(
            Message(content=event.message.content, user_id=event.author_id),
        )
