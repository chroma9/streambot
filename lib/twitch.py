import requests

class TwitchSystem:
    def __init__(self):
        self.live_streams = []

    def is_broadcast_live(self, username):
        url = str(f'https://www.twitch.tv/{username}')
        content = requests.get(url).content.decode('utf-8')
        if 'isLiveBroadcast' in content:
            return True
        else:
            return False

    def current_live_streams(self):
        return self.live_streams