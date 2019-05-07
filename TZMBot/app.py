# -*- coding: utf-8 -*-

"""TZMBot -  A discord.py bot for TZM server."""
import datetime
import logging
import logging.config

from discord.ext import commands
from tortoise import Tortoise

from TZMBot.settings import DATABASE_URL, LOGGING, TOKEN, INIT_EXTENSIONS
from TZMBot.utils import load_many_extensions

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

# Bot configuration options can be passed on the Bot init.
client = commands.Bot(command_prefix="!", case_insensitive=True)


@client.event
async def on_ready() -> None:
    """on_ready event for the TZMBot startup.

    The event logs the time the bot started up.
    """
    logger.info(f"Bot running on {client.user} (ID: {client.user.id})")
    logger.info(
        f"Took {datetime.datetime.now()-launch_time}, Time now {datetime.datetime.now()}"
    )


@client.event
async def on_connect() -> None:
    """on_connect event for the TZMBot startup.

    The event initiates the database connection through the Tortoise ORM and logs if it gets
    connected to the network.
    """
    await Tortoise.init(db_url=DATABASE_URL, modules={"models": ["TZMBot.models"]})
    await Tortoise.generate_schemas()
    logger.info("Connected to the network.")


@client.event
async def on_disconnect() -> None:
    """on_disconnect event for the TZMBot startup.

    The event closes any connections to the database through the Tortoise ORM and logs that it
    disconnected from the network.
    """
    await Tortoise.close_connections()
    logger.info("Disconnected from the network.")


if __name__ == "__main__":
    """If the bot gets called through Python, it will attempt to load any cog extensions it has specified in
    the settings, log it and run the bot application.
    """
    load_many_extensions(client, INIT_EXTENSIONS)
    launch_time = datetime.datetime.now()
    logger.info(f"Attempting to run bot at {launch_time}")
    client.run(TOKEN)
