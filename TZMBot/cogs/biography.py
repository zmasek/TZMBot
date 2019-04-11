import discord
from discord.ext import commands
from TZMBot.models import Biography


class BiographyCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bio(self, ctx, member: discord.Member):
        bio = await Biography.filter(person=member.id).first()
        if bio is None:
            await ctx.send("No bio set")
        else:
            await ctx.send(bio.content)

    @commands.command()
    async def set_bio(self, ctx, *args):
        bio, _ = await Biography.get_or_create(person=ctx.author.id)
        bio.content = " ".join(args)
        await bio.save()


def setup(client):
    client.add_cog(BiographyCog(client))
