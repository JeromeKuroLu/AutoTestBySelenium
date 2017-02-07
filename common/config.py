import json

class GlobalConfig():
    def __init__(self, config_dir='../static/config.json'):
        self._config_dir = config_dir

    def load(self):
        with open(self._config_dir) as config_data:
            config = json.load(config_data)
        print(config)
        self.profile_dir = config['firefox']['profile']
        self.extension_dir = config['firefox']['auto_auth_extension']