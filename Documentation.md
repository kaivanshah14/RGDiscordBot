
**🧾 logger_setup.py – Documentation**
**Purpose**
This file configures logging so:
Logs appear in console
Logs appear in a Discord channel
Crashes are reported safely

**How It Works**
| Part                      | Purpose                                   |
| ------------------------- | ----------------------------------------- |
| `logging.StreamHandler()` | Sends logs to terminal                    |
| `DiscordHandler`          | Custom handler that sends logs to Discord |
| `sys.excepthook`          | Detects unhandled crashes & logs them     |
| `setup_logging()`         | Main function to initialize everything    |

How to Use in main.py
from logger_setup import setup_logging
setup_logging(bot, channel_id=603237664686211072, level=logging.WARNING)

✔ This activates logging
✔ All warnings & errors go to Discord
✔ Console still shows logs

**🧾 main.py - Documentation**
**Purpose**

This file:
✔ Starts the bot
✔ Loads cogs
✔ Sets up logging
✔ Starts Discord status loop
✔ Connects UptimeRobot ping server (optional for Replit)

* What Happens When Bot Starts
* Logging is activated (console + Discord)
* Bot connects to Discord
* Status starts changing every 60 sec
* Cogs are loaded
* Errors are caught and reported in logs

Flowchart
User starts bot →
  setup_logging() →
  connect to Discord →
  on_ready() called →
  status loop begins →
  cogs load →
  bot runs until forced stop
