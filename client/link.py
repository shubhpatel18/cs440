import os

from config_reader import read_config

from PyQt5.QtCore import QObject

class Link(QObject):
    def __init__(self):
        super().__init__()

        self.username = ""

        self.server_address, self.server_port = self.get_address_port()

    def get_address_port(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
        config = read_config(config_file_path)

        server_address = config['server']['address']
        server_port = config['server']['port']

        return server_address, server_port