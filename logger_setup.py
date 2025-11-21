# logger_setup.py (UPDATED & SAFE)
import logging
import asyncio
import sys
import time

DISCORD_LOG_CHANNEL_ID = 603237664686211072
_bot = None  # Stores bot instance (so logger can use it later)
_last_sent_time = 0  # To prevent spam / rate limiting
_rate_limit_seconds = 2  # Min gap between log messages
SHUTTING_DOWN = False

class DiscordHandler(logging.Handler):
    def emit(self, record):
        if SHUTTING_DOWN:
            return
        try:
            msg = self.format(record)

            # Prevent recursive logging
            if "discord_handler" in msg.lower():
                return

            # Prevent rate spam
            global _last_sent_time
            if time.time() - _last_sent_time < _rate_limit_seconds:
                return

            _last_sent_time = time.time()
            asyncio.create_task(self._send_to_discord(msg))

        except Exception:
            # Prevent crashing from logger errors
            print("Error in DiscordHandler – falling back to console logging.")
            pass

    async def _send_to_discord(self, msg):
        await _bot.wait_until_ready()
        channel = _bot.get_channel(DISCORD_LOG_CHANNEL_ID)

        if channel is None:
            print(f"[LOGGER] ERROR: Could not find Discord channel {DISCORD_LOG_CHANNEL_ID}.")
            return  # Do NOT let bot crash

        try:
            # Discord can only send max 2000 characters
            await channel.send(f"```{msg[:1900]}```")
        except Exception as e:
            print(f"[LOGGER] Failed to send log to Discord: {e}")

def setup_logging(bot, channel_id, level=logging.INFO):
    global _bot, DISCORD_LOG_CHANNEL_ID
    _bot = bot
    DISCORD_LOG_CHANNEL_ID = channel_id

    log = logging.getLogger()
    log.setLevel(level)

    # Console logging (always works)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))
    log.addHandler(console_handler)

    # Add Discord Logging
    discord_handler = DiscordHandler()
    discord_handler.setLevel(level)
    log.addHandler(discord_handler)

    # Catch ALL unhandled errors
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        logging.critical("UNHANDLED EXCEPTION", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = handle_exception
    print("[LOGGER] Logging system initialized successfully.")