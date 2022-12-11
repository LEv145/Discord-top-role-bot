import abc
from dataclasses import dataclass

import dataconf


class ABCConfigParser(abc.ABC):
    @abc.abstractmethod
    def parse(self) -> "BaseConfig":
        pass


class EnvConfigParser(ABCConfigParser):
    def __init__(self, prefix: str) -> None:
        self._prefix = prefix

    def parse(self) -> "BaseConfig":
        return dataconf.env(self._prefix, BaseConfig)


@dataclass
class BotConfig():
    token: str


@dataclass
class BaseConfig():
    bot: BotConfig
