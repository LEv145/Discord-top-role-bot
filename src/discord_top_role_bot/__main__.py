import hikari

from discord_top_role_bot.config import EnvConfigParser


def main() -> None:
    config = EnvConfigParser(prefix="DTRB").parse()
    bot = hikari.GatewayBot(token=config.bot.token)

    bot.run()


if __name__ == "__main__":
    main()
