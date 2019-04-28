# -*- coding: utf-8 -*-

"""Biography Cog for TZMBot discord.py bot."""
from typing import Optional

import discord
from discord.ext import commands

from TZMBot.models import Biography


class BiographyCog(commands.Cog):
    """Biography Cog for TZMBot discord.py bot."""

    def __init__(self, client: commands.Bot) -> None:
        """An initializer for the Biography cog.

        Accepts a client should it needs using it somewhere.

        :param client: A client that the cog is loaded with.
        :type client: Bot
        """
        self.client = client

    async def get_bio(self, pk: str) -> str:
        """Attempt to return a biography content from a database.

        It will query a database with a member id and return a content set for it. Failing that, it
        will return a string that no biography is set for the member.

        :param pk: A string of a member id that the database should filter on.
        :type pk: str
        :returns: A string of a biography content for the given member or a message without bio set.
        :rtype: str
        """
        bio = await Biography.filter(person=pk).first()
        if bio is None:
            return "No bio set."
        return bio.content

    @commands.command()
    async def bio(
        self, ctx: commands.Context, member: Optional[discord.Member] = None
    ) -> None:
        """A command to get a member biography.

        If no member is given, it will return the biography of a caller if it's set.

        :param ctx: A context of the command call.
        :type ctx: Context
        :param member: (optional) A discord member.
        :type member: Member
        """
        if member is None:
            member = ctx.author
        bio = await self.get_bio(member.id)
        await ctx.send(bio)

    @commands.command()
    async def set_bio(self, ctx: commands.Context, *, member_bio: str) -> None:
        """A command to get a member biography.

        If no member is given, it will return the biography of a caller if it's set.

        :param ctx: A context of the command call.
        :type ctx: Context
        :param member_bio: A biography string to be set for the caller..
        :type member_bio: str
        """
        bio, _ = await Biography.get_or_create(person=ctx.author.id)
        bio.content = member_bio
        await bio.save()


def setup(client: commands.Bot) -> None:
    """Registers the cog with the client given.

    Accepts a client that the cog will be loaded in.

    :param client: A client that the cog is loaded in.
    :type client: Bot
    """
    client.add_cog(BiographyCog(client))
