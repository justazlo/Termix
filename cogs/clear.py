import discord
from discord.ext import commands

class clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(description=f"**Purged {amount} messages!**", color=0xc79df0)

        await ctx.send(embed=embed, delete_after=5)
        await ctx.message.delete()

def setup(client):
    client.add_cog(clear(client))