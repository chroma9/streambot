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
    print(f"Connected as {client.user.id}")

if __name__ == '__main__':
    formats.load_formats()
