# main.py
# -------------------------
# IMPORTS
# -------------------------
import discord
from webserver import keep_alive
import os
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import tasks
import asyncio
import logging
from logger_setup import setup_logging
import logger_setup

# -------------------------
# CONFIG / GLOBALS
# -------------------------
load_dotenv()
TOKEN = os.environ.get('TOKEN')
LOG_CHANNEL_ID = 603237664686211072

client = None
logger = None

# -------------------------
# STATUS TASK (FIXED)
# -------------------------
@tasks.loop(minutes=1)
async def status_change():
    """Rotates bot status every minute"""
    if client is None or client.is_closed():
        return
    try:
        statuses = [
            discord.Activity(type=discord.ActivityType.watching, name="Real Gods Esports"),
            discord.Activity(type=discord.ActivityType.listening, name="rg!help"),
            discord.Activity(type=discord.ActivityType.streaming, name="https://discord.gg/pUvnmRZ"),
        ]
        status = statuses[status_change.current_loop % len(statuses)]
        await client.change_presence(activity=status)
    except Exception as e:
        if logger:
            logger.exception(f"Error in status_change: {e}")

@status_change.before_loop
async def before_status_change():
    while client is None or client.is_closed():
        await asyncio.sleep(1)
    await client.wait_until_ready()

# -------------------------
# HEARTBEAT MONITOR (NEW)
# -------------------------
@tasks.loop(seconds=30)
async def heartbeat_monitor():
    """Monitors bot connection health"""
    if client is None or client.is_closed():
        return
    try:
        # Simple ping to keep connection alive
        if not client.latency or client.latency > 10:
            if logger:
                logger.warning(f"High latency detected: {client.latency:.2f}s")
    except Exception as e:
        if logger:
            logger.exception(f"Error in heartbeat_monitor: {e}")

@heartbeat_monitor.before_loop
async def before_heartbeat():
    while client is None or client.is_closed():
        await asyncio.sleep(1)
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
            # Stop any existing tasks to prevent duplication
            if status_change.is_running():
                status_change.cancel()
            if heartbeat_monitor.is_running():
                heartbeat_monitor.cancel()
            
            # Start tasks fresh
            status_change.start()
            heartbeat_monitor.start()
            
            general_channel = client.get_channel(LOG_CHANNEL_ID)
            if general_channel and isinstance(general_channel, discord.TextChannel):
                await general_channel.send("Hello World! Bot is now online")
            logger.info("Bot is now Online")
        except Exception as e:
            logger.exception(f"Error in on_ready: {e}")

    @client.event
    async def on_disconnect():
        logger.warning("Bot disconnected from Discord Gateway")
        # Stop background tasks on disconnect
        if status_change.is_running():
            try:
                status_change.cancel()
            except Exception:
                pass
        if heartbeat_monitor.is_running():
            try:
                heartbeat_monitor.cancel()
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
        if heartbeat_monitor.is_running():
            try:
                heartbeat_monitor.cancel()
            except Exception:
                pass

        logger_setup.SHUTTING_DOWN = True
        await client.close()

    return client

# -------------------------
# LOAD COGS
# -------------------------
async def load_extensions_for_client():
    global client, logger
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
# MAIN LOOP (IMPROVED)
# -------------------------
async def main():
    global client, logger
    if TOKEN is None:
        print("DISCORD token not found — exiting.")
        return

    retry_count = 0
    max_retries = 5
    
    while True:
        try:
            await create_client()
            retry_count = 0  # Reset on successful creation
            
            await load_extensions_for_client()
            logger.info("Starting bot...")
            
            async with client:
                await client.start(TOKEN)

        except asyncio.TimeoutError:
            retry_count += 1
            wait_time = min(10 * (2 ** retry_count), 300)  # Exponential backoff, max 5 min
            logger.error(f"Connection timeout (attempt {retry_count}). Retrying in {wait_time}s...")
            await asyncio.sleep(wait_time)
            
        except discord.ConnectionClosed as e:
            retry_count += 1
            wait_time = min(5 * (2 ** retry_count), 300)
            logger.error(f"Discord connection closed (code: {e.code}). Retrying in {wait_time}s...")
            await asyncio.sleep(wait_time)
            
        except discord.PrivilegedIntentsRequired:
            logger.critical("Privileged intents are required but not granted. Check Discord Developer Portal.")
            return
            
        except Exception as e:
            retry_count += 1
            wait_time = min(10 * (2 ** retry_count), 300)
            logger.exception(f"Unexpected error in main loop (attempt {retry_count}): {e}")
            logger.info(f"Retrying in {wait_time}s...")
            await asyncio.sleep(wait_time)
            
            if retry_count > max_retries:
                logger.critical(f"Max retries ({max_retries}) exceeded. Stopping bot.")
                return

if __name__ == '__main__':
    asyncio.run(main())
