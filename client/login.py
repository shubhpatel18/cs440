import os
import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.login_dialog import Ui_LoginDialog
from link import Link
from config_reader import read_config

class LoginDialog(QDialog):
    def __init__(self, link: Link):
        super().__init__()

        self.link = link

        self.verified = False

        self.login_dialog = Ui_LoginDialog()
        self.login_dialog.setupUi(self)

        self.ok_button = self.login_dialog.buttonBox
        self.ok_button.accepted.connect(lambda: self.verify_credentials(self.login_dialog.username_edit.text(), self.login_dialog.password_edit.text()))

    def verify_credentials(self, username, password):
        dir_path = os.path.dirname(os.path.realpath(__file__))

	    ### read config ##########################################################

        config_file_path = os.path.join(dir_path, 'resources', 'config.yaml')
        config = read_config(config_file_path)
        server_address = config['server']['address']
        server_port = config['server']['port']

        ### test login ###########################################################

        url = f'http://{server_address}:{server_port}/login'
        params = {
		    'username': username,
		    'password': password,
	    }

        r = requests.get(url=url, params=params)
        data = r.json()

        if data['login_successful'] == True:
            self.verified = True
            self.link.username = username
