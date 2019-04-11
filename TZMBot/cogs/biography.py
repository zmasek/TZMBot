import discord
from discord.ext import commands
from TZMBot.models import Biography


class BiographyCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def get_bio(self, pk):
        bio = await Biography.filter(person=pk).first()
        if bio is None:
            return "No bio set."
        return bio.content

    @commands.command()
    async def bio(self, ctx, member: discord.Member):
        bio = await self.get_bio(member.id)
        await ctx.send(bio)

    @commands.command()
    async def set_bio(self, ctx, *args):
        bio, _ = await Biography.get_or_create(person=ctx.author.id)
        bio.content = " ".join(args)
        await bio.save()


def setup(client):
    client.add_cog(BiographyCog(client))
