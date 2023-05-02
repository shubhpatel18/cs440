import os
import json

from common.config_reader import read_config

from PyQt5.QtCore import QObject

class Link(QObject):
    def __init__(self):
        super().__init__()

        self.username = ""

        self.server_address, self.server_port, self.server_cert = self.read_config()

        # weights
        self.receptions = 0.0
        self.tfl = 0.0
        self.yards = 0.0
        self.interceptions = 0.0
        self.touchdowns = 0.0
        self.fumbles = 0.0
        self.turnovers = 0.0
        self.punting_yards = 0.0
        self.sacks = 0.0
        self.fg_percentage = 0.0

        self.get_file_weights()

    def read_config(self):
        client_path = os.path.dirname(os.path.realpath(__file__))

        config_file_path = os.path.join(client_path, 'resources', 'config.yaml')
        config = read_config(config_file_path)
        server_address = config['server']['address']
        server_port = config['server']['port']
        server_cert_rel_path = config['server']['certfile']

        server_cert = os.path.join(client_path, server_cert_rel_path)

        return server_address, server_port, server_cert
    
    def get_file_weights(self):
        if os.path.isfile("client/resources/weights.json"):
            with open("client/resources/weights.json", "r") as outfile:
                data = json.load(outfile)

            self.receptions = data["receptions"]
            self.tfl = data["tackles for loss"]
            self.yards = data["total yards"]
            self.interceptions = data["interceptions"]
            self.touchdowns = data["touchdowns"]
            self.fumbles = data["fumbles recovered"]
            self.turnovers = data["turnovers lost"]
            self.punting_yards = data["punting yards"]
            self.sacks = data["sacks"]
            self.fg_percentage = data["field_goal_percentage"]
