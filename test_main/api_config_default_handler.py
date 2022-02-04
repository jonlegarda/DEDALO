import configparser

class ApiKeyShodanDefaultConfig:

    # variables of the config file & api key.
    config_file_name = '../config/config.cfg'
    api_key = ""


    # ApiKeyShodanDefaultConfig initializer: reads the config file and ass
    def __init__(self):
        config_file = configparser.ConfigParser()
        config_file.read(self.config_file_name)
        self.api_key = config_file['SHODAN']['API_SHODAN']
        print("Class initializer: ApiKeyShodanDefaultConfig | Api-Key = {}".format(self.api_key))


    # returns the api key string initialized before
    def get_api_key(self):
        return self.api_key


class ApiKeyZoomeyeDefaultConfig:

    # variables of the config file & api key.
    config_file_name = '../config/config.cfg'
    api_key = ""


    # ApiKeyZoomeyeDefaultConfig initializer: reads the config file and ass
    def __init__(self):
        config_file = configparser.ConfigParser()
        config_file.read(self.config_file_name)
        self.api_key = config_file['ZOOMEYE']['API_ZOOMEYE']
        print("Class initializer: ApiKeyZoomeyeDefaultConfig | Api-Key = {}".format(self.api_key))

    # returns the api key string initialized before
    def get_api_key(self):
        return self.api_key