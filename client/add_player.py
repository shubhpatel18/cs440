import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_python.add_player import Ui_AddPlayerDialog
from link import Link

from common.translations import POSITION_TO_ROLES

def uppercase(s: str):
    return s.upper()

class AddPlayerDialog(QDialog):
    def __init__(self, link: Link, player_name, player_position, team_name):
        super().__init__()

        self.link = link

        self.add_player_dialog = Ui_AddPlayerDialog()
        self.add_player_dialog.setupUi(self)

        self.ok_button = self.add_player_dialog.buttonBox
        self.ok_button.accepted.connect(lambda: self.add_player(player_name, player_position, team_name))
        self.successful = False

        self.add_player_dialog.comboBox.clear()
        self.add_player_dialog.comboBox.addItems(list(map(uppercase, POSITION_TO_ROLES[player_position])))

    def add_player(self, player_name, player_position, team_name):

        team_role = self.add_player_dialog.comboBox.currentText().lower()
    
        url = f'{self.link.server_address}:{self.link.server_port}/set_player'
        data = {
            'player_name': player_name,
            'player_position': player_position,
            'team_role': team_role,
            'team_name': team_name,
            'username': self.link.username,
        }

        r = requests.post(url=url, json=data, verify=self.link.server_cert)
        data = r.json()
        
        if data['add_player_successful'] == True:
            self.successful = True
