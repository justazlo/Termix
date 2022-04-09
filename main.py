import discord, config, os
from discord.ext import commands

client = commands.Bot(command_prefix=config.prefix)
client.remove_command('help')

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 921462013157326899:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'**Loaded "{extension}"**', delete_after=5)
        await ctx.message.delete()
    else:
        await ctx.send("**You're not allowed to use that!**", delete_after=5)
        await ctx.message.delete()

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 921462013157326899:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'**Unloaded "{extension}"**', delete_after=5)
        await ctx.message.delete()
    else:
        await ctx.send("**You're not allowed to use that!**", delete_after=5)
        await ctx.message.delete()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(config.auth_token)