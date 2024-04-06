# streambot

![Python Version](https://img.shields.io/static/v1?label=Python&message=3.11.5&color=%232b5b84&logo=python&logoColor=ffffff)

### Description
This is a very simple bot that shares custom messages to Discord channels when a user goes live on [twitch.tv](https://www.twitch.tv/). The configuration and setup is simple but requires the user to create the bot themselves in the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation
This bot requires Python 3.11 or higher to install. You can get this version of Python [here](https://www.python.org/downloads/release/python-3116/). Outside of this, you need to install the required packages using the following command from a terminal:
```bash
pip install -r requirements.txt
```

### Setup
1. Create a new bot in the [Discord Developer Portal](https://discord.com/developers/applications).
2. Use the newly generated bot credentials and put them under the `DISCORD` section of the `config.ini` file.
3. Under the `DISCORD` section of the `config.ini` file, put the Channel ID's (seperated by a comma).
4. Under the `TWITCH` section of the `config.ini` file, put the Twitch usernames (seperated by a comma).

### Message Formats
With this bot, you can create simple message formats per username in the bot. There is a default message that
will be used if no format is specified. If you want to use your own formats per username create a directory called
`formats` in the root of this project and create a file with the `username.txt` of the user you want to create a custom
message for. The contents of the file should be the message you want to send to the Discord channel. Please note that
in the format, `[USERNAME]` will be replaced with the username of the user that went live.

NOTE: You can also change the default message format by creating a file called `default.txt` in the `formats` directory.


### Notes
This bot was created out of necessity as many other bots were not doing what we needed to the extent that we needed amongst my few friends without a subscription to some premium service. This bot is not meant to be a replacement for any other bot, but rather a simple solution for a small group of friends.