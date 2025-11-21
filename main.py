# -------------------------
# IMPORTS (added logging & logger_setup)
# -------------------------
import discord
from webserver import keep_alive
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import tasks
import asyncio
import logging  # Logging
from logger_setup import setup_logging  # custom file to log into console + Discord channel

# -------------------------
# INTENTS & CLIENT SETUP
# -------------------------
intents = discord.Intents.all()
intents.members = True

load_dotenv()

client = commands.Bot(command_prefix='rg!', intents=intents)
client.remove_command('help')

# 🔹 SETUP LOGGING
LOG_CHANNEL_ID = 603237664686211072  # RG #serverlogs channel
setup_logging(client, LOG_CHANNEL_ID, logging.WARNING)
logger = logging.getLogger(__name__)

# -------------------------
# ON READY EVENT
# -------------------------
@client.event
async def on_ready():
    try:
        general_channel = client.get_channel(603237664686211072)
        if general_channel and isinstance(general_channel, discord.TextChannel):
            await general_channel.send("Hello World! Bot is now online")
        logger.info("Bot is now Online")

        if not status_change.is_running():  # prevents duplicate starts
            status_change.start()
    except Exception as e:
        logger.exception(f"Error in on_ready: {e}")

# -------------------------
# PRESENCE CHANGE LOOP (STATUS)
# -------------------------
@tasks.loop(seconds=10)
async def status_change():
    try:
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching, name="Real Gods Esports"))
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, name="rg!help"))
        await asyncio.sleep(20)
        await client.change_presence(activity=discord.Activity(
            type=discord.ActivityType.streaming, name="https://discord.gg/pUvnmRZ"))
        await asyncio.sleep(20)
    except Exception as e:
        logger.exception(f"Error in status_change: {e}")

@status_change.before_loop
async def before_status_change():
    await client.wait_until_ready()

# -------------------------
# LOAD / UNLOAD / RELOAD COMMANDS
# -------------------------
@client.command()
async def load(ctx, extension):
    owners = [829590898954207233, 403541270779265024]
    if ctx.author.id in owners:
        await client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully loaded **{extension}** :white_check_mark:')
        await ctx.message.delete()
        logger.info(f"Loaded extension: {extension}")
    else:
        await ctx.send("Oops! You cannot use this command.")
        await ctx.message.delete()

@client.command()
async def unload(ctx, extension):
    owners = [829590898954207233, 403541270779265024]
    if ctx.author.id in owners:
        await client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully unloaded **{extension}** :white_check_mark:')
        await ctx.message.delete()
        logger.info(f"Unloaded extension: {extension}")
    else:
        await ctx.send("Oops! You cannot use this command.")
        await ctx.message.delete()

@client.command()
async def reload(ctx, extension):
    owners = [829590898954207233, 403541270779265024]
    if ctx.author.id in owners:
        await client.unload_extension(f'cogs.{extension}')
        await client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Successfully reloaded **{extension}** :white_check_mark:')
        await ctx.message.delete()
        logger.info(f"Reloaded extension: {extension}")
    else:
        await ctx.send("Oops! You cannot use this command.")
        await ctx.message.delete()

# -------------------------
# CRASHTEST COMMAND (TEST RESTART)
# -------------------------
@client.command()
async def crashtest(ctx):
    owners = [829590898954207233, 403541270779265024]
    if ctx.author.id not in owners:
        await ctx.send("❌ You do not have permission to use this command.")
        return

    await ctx.send("⚠️ Simulating bot crash...")

    # 🔹 Stop status loop BEFORE closing bot
    if status_change.is_running():
        status_change.cancel()

    await client.close()  # Clean shutdown (restart handled by main loop)

# -------------------------
# LOAD ALL COGS (LOAD ONCE ONLY!)
# -------------------------
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await client.load_extension(f'cogs.{filename[:-3]}')
                logger.info(f"Loaded cog: {filename}")
            except Exception:
                logger.warning(f"Skipped loading {filename} (already loaded)")

# -------------------------
# ON COMMAND ERROR
# -------------------------
@client.event
async def on_command_error(ctx, error):
    try:
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f":stopwatch: Cooldown: **{error.retry_after:.2f}** seconds.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f":x: You need: {', '.join(error.missing_permissions)}")
        elif isinstance(error, discord.HTTPException) and error.status == 429:
            logger.warning(f"Rate limited! Retry after: {getattr(error, 'retry_after', 'unknown')}")
            await asyncio.sleep(getattr(error, 'retry_after', 5) or 5)
        else:
            logger.exception(f"Unhandled error: {error}")
    except Exception as e:
        logger.exception(f"Error in error handler: {e}")

# -------------------------
# DC / RECONNECT EVENTS
# -------------------------
@client.event
async def on_disconnect():
    logger.warning("Bot disconnected from Discord Gateway")

@client.event
async def on_resumed():
    logger.warning("Bot reconnected to Discord Gateway")

# -------------------------
# KEEP ALIVE (REPL ONLY)
# -------------------------
keep_alive()

# -------------------------
# MAIN RESTART LOOP
# -------------------------
TOKEN = os.environ['TOKEN']

async def main():
    await load_extensions()  # 🔹 Load ONCE ONLY

    while True:  # 🔁 Restart protection
        try:
            async with client:
                logger.info("Starting bot...")
                await client.start(TOKEN)

        except discord.ConnectionClosed:
            logger.warning("Connection closed, reconnecting...")
            await asyncio.sleep(5)

        except discord.HTTPException as e:
            if getattr(e, 'status', None) == 429:
                wait_time = getattr(e, 'retry_after', 60) or 60
                logger.warning(f"Rate limited globally, waiting {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            else:
                logger.exception(f"HTTP exception: {e}")
                await asyncio.sleep(10)

        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            await asyncio.sleep(15)

        logger.info("Attempting to restart bot...")

# -------------------------
# START BOT
# -------------------------
asyncio.run(main())
