import logging
from settings import COGS
import discord

logger = logging.getLogger("__main__")


async def strikethrough(message: discord.Message, new_message: str = ""):
    await message.edit(content=f"~~{message.content}~~ {new_message}")
    try:
        await message.clear_reactions()
    except discord.Forbidden:
        pass


def load_cogs(client):
    for cog in COGS:
        try:
            client.load_extension(cog)
            logger.debug(f"-\tCog extension {cog} loaded successfully")
        except Exception as e:
            logger.error(f"-\tCog extension {cog} could not be loaded: {e}")
