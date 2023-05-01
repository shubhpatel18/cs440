import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_python.create_new_team_dialog import Ui_CreateNewTeamDialog
from link import Link
import another_window

class CreateNewTeamDialog(QDialog):
    def __init__(self, link: Link):
        super().__init__()

        self.link = link

        self.create_new_team_dialog = Ui_CreateNewTeamDialog()
        self.create_new_team_dialog.setupUi(self)

        self.ok_button = self.create_new_team_dialog.buttonBox
        self.ok_button.accepted.connect(lambda: self.create_team(self.create_new_team_dialog.team_name_edit.text()))


    def create_team(self, team_name):
        # TODO:
        # Check if team already exists

        # If team name does not already exist
        url = f'{self.link.server_address}:{self.link.server_port}/create_fantasy_team'
        data = {
            'team_name': team_name,
            'username': self.link.username,
        }

        r = requests.post(url=url, json=data, verify=self.link.server_cert)
        data = r.json()
