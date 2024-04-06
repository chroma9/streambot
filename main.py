import os
import discord
import requests
import time

from discord.ext import commands

from lib.reporter import Reporter
from lib.configuration import Configuration
from lib.formats import FormatSystem

# Might find a different way to do this later.
# Literally, too early to worry about this shoddy method.
# It works so I'll leave it for now.
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

config = Configuration()
report = Reporter()
formats = FormatSystem()

live_streams = []

@client.event
async def on_ready():
    # Temporary Job
    report.success("discord.process", "Discord client is ready!")

# This was a class earlier. I have no idea why I 
# overcomplicated this.
def stream_is_live(username):
    url = str(f'https://www.twitch.tv/{username}')
    content = requests.get(url).content.decode('utf-8')
    if 'isLiveBroadcast' in content:
        return True
    else:
        return False
    
def broadcast_live_stream(message):
    channel_ids = config.get_list('DISCORD', 'channel_ids')
    for channel_id in channel_ids:
        channel = client.get_channel(int(channel_id))
        channel.send(message)

def check_live_streams():
    usernames = config.get_list('TWITCH', 'usernames')
    for un in usernames:
        if stream_is_live(un):
            if not un in live_streams:
                report.info("twitch.process", f"{un} is now live!")
                live_streams.append(un)
                mform = formats.get_message_format(un)
                message = mform.replace('[USERNAME]', un)
                broadcast_live_stream(message)
        else:
            if un in live_streams:
                report.info("twitch.process", f"{un} has gone offline!")
                live_streams.remove(un)

def stream_check_loop():
    while True:
        check_live_streams()
        time.sleep(60 * 5)


if __name__ == '__main__':
    report.info("discord.process", "Starting core system...")
    report.info("discord.process", "Loading message formats...")
    if os.path.exists('formats'):
        formats.load_formats()
        report.info("discord.process", "Message formats loaded successfully.")
    else:
        report.warn("discord.process", "No custom formats were found.")
        report.warn("discord.process", "Please check the documentation for more information.")
