import discord
from discord.ext import commands

prefix = 'rg!'


class helpCommand(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
    await ctx.send('Pong!')

  @commands.group(invoke_without_command=True)
  async def help(self, ctx, *input):
    prefix = 'rg!'
    version = '1.8'
    owner = '<@403541270779265024>'
    tag = "ℜG 〕"

    emb = discord.Embed(
      title='Real Gods Bot Help Command',
      color=ctx.author.color,
      description=
      f"Here's the list of available commands. For more specific and detailed help for each commands, use `{prefix}help <command name>` like `{prefix}help hello`"
    )
    emb.add_field(
      name='Bot Information\n------------------',
      value=f'Server Prefix: {prefix}\nVersion: {version}\nOwner: {owner}\n',
      inline=False)

    emb.add_field(name='Fun Commands\n------------------',
                  value="`hello` - Say hello\n" + "`add` - Add 2 numbers\n" +
                  "`invite` - Get RG server invite\n" +
                  "`joke` - Get a random joke 😂\n" +
                  "`punch` - Punch someone 👊\n`" + "kiss` - Give a kiss! 💋\n" +
                  "`hug` - Give a hug 🤗\n" + "`topic` - Get channel topic\n" +
                  "`slap` - Give someone a tight slap\n" +
                  "`cry` - If you wish to cry 😭\n" +
                  "`pingz` - Spam ping someone | **⚠**\n" +
                  "`pp` - Check someone's PP size 🍆\n" +
                  "`valorantstat` - Get someone's Valorant Stats 😋 | 🆕",
                  inline=False)

    emb.add_field(
      name='Staff Only Commands\n------------------',
      value=f"`setnick` - Set custom nickname with `{tag}` tag\n" +
      f"`defnick` - Set default nickname with `{tag}` tag\n" +
      f"`resetnick` - Reset someone nickname to default username\n" +
      f"`promote` - Promote a staff member\n" +
      f"`demote` - Demote a staff member\n" +
      f"`inrole` -  Get a list of users in that role 📃\n" +
      f"`accept` - Accept someone to staff ✅\n" +
      f"`dm` - Sent a direct message through bot | **⚠**\n" +
      f"`valotryout` -  Add someone to Tryouts for Valorant\n" +
      f"`find` - Find someone on RG discord server through options 🔍\n" +
      f"`pingAll` - Ping everyone in that role | **⚠**\n",
      inline=False)

    emb.add_field(name='Social Commands\n------------------',
                  value="`website` - Get a link to RG website\n" +
                  "`instagram` - Get a link to RG Instagram\n" +
                  "`socials` - Get all RG socials 🔗",
                  inline=False)

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await ctx.send(embed=emb)

  @help.command(aliases=['sn'])
  async def setnick(self, ctx):
    emb = discord.Embed(
      title='setnick',
      color=(discord.Colour.random()),
      description=
      f'`rg!setnick <user_id> newNickname`\n\n**Alias:** `rg!sn`\n\n**Note: Must have `Manage Nickname` permission to use this command.**\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/927518110003654656/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command(aliases=['dn'])
  async def defnick(self, ctx):
    emb = discord.Embed(
      title='defnick',
      color=(discord.Colour.random()),
      description=
      f'`rg!defnick <user_id>`\n\n**Alias:** `rg!dn`\n\n**Note: Must have `Manage Nickname` permission to use this command.**\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/927524145300897822/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command(aliases=['rn'])
  async def resetnick(self, ctx):
    emb = discord.Embed(
      title='resetnick',
      color=(discord.Colour.random()),
      description=
      f'`rg!resetnick <user_id>`\n\n**Alias:** `rg!rn`\n\n**Note: Must have `Manage Nickname` permission to use this command.**\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/927529770688852008/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command(aliases=['pr'])
  async def promote(self, ctx):
    emb = discord.Embed(
      title='promote',
      color=(discord.Colour.random()),
      description=
      f'`rg!promote <user_id> <role_name>/<role_id>`\n\n**Alias:** `rg!pr`\n\nRoles eligible to use this command: <@&806206434940551188> and above\n\n**:warning: Note:** Only works if user is already a `Staff Member` or is `Staff in Training.`\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/930901400370679818/unknown.png"
    )
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await ctx.send(embed=emb)

  @help.command(aliases=['dr'])
  async def demote(self, ctx):
    emb = discord.Embed(
      title='demote',
      color=(discord.Colour.random()),
      description=
      f'`rg!demote <user_id> <role_name>/<role_id>`\n\n**Alias:** `rg!dr`\n\nRoles eligible to use this command: <@&806206434940551188> and above\n\n**:warning: Note:** Only works if user is already a `Staff Member` or is `Staff in Training.`\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/930901939963711629/unknown.png"
    )
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    await ctx.send(embed=emb)

  @help.command(aliases=['ir'])
  async def inrole(self, ctx):
    emb = discord.Embed(
      title='inrole',
      color=(discord.Colour.random()),
      description=
      f'`rg!inrole <user_id>`\n\n**Alias:** `rg!ir`\n\nRoles eligible to use this command: <@&694114569223929877> and above\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/930905645048299530/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def accept(self, ctx):
    emb = discord.Embed(
      title='accept',
      color=(discord.Colour.random()),
      description=
      f'`rg!accept <user_id> <option>`\n\n**Options:**\n`staff` - Accept user as <@&780070933762408479>\n`pm` - Accept a user as a <@&808563309829292063>\n`exe` - Accept an user as an <@&806206434940551188>\n`ssm` - Accept a user as a <@&939904375881601054>\n\nRoles eligible to use this command: <@&806206434940551188> and above\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/930906487419711528/staff_accept.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def hello(self, ctx):
    emb = discord.Embed(
      title='hello',
      color=(discord.Colour.random()),
      description=
      f'`rg!hello`\n\nJust say hello to the bot 😊\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/936665360680230922/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def add(self, ctx):
    emb = discord.Embed(
      title='add',
      color=(discord.Colour.random()),
      description=
      f'`rg!add <number1> <number2>`\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )
    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/789140658648252426/936668101599166494/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def invite(self, ctx):
    emb = discord.Embed(
      title='invite',
      color=(discord.Colour.random()),
      description=
      f'`rg!invite`\n\nAn invite for the server\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/789140658648252426/936668429014954094/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def joke(self, ctx):
    emb = discord.Embed(
      title='joke',
      color=(discord.Colour.random()),
      description=
      f'`rg!joke`\n\nTime to take a break and read some jokes! 😅\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://media.discordapp.net/attachments/789140658648252426/936668869291036712/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def punch(self, ctx):
    emb = discord.Embed(
      title='punch',
      color=(discord.Colour.random()),
      description=
      f'`rg!punch <user_id>/<user_mention>`\n\nLets see how hard can you punch someone 👊🏻\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/789140658648252426/936671700970504192/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def kiss(self, ctx):
    emb = discord.Embed(
      title='kiss',
      color=(discord.Colour.random()),
      description=
      f'`rg!kiss <user_id>/<user_mention>`\n\nSpread love 😘\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/789140658648252426/936672034161840249/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def hug(self, ctx):
    emb = discord.Embed(
      title='hug',
      color=(discord.Colour.random()),
      description=
      f'`rg!hug <user_id>/<user_mention>`\n\nAwww 🤗\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/789140658648252426/936672617430151208/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def pp(self, ctx):
    emb = discord.Embed(
      title='pp',
      color=(discord.Colour.random()),
      description=
      f'`rg!pp <user_id>/<user_mention>`\n\n😲\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/950808000384344064/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command(aliases=['vt'])
  async def valotryout(self, ctx):
    emb = discord.Embed(
      title='Valorant Tryout Management',
      color=(discord.Colour.random()),
      description=
      f'`rg!vt <user_id>/<user_mention> <region>`\n\n**Region**\n`asia` - Accept applicant as <@&928900868210827275>\n`europe` or `eu` - Accept applicant as <@&950432226686951474>\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/950809634262904882/unknown.png"
    )
    await ctx.send(embed=emb)

  @help.command()
  async def find(self, ctx):
    emb = discord.Embed(
      title='Find Users on Server',
      color=(discord.Colour.random()),
      description=
      f'`rg!find <user_id>/<user_mention> <option>`\n\n**Options**\n`id` - Find a User by User Id\n`nick` or `nickname` - Find a User by Nickname\n`tag` - Find a User by Discord Tag\n\nRequested by: {ctx.author.mention}\n\n__**Example:**__'
    )

    emb.set_footer(
      text='#RGAlways, #RGonTop',
      icon_url=
      "https://cdn.discordapp.com/attachments/708651332357324830/928921610893819904/1641210732104.jpg"
    )
    emb.set_image(
      url=
      "https://cdn.discordapp.com/attachments/708651332357324830/950811172247072808/unknown.png"
    )
    await ctx.send(embed=emb)


# @help.command(aliases=['dn'])
# async def send_embed(ctx, embed):

  """
    Function that handles the sending of embeds
    -> Takes context and embed to send
    - tries to send embed in channel
    - tries to send normal message when that fails
    - tries to send embed private with information abot missing permissions
    If this all fails: https://youtu.be/dQw4w9WgXcQ
    """


async def setup(client):
  await client.add_cog(helpCommand(client))
