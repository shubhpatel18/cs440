import os
import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.edit_team import Ui_EditTeamDialog
from link import Link

#self.link.username is current user

class EditTeamDialog(QDialog):
    def __init__(self, link: Link, team_name: str):
        super().__init__()

        self.link = link

        self.cancel = False
        self.valid = False
        self.success = False

        self.edit_team = Ui_EditTeamDialog()
        self.edit_team.setupUi(self)

        self.ok_button = self.edit_team.buttonBox
        self.ok_button.accepted.connect(lambda: self.change_team_name(team_name, self.edit_team.edit_team_input.text()))
        self.cancel_button = self.edit_team.buttonBox
        self.cancel_button.rejected.connect(lambda: self.cancel_change())


    def change_team_name(self, team_name, new_name):

        url = f'{self.link.server_address}:{self.link.server_port}/rename_fantasy_team'
        post_data = {
            'team_name': team_name,
            'new_team_name': new_name,
            'username': self.link.username,
        }

        r = requests.post(url=url, json=post_data, verify=self.link.server_cert)
        data = r.json()

        if data['valid_request'] == True:
            self.valid = True

        if data['rename_team_successful'] == True:
            self.success = True

    def cancel_change(self):
        self.cancel = True
