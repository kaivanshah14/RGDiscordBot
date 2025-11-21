import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


class dev(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['reboot'])
  async def restart(self, ctx):
    extensions = ['cogs.fun', 'cogs.helpCommand', 'cogs.socials', 'cogs.staff']
    owners = [829590898954207233, 403541270779265024]

    if ctx.author.id in owners:
      m = await ctx.send(
        "> **⚠ Restarting the bot! Please wait don't use any commands ⚠**",
        delete_after=10)
      try:
        for extension in extensions:
          await self.client.unload_extension(extension)
          await self.client.load_extension(extension)
        m = await ctx.send(
          "> <a:loader:837561814765010944> **Reloading Real Gods Clan Bot**")
        await asyncio.sleep(5)
        await m.edit(
          content="> <a:loader:837561814765010944> **Fetching data**")
        await asyncio.sleep(4)
        await m.edit(
          content="> <a:accepted:704094494957764722> **Restart completed**")
        await asyncio.sleep(3)
        await m.edit(content="> Logging in... *Please wait*")
        await asyncio.sleep(1)
        await m.edit(content="> Almost completed")
        await asyncio.sleep(2)
        await m.edit(
          content="> Bot is now available <a:lesgo:762553055626395648> ")
        await asyncio.sleep(2)
        await m.edit(
          content="**Logged in as**:\n**{0.user.name}** - `{0.user.id}`".
          format(self.client))
        await asyncio.sleep(3)
        await m.edit(
          content=f'Current bot latency: {round(self.client.latency * 1000)} ms'
        )

      except Exception as e:
        await ctx.send(
          f"<a:deny:780077466161119273> Oops! There's some problem in restarting the bot.\n\n`{e}`"
        )
        await m.edit(content="<a:deny:780077466161119273> **Restart failed**")

    else:
      await ctx.send("**You cannot use this command :x:**")


async def setup(client):
  await client.add_cog(dev(client))
