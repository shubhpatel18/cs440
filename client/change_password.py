import os
import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.change_password_dialog import Ui_ChangePasswordDialog
from link import Link
from config_reader import read_config

#self.link.username is current user

class ChangePasswordDialog(QDialog):
    def __init__(self, link: Link):
        super().__init__()

        self.link = link

        self.cancel = False
        self.valid = False
        self.success = False

        self.change_password_dialog = Ui_ChangePasswordDialog()
        self.change_password_dialog.setupUi(self)

        self.ok_button = self.change_password_dialog.buttonBox
        self.ok_button.accepted.connect(lambda: self.verify_credentials(self.link.username, self.change_password_dialog.current_password_edit.text(), self.change_password_dialog.new_password_edit_1.text(),self.change_password_dialog.new_password_edit_2.text()))
        self.cancel_button = self.change_password_dialog.buttonBox
        self.cancel_button.rejected.connect(lambda: self.cancel_password_change())


    def change_password(self, username, current_password, new_password, new_password_verify):
        if new_password != new_password_verify:
            self.cancel_password_change()

        url = f'{self.link.server_address}:{self.link.server_port}/change_password'
        post_data = {
            'username':username,
            'old_password':current_password,
            'new_password':new_password,
        }

        r = requests.post(url=url, json=post_data, verify=self.link.server_cert)
        data = r.json()
        print(data)

        if data['valid_request'] == True:
            self.valid = True

        if data['password_change_successful'] == True:
            self.success = True

    def cancel_password_change(self):
        self.cancel = True
