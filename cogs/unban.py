import discord
from discord.ext import commands

class unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed=discord.Embed(description="**User was unbanned!**", color=0xc79df0)

                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()
                return

def setup(client):
    client.add_cog(unban(client))