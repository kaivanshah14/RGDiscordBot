import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

insta = 'https://www.instagram.com/realgodsesports'
twitter = 'https://twitter.com/RealGodsEsports'
website = 'https://realgodsclan.netlify.app/'
dc = 'https://discord.gg/pUvnmRZ'


class socials(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def twitter(self, ctx):
    emb = discord.Embed(
      title='**Twitter**',
      color=(discord.Colour.random()),
      description=f'<:rgTWITTER:935537054664757349> Twitter - {twitter}')
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await ctx.send(embed=emb)

  @commands.command(aliases=['web'])
  async def website(self, ctx):
    emb = discord.Embed(
      title='**Website**',
      color=(discord.Colour.random()),
      description=f'<:Mail:830859644574105700> Website - {website}')
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await ctx.send(embed=emb)

  @commands.command(aliases=['insta'])
  async def instagram(self, ctx):
    emb = discord.Embed(
      title='**Instagram**',
      color=(discord.Colour.random()),
      description=f'<:rgIG:935537289260568596> Instagram - {insta}')
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await ctx.send(embed=emb)

  @commands.command()
  async def socials(self, ctx):
    emb = discord.Embed(
      title='**Socials**',
      color=(discord.Colour.random()),
      description=
      f'<:rgIG:935537289260568596> Instagram - {insta}\n<:rgTWITTER:935537054664757349> Twitter - {twitter}\n<:Mail:830859644574105700> Website - {website}\n<:rgDISCORD:935537176148578424> Discord - {dc}'
    )
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await ctx.send(embed=emb)


async def setup(client):
  await client.add_cog(socials(client))
