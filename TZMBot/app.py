#!/usr/bin/env python
import datetime
import logging
import logging.config
import os

from discord.ext import commands
from settings import BASE_DIR, LOGGING, TOKEN
from tortoise import Tortoise
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


@client.event
async def on_connect():
    await Tortoise.init(
        db_url=f"sqlite://{os.path.join(BASE_DIR, '..', 'db.sqlite')}",
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


@client.event
async def on_disconnect():
    await Tortoise.close_connections()

if __name__ == "__main__":
    load_cogs(client)
    launch_time = datetime.datetime.now()
    logger.info(f"Attempting to run bot at {launch_time}")
    client.run(TOKEN)
