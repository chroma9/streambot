import os
import discord

from discord.ext import commands

from lib.reporter import Reporter
from lib.configuration import Configuration
from lib.twitch import TwitchSystem
from lib.formats import FormatSystem

# Might find a different way to do this later.
# Literally, too early to worry about this shoddy method.
# It works so I'll leave it for now.
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

config = Configuration()
report = Reporter()
twitch = TwitchSystem()
formats = FormatSystem()

@client.event
async def on_ready():
    # Temporary Job
    report.success("discord.process", "Discord client is ready!")


if __name__ == '__main__':
    report.info("discord.process", "Starting core system...")
    report.info("discord.process", "Loading message formats...")
    if os.path.exists('formats'):
        formats.load_formats()
        report.info("discord.process", "Message formats loaded successfully.")
    else:
        report.warn("discord.process", "No custom formats were found.")
        report.warn("discord.process", "Please check the documentation for more information.")
