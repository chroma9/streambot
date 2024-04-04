import os as OS

default_format = '''
**[USERNAME]** is now live on Twitch! 
CCome watch them live: https://www.twitch.tv/[USERNAME]
'''

class FormatSystem:
    def __init__(self):
        self.directory = str('formats')
        self.formats = {}

        self.formats['default'] = default_format

    def load_formats(self):
        for file in OS.listdir(self.directory):
            if file.endswith('.txt'):
                path = str(f'{self.directory}/{file}')
                name = file[:-4]
                self.load_format_file(path, name)
    
    def load_format_file(self, path, name):
        with open(path, 'r') as file:
            self.formats[name] = file.read()
    
    def get_message_format(self, username):
        if username in self.formats:
            return self.formats[username]
        else:
            return self.formats['default']
            