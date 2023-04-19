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
        
        self.unique_username = False
        self.success = False

        self.signup_dialog = Ui_SignupDialog()
        self.signup_dialog.setupUi(self)
        
        self.ok_button = self.signup_dialog.buttonBox
        self.ok_button.accepted.connect(lambda: self.configure_credentials(self.signup_dialog.username_edit.text(), self.signup_dialog.name_edit.text(), self.signup_dialog.password_edit.text()))
        
    def configure_credentials(self, username, name, password):
        dir_path = os.path.dirname(os.path.realpath(__file__))

	    ### read config ##########################################################
     
        config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
        config = read_config(config_file_path)
        server_address = config['server']['address']
        server_port = config['server']['port']

	    ### test sign up ###########################################################

        url = f'http://{server_address}:{server_port}/signup'
        post_data = {
		    'username': username,
		    'name': name,
		    'password': password,
	    }

        r = requests.post(url=url, json=post_data)
        data = r.json()
        
        if data['signup_successful'] == True:
            self.success = True
            self.unique_username = True
            self.link.username = username