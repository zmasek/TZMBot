# -*- coding: utf-8 -*-

"""Helper methods for TZMBot."""
import asyncio
import logging
from typing import Iterable, Union

import discord
from discord.ext.commands import Bot

logger = logging.getLogger("__main__")


async def strikethrough(message: discord.Message, new_message: str = ""):
    await message.edit(content=f"~~{message.content}~~\n{new_message}")
    try:
        await message.clear_reactions()
    except discord.Forbidden:
        pass


async def add_many_reactions(
    message: discord.Message,
    *reactions: Iterable[Union[str, discord.Emoji, discord.PartialEmoji]],
):
    for reaction in reactions:
        await message.add_reaction(reaction)
        await asyncio.sleep(0.25)


def load_many_extensions(client: Bot, extensions: Iterable[str]) -> None:
    """Load passed in extensions on a passed in bot.

    Attempts to load each extension in extensions. For each, logs if it succeeded or not.

    :param client: A client that the extensions will be loaded to.
    :type client: Bot
    :param extensions: An iterable of extensions to load
    :type extensions: Iterable[str]
    """
    for extension in extensions:
        try:
            client.load_extension(extension)
            logger.debug(f"-\tCog extension {extension} loaded successfully")
        except Exception as e:
            logger.error(f"-\tCog extension {extension} could not be loaded: {e}")
