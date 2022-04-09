import discord
from discord.ext import commands

class info(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def info(self, ctx):
        servercount = str(len(self.client.guilds))
        embed=discord.Embed(title='Info!', color=0xc79df0)
        embed.add_field(name='Creator!', value='Azlo/Kimble!', inline=False)
        embed.add_field(name='Purpose!', value='Moderation!', inline=False)
        embed.add_field(name='System!', value='GNU/Linux', inline=False)
        embed.add_field(name='Server Count!', value=f'Im in {servercount} guilds!', inline=False)

        await ctx.send(embed=embed, delete_after=60)
        await ctx.message.delete()    

def setup(client):
    client.add_cog(info(client))