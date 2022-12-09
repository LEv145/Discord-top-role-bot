from __future__ import annotations

import typing as t
import abc


if t.TYPE_CHECKING:
    from ...models import Message


class ABCMessagesRepository(abc.ABC):
    @abc.abstractmethod
    async def add(self, data: Message) -> None:
        pass

    @abc.abstractmethod
    async def get(self) -> Message:
        pass
