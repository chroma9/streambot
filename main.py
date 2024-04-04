import discord

from discord.ext import commands

from lib.reporter import Reporter

# Might find a different way to do this later. Not enough coffee ATM.
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

report = Reporter()

@client.event
async def on_ready():
    print(f"Connected as {client.user.id}")

if __name__ == '__main__':
    pass