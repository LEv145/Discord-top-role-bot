import hikari

from .config import TomlConfigParser


def main() -> None:
    config = TomlConfigParser(...).parse()  # type: ignore

    bot = hikari.GatewayBot(token=config.bot.token)
    bot.run()


if __name__ == "__main__":
    main()
