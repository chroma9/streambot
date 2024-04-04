from configparser import ConfigParser

class Configuration:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('config.ini')
    
    def get_string(self, section, key):
        return self.config.get(section, key)
    
    def get_list(self, section, key):
        return self.get_string(section, key).split(',')
    
    def get_int(self, section, key):
        return int(self.get_string(section, key))
    
    def get_float(self, section, key):
        return float(self.get_string(section, key))
    
    def get_bool(self, section, key):
        return self.get_string(section, key).lower() == str('true')
    
    def set_value(self, section, key, value):
        self.config.set(section, key, value)
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)