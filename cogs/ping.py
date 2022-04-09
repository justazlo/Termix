import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed(description=f'**SPEED:** {round(self.client.latency * 1000)}', color=0xc79df0)

        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

def setup(client):
    client.add_cog(ping(client))