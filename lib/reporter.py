from datetime import datetime

from lib.configuration import config

class Reporter:
    def __init__(self):
        self.output_to_file = config.get_bool('LOGGING', 'output_to_file')

        self.file_dir = str('logs')
        self.file_name = str('0000-00-00.log')
        self.file_path = str(f'{self.file_dir}/{self.file_name}')
        self.file = None
    
    def _update_file(self):
        date = datetime.now()

        self.file_name = date.strftime('%Y-%m-%d.log')
        self.file_path = str(f'{self.file_dir}/{self.file_name}')
        self.file = open(self.file_path, 'a')
    
    def warn(self, event, message):
        self._log('warn', event, message)

    def error(self, event, message):
        self._log('error', event, message)

    def info(self, event, message):
        self._log('info', event, message)
    
    def success(self, event, message):
        self._log('success', event, message)
    
    def _log(self, type, event, message):
        if self.output_to_file:
            self._update_file()
        
        styling = {}
        styling['reset'] = '\033[0m'
        styling['bold'] = '\033[1m'
        styling['time'] = '\033[90m' + styling['bold']
        styling['info'] = '\033[94m' + styling['bold']
        styling['error'] = '\033[91m' + styling['bold']
        styling['success'] = '\033[92m' + styling['bold']
        styling['event'] = '\033[35m'

        date_template = str(f'%Y-%m-%d %H:%M:%S')
        timestamp = datetime.now()

        ts_current = timestamp.strftime(date_template)
        ts_color = str(f'{styling['time']}{ts_current}{styling['reset']}')

        type_upper = str(f'{type}').upper().ljust(8, ' ')
        type_color = str(f'{styling[type]}{type_upper}{styling['reset']}')

        evn_color = str(f'{styling['event']}{event}{styling['reset']}')

        print(f'{ts_color} {type_color} {evn_color} {message}')

        if self.output_to_file:
            self.file.write(f'{ts_current} {type_upper} {event} {message}\n')
