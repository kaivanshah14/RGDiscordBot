import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


class joinleave(commands.Cog):

  # connects the index client to this file
  def __init__(self, client):
    self.client = client

  # @commands.Cog.listener()
  # async def on_member_join(self,member):
  #     guild = self.client.get_guild(571139196715270144)
  #     channel = self.client.get_channel()
  #     if member.guild!=guild:
  #       return
  #     await channel.send(f"> <a:phypesquad:800273195109449730> Kon'nichiwa {member.mention} <:rg_welcome:762564519569653771>\n> Welcome to **{guild.name}** we are a clan for **Valorant, Call of Duty Mobile, and Clash of Clans.** If you are looking for a Clan join Real Gods by applying at <#803999972366090262> <a:ZeroTwoPat:926082188909355069> \n> You are the {guild.member_count} server member <a:MusicLove:705522432693502002>")


async def setup(client):
  await client.add_cog(joinleave(client))
