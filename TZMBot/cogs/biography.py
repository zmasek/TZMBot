# -*- coding: utf-8 -*-

"""Biography Cog for TZMBot discord.py bot."""
from typing import Optional
from random import choice

import discord
from discord.ext import commands

from TZMBot.models import Biography
from TZMBot.utils import possessive_mention
from TZMBot.settings import EMBED_COLOURS


class Bio(commands.Cog):
    """Biography Cog for TZMBot discord.py bot."""

    def __init__(self, client: commands.Bot) -> None:
        """An initializer for the Biography cog.

        Accepts a client should it needs using it somewhere.

        :param client: A client that the cog is loaded with.
        :type client: Bot
        """
        self.client = client

    async def get_bio(self, pk: str) -> str or None:
        """Attempt to return a biography content from a database.

        It will query a database with a member id and return a content set for it. Failing that, it
        will return None

        :param pk: A string of a member id that the database should filter on.
        :type pk: str
        :returns: A string of a biography content for the given member or None.
        :rtype: str, NoneType
        """
        bio = await Biography.filter(person=pk).first()
        if bio is None:
            return None
        return bio.content

    @commands.command(aliases=["b"])
    async def bio(
        self, ctx: commands.Context, member: discord.Member = None
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

        if bio is None:
            embed = discord.Embed(description=f"{member.mention} has not set a bio.")
        else:
            embed = discord.Embed(description=f"{possessive_mention(member)} bio: {bio}")

        embed.set_thumbnail(url=member.avatar_url)
        embed.colour = choice(EMBED_COLOURS)

        await ctx.send(ctx.author.mention, embed=embed)

    @commands.command(name="setbio", aliases=["sb"])
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

        await ctx.send("Bio set!")

    @commands.command(name="removebio", aliases=["rb"])
    async def remove_bio(self, ctx: commands.Context):
        bio = await Biography.filter(person=ctx.author.id).first()
        await bio.delete()

        await ctx.send("Bio deleted!")


def setup(client: commands.Bot) -> None:
    """Registers the cog with the client given.

    Accepts a client that the cog will be loaded in.

    :param client: A client that the cog is loaded in.
    :type client: Bot
    """
    client.add_cog(Bio(client))
