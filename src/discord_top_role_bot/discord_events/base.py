import typing as t
import abc

if t.TYPE_CHECKING:
    from hikari import GatewayBot


class BaseEvent(abc.ABC):
    def __init__(self, bot: GatewayBot) -> None:
        self._bot = bot

    @abc.abstractmethod
    def subscribe(self) -> None:
        pass
