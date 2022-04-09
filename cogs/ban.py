import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        embed=discord.Embed(description="**User was banned!**", color=0xc79df0)

        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

def setup(client):
    client.add_cog(ban(client))