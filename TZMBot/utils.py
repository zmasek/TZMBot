# -*- coding: utf-8 -*-

"""Helper methods for TZMBot."""
import logging

import discord
from discord.ext.commands import Bot


from TZMBot.settings import COGS

logger = logging.getLogger("__main__")


async def strikethrough(message: discord.Message, new_message: str = ""):
    await message.edit(content=f"~~{message.content}~~ {new_message}")
    try:
        await message.clear_reactions()
    except discord.Forbidden:
        pass


def load_cogs(client: Bot) -> None:
    """Load extensions for a passed in bot.

    Loads extensions defined in the settings. For each extension logs if it succeeded or not.

    :param client: A client that the cogs will be loaded to.
    :type client: Bot
    """
    for cog in COGS:
        try:
            client.load_extension(cog)
            logger.debug(f"-\tCog extension {cog} loaded successfully")
        except Exception as e:
            logger.error(f"-\tCog extension {cog} could not be loaded: {e}")
