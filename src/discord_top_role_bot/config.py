import abc
from dataclasses import dataclass
from pathlib import Path

import toml
import dataconf


class ABCConfigParser(abc.ABC):
    @abc.abstractmethod
    def parse(self) -> "BaseConfig":
        pass


class TomlConfigParser(ABCConfigParser):
    def __init__(self, path: Path) -> None:
        self._path = path

    def parse(self) -> "BaseConfig":
        data = toml.load(self._path)
        config: BaseConfig = dataconf.dict(data, BaseConfig)  # type: ignore
        return config


@dataclass
class BotConfig():
    token: str


@dataclass
class BaseConfig():
    bot: BotConfig
