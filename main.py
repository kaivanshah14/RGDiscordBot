# main.py
# -------------------------
# IMPORTS (keeps your original names & intent)
# -------------------------
import discord
from webserver import keep_alive
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import tasks
import asyncio
import logging
from logger_setup import setup_logging  # expects the logger_setup.py you already have
import logger_setup  # <-- IMPORTANT (so we can set SHUTTING_DOWN)

# -------------------------
# CONFIG / GLOBALS (original names preserved)
# -------------------------
load_dotenv()
TOKEN = os.environ.get('TOKEN')
LOG_CHANNEL_ID = 603237664686211072

client = None
logger = None

# -------------------------
# STATUS TASK
# -------------------------
@tasks.loop(seconds=10)
async def status_change():
    if client is None or getattr(client, "is_closed", lambda: True)():
        return
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
        if logger:
            logger.exception(f"Error in status_change: {e}")
        else:
            print(f"Error in status_change: {e}")

@status_change.before_loop
async def before_status_change():
    while client is None:
        await asyncio.sleep(0.5)
    await client.wait_until_ready()

# -------------------------
# CREATE CLIENT
# -------------------------
async def create_client():
    global client, logger

    intents = discord.Intents.all()
    intents.members = True

    client = commands.Bot(command_prefix='rg!', intents=intents)
    client.remove_command('help')

    setup_logging(client, LOG_CHANNEL_ID, logging.WARNING)
    logger = logging.getLogger(__name__)

    @client.event
    async def on_ready():
        try:
            general_channel = client.get_channel(LOG_CHANNEL_ID)
            if general_channel and isinstance(general_channel, discord.TextChannel):
                await general_channel.send("Hello World! Bot is now online")
            logger.info("Bot is now Online")

            if not status_change.is_running():
                status_change.start()
        except Exception as e:
            logger.exception(f"Error in on_ready: {e}")

    @client.event
    async def on_disconnect():
        logger.warning("Bot disconnected from Discord Gateway")
        if status_change.is_running():
            try:
                status_change.cancel()
            except Exception:
                pass

    @client.event
    async def on_resumed():
        logger.info("Bot reconnected to Discord Gateway")

    @client.event
    async def on_command_error(ctx, error):
        try:
            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f":stopwatch: Command is on Cooldown for **{error.retry_after:.2f}** seconds.")
            elif isinstance(error, commands.MissingPermissions):
                await ctx.send(f":x: You need the following perms: {', '.join(error.missing_permissions)}")
            elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Required arguments are not passed ❌")
            elif isinstance(error, commands.CommandNotFound):
                await ctx.send("Command not found. ❌")
            elif isinstance(error, commands.BadArgument):
                await ctx.send("One or more arguments are of the wrong type.")
            elif isinstance(error, commands.DisabledCommand):
                await ctx.send(f'{ctx.command} has been disabled. ❌')
            elif isinstance(error, discord.HTTPException) and getattr(error, "status", None) == 429:
                logger.warning(f"Rate limited! Retry after: {getattr(error, 'retry_after', 'unknown')}")
                await asyncio.sleep(getattr(error, 'retry_after', 5) or 5)
            else:
                logger.exception(f"Unhandled error: {error}")
        except Exception as e:
            logger.exception(f"Error in error handler: {e}")

    # -------------------------
    # COMMANDS
    # -------------------------
    @client.command()
    async def load(ctx, extension):
        owners = [829590898954207233, 403541270779265024]
        if ctx.author.id in owners:
            try:
                await client.load_extension(f'cogs.{extension}')
                await ctx.send(f'Successfully loaded **{extension}** :white_check_mark:')
                await ctx.message.delete()
                logger.info(f"Loaded extension: {extension}")
            except Exception as e:
                logger.exception(f"Error loading extension {extension}: {e}")
                await ctx.send(f"❌ Error loading {extension}")
        else:
            await ctx.send("Oops! You cannot use this command.")
            await ctx.message.delete()

    @client.command()
    async def unload(ctx, extension):
        owners = [829590898954207233, 403541270779265024]
        if ctx.author.id in owners:
            try:
                await client.unload_extension(f'cogs.{extension}')
                await ctx.send(f'Successfully unloaded **{extension}** :white_check_mark:')
                await ctx.message.delete()
                logger.info(f"Unloaded extension: {extension}")
            except Exception as e:
                logger.exception(f"Error unloading extension {extension}: {e}")
                await ctx.send(f"❌ Error unloading {extension}")
        else:
            await ctx.send("Oops! You cannot use this command.")
            await ctx.message.delete()

    @client.command()
    async def reload(ctx, extension):
        owners = [829590898954207233, 403541270779265024]
        if ctx.author.id in owners:
            try:
                await client.unload_extension(f'cogs.{extension}')
                await client.load_extension(f'cogs.{extension}')
                await ctx.send(f'Successfully reloaded **{extension}** :white_check_mark:')
                await ctx.message.delete()
                logger.info(f"Reloaded extension: {extension}")
            except Exception as e:
                logger.exception(f"Error reloading extension {extension}: {e}")
                await ctx.send(f"❌ Error reloading {extension}")
        else:
            await ctx.send("Oops! You cannot use this command.")
            await ctx.message.delete()

    @client.command()
    async def crashtest(ctx):
        owners = [829590898954207233, 403541270779265024]
        if ctx.author.id not in owners:
            await ctx.send("❌ You do not have permission to use this command.")
            return

        await ctx.send("⚠️ Simulating bot crash...")
        if status_change.is_running():
            try:
                status_change.cancel()
            except Exception:
                pass

        logger_setup.SHUTTING_DOWN = True  # <-- FIXED HERE
        await client.close()  # restart safely

    return client

# -------------------------
# LOAD COGS
# -------------------------
async def load_extensions_for_client():
    if client is None:
        return
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await client.load_extension(f'cogs.{filename[:-3]}')
                logger.info(f"Loaded cog: {filename}")
            except Exception as e:
                logger.warning(f"Skipped loading {filename}: {e}")

# -------------------------
# KEEP ALIVE
# -------------------------
keep_alive()

# -------------------------
# MAIN LOOP
# -------------------------
async def main():
    global client, logger
    if TOKEN is None:
        print("DISCORD token not found — exiting.")
        return

    while True:
        await create_client()
        try:
            await load_extensions_for_client()
            async with client:
                logger.info("Starting bot...")
                await client.start(TOKEN)

        except Exception as e:
            logger.exception(f"Unexpected error in main loop: {e}")
            await asyncio.sleep(10)

        logger.info("Attempting restart in 5s...")
        await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
