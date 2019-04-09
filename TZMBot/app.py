#!/usr/bin/env python
import datetime
import logging
import logging.config

from discord.ext import commands

from settings import LOGGING, TOKEN
from utils import load_cogs

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    logger.info(f"Bot running on {client.user} (ID: {client.user.id})")
    logger.info(
        f"Took {datetime.datetime.now()-launch_time}, Time now {datetime.datetime.now()}"
    )


if __name__ == "__main__":
    load_cogs(client)
    launch_time = datetime.datetime.now()
    logger.info(f"Attempting to run bot at {launch_time}")
    client.run(TOKEN)
