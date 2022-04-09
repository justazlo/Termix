import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help!", color=0xc79df0)
        embed.add_field(name="$info", value="Shows information about termix!", inline=False)
        embed.add_field(name="$ping", value="Shows server speed/ping!", inline=False)
        embed.add_field(name="$ban", value="EX. $ban [USER] [REASON]", inline=False)
        embed.add_field(name="$kick", value="EX. $kick [USER] [REASON]", inline=False)
        embed.add_field(name="$unban", value="EX. $unban [USER]", inline=False)
        embed.add_field(name="$clear", value="EX. $clear [AMOUNT]", inline=False)

        await ctx.send(embed=embed, delete_after=60)
        await ctx.message.delete()    

def setup(client):
    client.add_cog(help(client))