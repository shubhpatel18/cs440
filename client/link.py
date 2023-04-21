import os

from common.config_reader import read_config

from PyQt5.QtCore import QObject

class Link(QObject):
    def __init__(self):
        super().__init__()

        self.username = ""

        self.server_address, self.server_port, self.server_cert = self.read_config()

    def read_config(self):
        client_path = os.path.dirname(os.path.realpath(__file__))

        config_file_path = os.path.join(client_path, 'resources', 'config.yaml')
        config = read_config(config_file_path)
        server_address = config['server']['address']
        server_port = config['server']['port']
        server_cert_rel_path = config['server']['certfile']

        server_cert = os.path.join(client_path, server_cert_rel_path)

        return server_address, server_port, server_cert
