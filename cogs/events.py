import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))
        print(f'[Discord API] Connected To [{self.client.user}]')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(description='**You do not have permission to use that command!**', color=0xc79df0)

            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed=discord.Embed(description='**That command was not found!**', color=0xc79df0)

            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

def setup(client):
    client.add_cog(events(client))