import discord
from discord.ext import commands
import re

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


class staff(commands.Cog):

  # connects the index client to this file
  def __init__(self, client):
    self.client = client

  @commands.command(pass_content=True, aliases=['dn'])
  @commands.has_permissions(manage_nicknames=True)
  async def defnick(self, ctx, member: discord.Member):
    await member.edit(nick='ℜG 〕{}'.format(member.name))
    await ctx.send(f'Nickname was changed for **{member.name}**')

  @commands.command(pass_content=True, aliases=['sn'])
  @commands.has_permissions(manage_nicknames=True)
  async def setnick(self, ctx, member: discord.Member, nick):
    await member.edit(nick='ℜG 〕{}'.format(nick))
    await ctx.send(f'Nickname was changed for **{member.name}**')

  @commands.command(pass_content=True, aliases=['rn'])
  @commands.has_permissions(manage_nicknames=True)
  async def resetnick(self, ctx, member: discord.Member):
    await member.edit(nick='{}'.format(member.name))
    await ctx.send(f'Nickname was changed for **{member.name}**')

  @commands.command(pass_content=True, aliases=['pr'])
  @commands.has_any_role(806206434940551188, 706883939087810964,
                         795263405132611605, 763055090214633473,
                         579595387313324042)
  @commands.has_permissions(manage_roles=True)
  async def promote(self, ctx, member: discord.Member, role: discord.Role):
    news = self.client.get_channel(883323899981479946)
    r1 = ctx.guild.get_role(763055090214633473)
    r2 = ctx.guild.get_role(579595387313324042)
    r3 = ctx.guild.get_role(928662946232549417)
    r4 = ctx.guild.get_role(795263405132611605)
    r5 = ctx.guild.get_role(962599070633971752)

    if role == r1 or role == r2 or role == r3 or role == r4 or role == r5:
      await ctx.send(f"**Can't do that :x:**")
    elif role in member.roles:
      await ctx.send(
        f"**{member}** already has **{role}** hence cannot be promoted. :x:")
    else:
      emb = discord.Embed(
        title='**STAFF UPDATES**',
        color=role.color,
        description=
        f'Congratulations **{member.mention}** on getting promoted to **{role.mention}** :tada: \n\nYou continue to exceed every expectation that we set. Great job.'
      )
      emb.set_footer(
        text='#RGAlways, #RGonTop',
        icon_url=
        "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
      )
      # emb.set_thumbnail(url=member.avatar_url)
      await member.add_roles(role)
      await ctx.send(
        f"**{member}** has been promoted to **{role}**. :white_check_mark:")
      await news.send(embed=emb)
      # emb2 = discord.Embed(title='**Staff role update at Real Gods Clan**', color=role.color, description=f"Congratulations on getting promoted to **{role}** :tada: \nPlease contact <@961613618632347658> or <@747838925049168005> to know more about your duties.")
      # emb2.set_footer(text='#RGAlways, #RGonTop', icon_url = "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg")
      # emb2.set_image(url="https://c.tenor.com/pk0oHDAYMy8AAAAC/congratulations-congrats.gif")
      # await member.send(embed=emb2)

  @commands.command(pass_content=True, aliases=['dr'])
  @commands.has_any_role(806206434940551188, 706883939087810964,
                         795263405132611605, 763055090214633473,
                         579595387313324042)
  @commands.has_permissions(manage_roles=True)
  async def demote(
    self,
    ctx,
    member: discord.Member,
    role: discord.Role,
  ):
    news = self.client.get_channel(883323899981479946)
    if role not in member.roles:
      await ctx.send(
        f"**{member}** doesn't have **{role} role** hence cannot be demoted. :x:"
      )
    else:
      emb = discord.Embed(
        title='**STAFF UPDATES**',
        color=role.color,
        description=
        f'Unfortunately **{member.mention}** has been demoted from **{role.mention}** :pensive: \n\nStay strong and work hard!'
      )
      emb.set_footer(
        text='#RGAlways, #RGonTop',
        icon_url=
        "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
      )
      await member.remove_roles(role)
      await ctx.send(
        f"**{member}** has been demoted from **{role}**. :white_check_mark:")
      await news.send(embed=emb)
      # emb2 = discord.Embed(title='**Staff role update at Real Gods Clan**', color=role.color, description=f"Unfortunately the Management team has decided to demote you from **{role}** role \nas we don't see you fit for the role at the moment, we hope you try working harder. \n \n Stay strong :v:")
      # emb2.set_footer(text='#RGAlways, #RGonTop', icon_url = "https://media.giphy.com/media/P7Y2VlF715z6NqR0XV/giphy.gif")
      # await member.send(embed=emb2)

  @commands.command(pass_context=True, aliases=['ir'])
  @commands.has_any_role(694114569223929877, 808563309829292063,
                         898865399834218516, 806206434940551188,
                         706883939087810964, 795263405132611605,
                         763055090214633473, 579595387313324042)
  async def inrole(self, ctx, *, role: discord.Role):
    embed = discord.Embed(title=f"**{role.name} - {len(role.members)} users**",
                          description=("\n".join(map(str, role.members))),
                          color=role.color)
    await ctx.send(embed=embed)

  @commands.command(pass_context=True)
  @commands.has_any_role(806206434940551188, 706883939087810964,
                         795263405132611605, 763055090214633473,
                         579595387313324042)
  async def accept(self, ctx, member: discord.Member, name):
    name = name.lower()
    news = self.client.get_channel(883323899981479946)
    role2 = ctx.guild.get_role(780070933762408479)

    async def checkHasRole(member, role):
      if role in member.roles:
        await ctx.send(
          f"> **{member.name}** already has **{role} hence cannot be accepted** :x:"
        )
      else:
        if (role != role2):
          await member.add_roles(role2)
        await member.add_roles(role)
        await member.edit(nick='ℜG 〕{}'.format(member.name))
        await ctx.send(
          f"> **{member.name}** is now a **{role}** :white_check_mark:")
        emb = discord.Embed(
          title='**STAFF UPDATES**',
          color=role.color,
          description=
          f'Congratulations **{member.mention}** on getting accepted as **{role.mention}** :tada: \n\nWelcome to the Real Gods Staff Team.\n\n'
        )
        emb.set_footer(
          text='#RGAlways, #RGonTop',
          icon_url=
          "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
        )
        # emb.set_thumbnail(url=member.avatar_url)
        await news.send(embed=emb)
        # await member.send(embed=emb2)

    if (name == "staff" or name == 'sit' or name == 'staff_training'):
      role = ctx.guild.get_role(780070933762408479)
      await checkHasRole(member, role)
    elif (name == "pm" or name == 'partnership_manager'):
      role = ctx.guild.get_role(808563309829292063)
      await checkHasRole(member, role)
    elif (name == 'exe' or name == 'executive'):
      role = ctx.guild.get_role(806206434940551188)
      await checkHasRole(member, role)
    elif (name == 'smm' or name == 'socialmediamanager'):
      role = ctx.guild.get_role(939904375881601054)
      await checkHasRole(member, role)
    else:
      await ctx.send(
        f"> Used alias is incorrect :x: \n> You can use the following: \n> `staff` for **Staff in Training** \n> `pm` for **Partnership Manager** \n> `exe` for **Executive**"
      )

  # @commands.command(pass_context=True)
  # @commands.has_any_role(706883939087810964, 795263405132611605, 763055090214633473, 579595387313324042)
  # async def remove(self,ctx, member:discord.Member):
  #     rolelist = [780070933762408479, 694114569223929877, 808563309829292063, 898865399834218516, 806206434940551188, 871640017611685919]
  #     if rolelist in member.roles:
  #         comm = ctx.guild.get_role(728338560578617444)
  #         await member.edit(roles=[comm])
  #         await member.edit(nick='{}'.format(member.name))
  #         await ctx.send(f"**{member.name}** has been removed from the Staff Team.")
  #         emb2 = discord.Embed(title='**Staff role update at Real Gods Clan**', color=(discord.Colour.random()), description=f"We regret to inform you that you have been removed from Real Gods Staff Team. If you think this was done by mistake kindly DM an Executive at [Real Gods Clan](https://discord.gg/pUvnmRZ)")
  #         emb2.set_footer(text='#RGAlways, #RGonTop', icon_url = "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg")
  #         await member.send(embed=emb2)
  #     else:
  #       await ctx.send(f'**{member.name}** is not a Staff Member hence cannot be removed :x:')

  @commands.command(pass_context=True)
  @commands.has_any_role(795263405132611605, 763055090214633473,
                         579595387313324042)
  async def dm(self, ctx, member: discord.Member, *, msg=None):
    emb = discord.Embed(title='**You have a message from Real Gods Clan**',
                        color=(discord.Colour.random()),
                        description=f'{msg}\n\n')
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await member.send(embed=emb)
    await ctx.send(f'**DM message was sent successfully to {member.name} ✅**')

  # li = [['To change ad', 'Pending', 'Assigned to'], ['To get staff', 'Pending']]
  # @commands.command(pass_context=True)
  # @commands.has_any_role(795263405132611605, 763055090214633473, 579595387313324042)
  # async def tasks(self,ctx, li):

  # @commands.command(pass_context=True)
  # @commands.has_any_role(806206434940551188, 706883939087810964, 795263405132611605, 763055090214633473, 579595387313324042)
  # async def reject(self,ctx, member:discord.Member):
  #   c=0
  #   list1=[780070933762408479, 694114569223929877, 808563309829292063]
  #   for i in list1:
  #     if i in member.roles:
  #       c = c+1

  #   if(c>1):
  #       await ctx.send(f"{member.name} is already Staff, hence cannot be rejected :x:.\nIf you wish to demote or remove the staff member use: `rg!demote` or `rg!remove` command.")
  #   else:
  #       emb2 = discord.Embed(title='**Staff Application update at Real Gods Clan**', color=(discord.Colour.random()), description=f"We regret to inform you that your **Staff Application** was rejected at [Real Gods Clan](https://discord.gg/pUvnmRZ) :x:\n\nYou can re-apply after 7 days, we suggest you to **stay active on the Real Gods Clan Server** to increase your chance of getting accepted.\nGood Luck!")
  #       emb2.set_footer(text='#RGAlways, #RGonTop', icon_url = "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg")
  #       await member.send(embed=emb2)
  #       await ctx.send(f"Rejection message sent to **{member.name}** ✅")

  @commands.command(pass_context=True, aliases=['fi'])
  @commands.has_any_role(930797586401599508, 935840617131561050,
                         706883939087810964, 795263405132611605,
                         763055090214633473, 579595387313324042)
  async def find(self, ctx, type: str, search: str):
    if type == 'id':
      loop = [
        f"{i} | {i} - {i.id}" for i in ctx.guild.members
        if (str(search) in str(i.id)) and not i.bot
      ]
      await ctx.send(
        f'Found **{len(loop)}** on your search for **{search}** -> {loop}')
    if type == 'nick' or type == 'nickname':
      loop = [
        f"{i.nick} | {i} {i.id}" for i in ctx.guild.members if i.nick
        if (search.lower() in i.nick.lower()) and not i.bot
      ]
      await ctx.send(
        f'Found **{len(loop)}** on your search for **{search}** -> {loop}')
    if type == 'tag' or type == 'discordtag':
      if not len(search) == 4 or not re.compile("^[0-9]*$").search(search):
        return await ctx.send("You must provide exactly 4 digits")
      loop = [
        f"{i} - {i.id}" for i in ctx.guild.members if search == i.discriminator
      ]
      await ctx.send(
        f'Found **{len(loop)}** on your search for **{search}** -> {loop}')

  @commands.command(pass_context=True)
  @commands.has_any_role(579595387313324042, 930797586401599508,
                         706883939087810964)
  async def casual(self, ctx, member: discord.Member):
    role = ctx.guild.get_role(1043541748779057365)
    await member.add_roles(role)
    await member.edit(nick='ℜG 〕{}'.format(member.name))
    await ctx.send(
      f"**{member}** has been given **{role}**. :white_check_mark:")

  @commands.command(pass_context=True, aliases=['pa'])
  @commands.has_any_role(579595387313324042, 930797586401599508,
                         706883939087810964)
  async def pingAll(self, ctx, role: discord.Role):
    members = role.members
    memberString = ""
    for member in members:
      memberString += member.mention
    await ctx.send(memberString)


async def setup(client):
  await client.add_cog(staff(client))
