import os

from config_reader import read_config

from PyQt5.QtCore import QObject

class Link(QObject):
    def __init__(self):
        super().__init__()

        self.username = ""

        self.server_address, self.server_port, self.server_cert = self.read_config()

    def read_config(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
        config = read_config(config_file_path)
        server_address = config['server']['address']
        server_port = config['server']['port']
        server_cert_rel_path = config['server']['certfile']

        file_path = os.path.dirname(__file__)
        server_cert = os.path.join(file_path, server_cert_rel_path)

        return server_address, server_port, server_cert
