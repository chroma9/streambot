import requests

class TwitchSystem:
    def __init__(self):
        self.live_streams = []

    def is_broadcast_live(self, username):
        url = str(f'https://www.twitch.tv/{username}')
        content = requests.get(url).content.decode('utf-8')
        if 'isLiveBroadcast' in content:
            if username in self.live_streams:
                return True
            else:
                self.live_streams.append(username)
                return True
        else:
            if username in self.live_streams:
                self.live_streams.remove(username)
            return False

    def current_live_streams(self):
        return self.live_streams