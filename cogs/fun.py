import discord
from discord import client
from discord.ext import commands
import random
import giphy_client
from giphy_client.rest import ApiException

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


class fun(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def hello(self, ctx):
    await ctx.reply('Hey there, I hope you have a good day!')

  @commands.command()
  async def invite(self, ctx):
    await ctx.reply('https://discord.gg/pUvnmRZ')

  @commands.command()
  async def add(self, ctx, n1: int, n2: int):
    await ctx.reply(n1 + n2)

  @commands.command()
  async def joke(self, ctx):
    test_list = [
      'Today a man knocked on my door and asked for a small donation toward the local swimming pool. I gave him a glass of water.',
      'Maybe if we start telling people their brain is an app, they will want to use it',
      'I got a new pair of gloves today, but they are both lefts, which on the one hand is great, but on the other, it is just not right.',
      'People who take care of chickens are literally chicken tenders',
      'It was an emotional wedding. Even the cake was in tiers',
      'The future, the present, and the past walk into a bar. Things got a little tense',
      'Last night my girlfriend was complaining that I never listen to her… or something like that',
      'A told my girlfriend she drew her eyebrows too high. She seemed surprised',
      'I failed math so many times at school, I cannot even count',
      'Why was six afraid of seven? Because seven eight nine',
      'What do fish say when they hit a concrete wall? Dam!',
      'What did the toaster say to the slice of bread? "I want you inside me."',
      '"Give it to me! Give it to me!" she yelled. "I am so wet, give it to me now!" She could scream all she wanted, but I was keeping the umbrella.',
      'Two men broke into a drugstore and stole all the Viagra. The police put out an alert to be on the lookout for the two hardened criminals.',
      'They say that during sex you burn off as many calories as running eight miles. Who the hell runs eight miles in 30 seconds?',
      'I will admit it, I have a tremendous sex drive. My girlfriend lives forty miles away.',
      'Who is the most popular guy at the nudist colony? The one who can carry a cup of coffee in each hand and a dozen doughnuts.',
      'What is the difference between kinky and perverted? Kinky is when you tickle your girlfriend with a feather, perverted is when you use the whole bird.',
      '"I bet you cannot tell me something that will make me both happy and sad at the same time," a husband says to his wife. She thinks about it for a moment and then responds, "Your penis is bigger than your brothers."',
      'A woman walks out of the shower, winks at her boyfriend, and says, "Honey, I shaved myself down there. Do you know what that means?" The boyfriend says, "Yeah, it means the drain is clogged again."',
      'How do you make a pool table laugh? Tickle its balls.',
      'If you were born in September, it is pretty safe to assume that your parents started their new year with a bang.',
      'A naked man broke into a church. The police chased him around and finally caught him by the organ.',
      'Did you hear about the constipated accountant? He could not budget, so he had to work it out with a paper and pencil.',
      'Why did the sperm cross the road? Because I put on the wrong sock this morning.',
      'An old woman walked into a dentists office, took off all her clothes, and spread her legs. The dentist said, "I think you have the wrong room." "You put in my husbands teeth last week," she replied. "Now you have to remove them."',
      'Why does a mermaid wear seashells? Because she outgrew her B-shells!',
      'What do you call a cheap circumcision? A rip-off!',
      'What do you do when your cats dead? Play with the neighbors pussy instead.',
      'How is life like toilet paper? You are either on a roll or taking shit from someone.',
      'What is the difference between a tire and 365 used condoms? One is a Goodyear. The other is a great year.',
      'What is Moby Dicks dads name? Papa Boner.',
      'What do you call someone who refuses to fart in public? A private tutor!',
      'What do you call a herd of cows masturbating? Beef stroking off!',
      'What did the leper say to the sex worker? Keep the tip.',
      'What do you call the lesbian version of a cock block? A beaver dam!',
      'What do a penis and a Rubiks Cube have in common? The more you play with it, the harder it gets.',
      'What is long, green, and smells like bacon? Kermit The Frogs fingers!',
      'What do you get when you jingle Santas balls? A white Christmas!',
      'Why is diarrhea hereditary? It runs in your genes!',
      'A penguin takes his car to the shop and the mechanic says it will take about an hour for him to check it. While he waits, the penguin goes to an ice cream shop and orders a big sundae to pass the time. The penguin is not the neatest eater, and he ends up covered in melted ice cream. When he returns to the shop, the mechanic takes one look at him and says, "Looks like you blew a seal." "No," the penguin insists, "it is just ice cream."',
      'What did one butt cheek say to the other? Together, we can stop this crap.',
      'A man and a woman started to have sex in the middle of a dark forest. After about 15 minutes, the man finally gets up and says, "Damn, I wish I had a flashlight!" The woman says, "Me too, you have been eating grass for the past ten minutes!"',
      'What do you get when you cross a dick with a potato? A dictator!',
      'How is sex like a game of bridge? If you have a great hand, you do not need a partner.',
    ]
    random_num = random.choice(test_list)
    await ctx.send(f'Here is a joke : {random_num}')

  @commands.command()
  async def punch(self, ctx, member: discord.Member):
    punch_gif = [
      'https://c.tenor.com/EfhPfbG0hnMAAAAC/slap-handa-seishuu.gif',
      'https://c.tenor.com/SwMgGqBirvcAAAAC/saki-saki-kanojo-mo-kanojo.gif',
      'https://c.tenor.com/BoYBoopIkBcAAAAC/anime-smash.gif',
      'https://c.tenor.com/EvBn8m3xR1cAAAAC/toradora-punch.gif',
      'https://c.tenor.com/Y8_ITfFMQmMAAAAC/yue-arifureta.gif',
      'https://c.tenor.com/6a42QlkVsCEAAAAC/anime-punch.gif',
      'https://c.tenor.com/UH8Jnl1W3CYAAAAC/anime-punch-anime.gif',
      'https://c.tenor.com/aEX1wE-WrEMAAAAC/anime-right-in-the-stomach.gif',
      'https://c.tenor.com/EdV_frZ4e_QAAAAC/anime-naruto.gif',
      'https://c.tenor.com/5AsLKQTjbJ4AAAAC/kasumi-love-live.gif',
      'https://c.tenor.com/xWqmJMePsqEAAAAC/weaboo-otaku.gif',
      'https://c.tenor.com/n7LKoJVrwM8AAAAC/anime-punch.gif',
      'https://c.tenor.com/lWmjgII6fcgAAAAC/saki-saki-mukai-naoya.gif',
      'https://c.tenor.com/3CUBZHrDUvUAAAAC/punch-combo.gif',
      'https://c.tenor.com/D4D8Xj2rqzoAAAAC/anime-punch.gif',
      'https://c.tenor.com/DKMb2QPU7aYAAAAC/rin243109-blue-exorcist.gif',
      'https://c.tenor.com/l_zcD2qX5M4AAAAC/double-punch-anime-double-punch.gif',
      'https://c.tenor.com/Ka8eQ8D7yVwAAAAC/anime-super-punch.gif',
      'https://c.tenor.com/uaoyO8y01vMAAAAC/naruto-sasuke.gif',
      'https://c.tenor.com/SPsqUzhCu8QAAAAC/hajimenoippo-ippo.gif',
    ]
    emb = discord.Embed(
      title="Punched You!",
      colour=(discord.Colour.random()),
      description=f"{ctx.author.mention} punched {member.mention}")
    emb.set_image(url=(random.choice(punch_gif)))
    await ctx.channel.send(embed=emb)

  @commands.command()
  async def slap(self, ctx, member: discord.Member):
    slap_gif = [
      'https://c.tenor.com/XiYuU9h44-AAAAAC/anime-slap-mad.gif',
      'https://c.tenor.com/Ws6Dm1ZW_vMAAAAC/girl-slap.gif',
      'https://c.tenor.com/FJsjk_9b_XgAAAAC/anime-hit.gif',
      'https://c.tenor.com/WRYiTfeCU8YAAAAd/anime-slap-slap-anime.gif',
      'https://c.tenor.com/ra17G61QRQQAAAAC/tapa-slap.gif',
      'https://c.tenor.com/PeJyQRCSHHkAAAAC/saki-saki-mukai-naoya.gif',
      'https://c.tenor.com/bW9sL6u6V7AAAAAC/fly-away-slap.gif',
      'https://c.tenor.com/noSQI-GitQMAAAAC/mm-emu-emu.gif',
      'https://c.tenor.com/VlSXTbFcvDQAAAAC/naruto-anime.gif',
      'https://c.tenor.com/TCxz2fAU75IAAAAC/love-lab-head-smack-anime-smack.gif',
      'https://c.tenor.com/rVXByOZKidMAAAAd/anime-slap.gif',
      'https://c.tenor.com/1-1M4PZpYcMAAAAd/tsuki-tsuki-ga.gif',
      'https://c.tenor.com/CvBTA0GyrogAAAAC/anime-slap.gif',
      'https://c.tenor.com/1lemb3ZmGf8AAAAC/anime-slap.gif',
      'https://c.tenor.com/5eI0koENMAAAAAAC/anime-hit.gif',
      'https://c.tenor.com/OuYAPinRFYgAAAAC/anime-slap.gif',
      'https://c.tenor.com/nBaCVW8855oAAAAC/anime-slap.gif',
      'https://c.tenor.com/uTT2gXruNtkAAAAC/oreimo-anime.gif',
      'https://c.tenor.com/AlM5Pxv06fUAAAAC/anime-slap.gif',
    ]
    emb = discord.Embed(
      title="Slaps for you!",
      colour=(discord.Colour.random()),
      description=f"{ctx.author.mention} slapped {member.mention}")
    emb.set_image(url=(random.choice(slap_gif)))
    await ctx.channel.send(embed=emb)

  @commands.command()
  async def cry(self, ctx):
    cry_gif = [
      'https://c.tenor.com/N2qSCBkdracAAAAM/neko-anime.gif',
      'https://c.tenor.com/Q0HUwg81A_0AAAAd/anime-cry.gif',
      'https://c.tenor.com/OfYt0T0tgCYAAAAC/anime-cry.gif',
      'https://c.tenor.com/gDk49oAcW9QAAAAd/anime-cry-cry.gif',
      'https://c.tenor.com/q9V98YHPZX4AAAAC/anime-umaru.gif',
      'https://c.tenor.com/fBNK66X1CWwAAAAC/cry-anime.gif',
      'https://c.tenor.com/nYR1I7VED_IAAAAC/gayixiangs.gif',
      'https://c.tenor.com/TbGKaGTBI2QAAAAC/kobayashi-kobayashi-san-chi-no-maid-dragon.gif',
      'https://c.tenor.com/TtSO-_weHb0AAAAC/aqua-anime.gif',
      'https://c.tenor.com/XBWh-szFwDQAAAAC/crying-naruto-crying.gif',
      'https://c.tenor.com/NMiID29TUvIAAAAC/hunter-x-hunter-gon-freecs.gif',
      'https://c.tenor.com/I44FeazkcWQAAAAC/anime-cute.gif',
      'https://c.tenor.com/r0XjQL8Fd5MAAAAC/crying-sad.gif',
      'https://c.tenor.com/2pawKZu4h_oAAAAC/sad-anime.gif',
      'https://c.tenor.com/SVvaVhZlVB8AAAAC/anime-crying.gif',
      'https://c.tenor.com/jTei9b9RH0wAAAAC/anime-sad.gif',
      'https://c.tenor.com/sqCIrfKU84gAAAAC/anime-anime-girl.gif',
      'https://c.tenor.com/8FsoAJ-ZmVcAAAAC/anime-hitori.gif',
      'https://c.tenor.com/EZsmE8l33TcAAAAd/anime-anime-cry.gif',
    ]
    emb = discord.Embed(title='😭',
                        colour=(discord.Colour.random()),
                        description=f'{ctx.author.mention} feels bad')
    emb.set_image(url=(random.choice(cry_gif)))
    await ctx.channel.send(embed=emb)

  @commands.command()
  async def kiss(self, ctx, member: discord.Member, q='anime-kiss'):
    kiss_gif = [
      'https://c.tenor.com/F02Ep3b2jJgAAAAC/cute-kawai.gif',
      'https://c.tenor.com/V0nBQduEYb8AAAAC/anime-kiss-making-out.gif'
      'https://c.tenor.com/TWbZjCy8iN4AAAAC/girl-anime.gif',
      'https://c.tenor.com/dJU8aKmPKAgAAAAC/anime-kiss.gif',
      'https://c.tenor.com/I8kWjuAtX-QAAAAC/anime-ano.gif',
      'https://c.tenor.com/wDYWzpOTKgQAAAAC/anime-kiss.gif',
      'https://c.tenor.com/03wlqWILqpEAAAAC/highschool-dxd-asia.gif',
      'https://c.tenor.com/G954PGQ7OX8AAAAC/cute-urara-shiraishi-anime.gif',
      'https://c.tenor.com/3zdH2jC6qCcAAAAC/love-anime.gif',
      'https://c.tenor.com/4ofp_xCUBxcAAAAC/eden-of-the-east-akira-takizawa.gif',
      'https://c.tenor.com/e6cYiAPPCq4AAAAC/anime-kissing.gif',
      'https://c.tenor.com/BjwmxFVGKm0AAAAC/toloveru-unexpected.gif',
      'https://c.tenor.com/HgV0doOr_YoAAAAC/golden-time-anime.gif',
      'https://c.tenor.com/lK1PF-Xv1O4AAAAC/yato-anime-noragami.gif',
      'https://c.tenor.com/TnjL6WcdkkwAAAAd/anime-kiss.gif',
      'https://c.tenor.com/bkF2kFvXR50AAAAC/yes-love.gif',
      'https://c.tenor.com/By9JmT7hTwMAAAAC/kissing-couples.gif',
      'https://c.tenor.com/0E_odieuKmwAAAAC/anime-zero.gif'
    ]
    emb = discord.Embed(
      title="Love you :kissing_heart:",
      colour=(discord.Colour.random()),
      description=f"{ctx.author.mention} kisses {member.mention}")
    emb.set_image(url=(random.choice(kiss_gif)))
    await ctx.channel.send(embed=emb)

  @commands.command()
  async def hug(self, ctx, member: discord.Member):
    hug_gif = [
      'https://c.tenor.com/rQ2QQQ9Wu_MAAAAC/anime-cute.gif',
      'https://c.tenor.com/xgVPw2QK5n8AAAAC/sakura-quest-anime.gif',
      'https://c.tenor.com/DVOTqLcB2jUAAAAC/anime-hug-love.gif',
      'https://c.tenor.com/0vl21YIsGvgAAAAC/hug-anime.gif',
      'https://c.tenor.com/dIvoDyyk5LIAAAAC/anime-hug-sweet.gif',
      'https://c.tenor.com/UhcyGsGpLNIAAAAC/hug-anime.gif',
      'https://c.tenor.com/2bWwi8DhDsAAAAAC/hugs-and-love.gif',
      'https://c.tenor.com/ItpTQW2UKPYAAAAC/cuddle-hug.gif',
      'https://c.tenor.com/pcULC09CfkgAAAAC/hug-anime.gif',
      'https://c.tenor.com/xIuXbMtA38sAAAAC/toilet-bound-hanakokun.gif',
      'https://c.tenor.com/mmQyXP3JvKwAAAAC/anime-cute.gif',
      'https://c.tenor.com/X5nBTYuoKpoAAAAC/anime-cheeks.gif',
      'https://c.tenor.com/VqazOH8fQ8gAAAAC/anime-hug.gif',
      'https://c.tenor.com/nHkiUCkS04gAAAAC/anime-hug-hearts.gif',
      'https://c.tenor.com/vkiqyZJWJ4wAAAAC/hug-cat.gif',
      'https://c.tenor.com/nmzZIEFv8nkAAAAC/hug-anime.gif',
      'https://c.tenor.com/sBFE3GeNpJ4AAAAC/tackle-hug-couple.gif',
      'https://c.tenor.com/PuuhAT9tMBYAAAAC/anime-cuddles.gif',
      'https://c.tenor.com/5u1n4SYgd3AAAAAC/cuddle-nuzzle.gif',
    ]

    emb = discord.Embed(title="Hugs for you :hugging:",
                        colour=(discord.Colour.random()),
                        description=f"{ctx.author.mention} 🤗 {member.mention}")
    emb.set_image(url=(random.choice(hug_gif)))
    await ctx.channel.send(embed=emb)

  @commands.command(pass_content=True, aliases=['ct'])
  async def topic(self, ctx):
    m = ctx.channel
    emb = discord.Embed(title="Channel topic",
                        description=(f"{m.topic}"),
                        color=(discord.Colour.random()))
    if m.topic == None:
      await ctx.send("**No channel topic set**")
    else:
      await ctx.send(embed=emb)
      await ctx.message.delete()

  @commands.command(pass_content=True, aliases=['pz'])
  @commands.has_any_role(763055090214633473, 579595387313324042)
  async def pingz(self, ctx, member: discord.Member, num: int):
    for i in range(num):
      await ctx.send(
        f"{member.mention} check the message nibba and don't be gae",
        delete_after=60)

  @commands.command()
  async def pp(self, ctx, member: discord.Member = None):
    if member is None:
      member = ctx.message.author
    elif member.id == ctx.guild.owner.id:
      ppsize = ['```8=================D```', '```Oh my! Itz too big```']
    ppsize = [
      '```No PP found```', '```Too tiny```', '```8D```', '```8=D```',
      '```8==D```', '```8===D```', '```8====D```', '```8======D```',
      '```8=======D```', '```8======D```', '```8========D```',
      '```8=================D```', '```Oh my! Itz too big```'
    ]
    emb = discord.Embed(title="PP size",
                        colour=(discord.Colour.random()),
                        description=f'Here is {member.mention} pp size')
    emb.add_field(name='🍆', value=random.choice(ppsize))
    await ctx.channel.send(embed=emb)

  @commands.command(pass_content=True, aliases=['vs'])
  async def valorantstat(self, ctx, member: discord.Member = None):
    agents = [
      "Phoenix", "Raze", "Jett", "Yoru", "Neon", "Reyna", "Sage", "Cypher",
      "Chamber", "Killjoy", "Omen", "Viper", "Brimstone", "Astra", "Harbor",
      "Sova", "Breach", "Skye", "KAY/O", "Fade"
    ]
    valorole = ["Duelist", "Sentinel", "Initiator", "Controller"]
    rank = [
      "Iron 1", "Iron 2", "Iron 3", "Bronze 1", "Bronze 2", "Bronze 3",
      "Silver 1", "Silver 2", "Silver 3", "Gold 1", "Gold 2", "Gold 3",
      "Platinum 1", "Platinum 2", "Platinum 3", "Diamond 1", "Diamond 2",
      "Diamond 3", "Ascendant 1", "Ascendant 2", "Ascendant 3", "Immortal 1",
      "Immortal 2", "Immortal 3", "Radiant"
    ]
    kd = round(random.uniform(0.8, 3.0), 2)
    remarks = [
      "You are too noob to play Valorant", "Stop camping you looser",
      "Valorant, it's not for you", "You play good but you can do better",
      "Why don't you uninstall Valorant?",
      "Well you are doing good with your rank",
      "Focus on improving your aim you can do better",
      "Sheesh! You are a Real God!!! 👑",
      "Must say you are better than Sen Tenz",
      "Bro you should play candy crush", "You are a stupid lurker",
      "Baiter! Baiter spotted, a baiter a traitor", "Get a life dude!",
      "Your gameplay is shit, maybe you need to join RG",
      "Join RG and you can get to Immortal ez pz", "You deserve your rank",
      "Even a bot like me can defeat you in a 1v1",
      "You are a smart ass keep up!", "You are the G.O.A.T",
      "All must bow to the Aim God 🙌", "Sniper God, yes you are one",
      "Just stop complaining about your ping, even your pings plays better than you"
    ]
    if member is None and member.id != ctx.guild.owner.id:
      member = ctx.message.author
    elif member.id == ctx.guild.owner.id:
      rank = ["Immortal 1", "Immortal 2", "Immortal 3", "Radiant"]
      kd = round(random.uniform(1.9, 3.0), 2)
      remarks = [
        "Sheesh! You are a Real God 👑", "All must bow to the Aim God 🙌",
        "Sniper God, yes you are one", "My Owner is the RG in Valorant",
        "Must say you are better than Sen Tenz",
        "You are a smart ass keep up!", "You are the G.O.A.T"
      ]
    emb = discord.Embed(title="Valorant Stats",
                        colour=(discord.Colour.random()),
                        description=f'Here is {member.mention} Valorant Stats')
    emb.add_field(name='--------------',
                  value=f"ID: {member.name}#{member.discriminator}\n" +
                  f"Rank: {random.choice(rank)}\n" +
                  f"Agent: {random.choice(agents)}\n" + f"K/D: {kd}\n" +
                  f"**Remarks: {random.choice(remarks)}**",
                  inline=False)
    emb.set_thumbnail(
      url=
      "https://media.discordapp.net/attachments/708651332357324830/1078002431650177115/mn3yrpc10t761.png?width=473&height=473"
    )
    await ctx.channel.send(embed=emb)

  @commands.command(aliases=['mc'])
  async def memberCount(self, ctx):
    member_count = ctx.guild.member_count
    await ctx.channel.send(f"The server has {member_count} members.")


async def setup(client):
  await client.add_cog(fun(client))
