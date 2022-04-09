import discord
from discord.ext import commands

class kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        embed=discord.Embed(description="**User was kicked!**", color=0xc79df0)

        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

def setup(client):
    client.add_cog(kick(client))