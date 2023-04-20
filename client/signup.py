import os
import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.signup_dialog import Ui_SignupDialog
from link import Link
from config_reader import read_config

class SignupDialog(QDialog):
    def __init__(self, link: Link):
        super().__init__()

        self.link = link
        
        self.cancel = False
        self.valid = False
        self.username_taken = True
        self.success = False

        self.signup_dialog = Ui_SignupDialog()
        self.signup_dialog.setupUi(self)
        
        self.ok_button = self.signup_dialog.buttonBox
        self.ok_button.accepted.connect(lambda: self.configure_credentials(self.signup_dialog.username_edit.text(), self.signup_dialog.name_edit.text(), self.signup_dialog.password_edit.text()))
       
        self.cancel_button = self.signup_dialog.buttonBox
        self.cancel_button.rejected.connect(lambda: self.cancel_signup())
        
    def configure_credentials(self, username, name, password):
        url = f'{self.link.server_address}:{self.link.server_port}/signup'
        post_data = {
            'username': username,
            'name': name,
            'password': password,
        }

        r = requests.post(url=url, json=post_data, verify=self.link.server_cert)
        data = r.json()
        
        self.success = data['signup_successful']
        self.username_taken = data['username_taken']
        self.valid = data['valid_request']
        
        if self.success:
            self.link.username = username
            
    def cancel_signup(self):
        self.cancel = True
