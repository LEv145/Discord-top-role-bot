import typing as t

if t.TYPE_CHECKING:
    from hikari import GatewayBot


class BaseEvent():
    def __init__(self, bot: GatewayBot) -> None:
        self._bot = bot
