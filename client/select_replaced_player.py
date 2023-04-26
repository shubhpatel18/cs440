import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.select_replaced_player_dialog import Ui_SelectReplacedPlayerDialog
from link import Link

class SelectReplacedPlayerDialog(QDialog):
    def __init__(self, link: Link):
        super().__init__()
        
        self.link = link
        
        self.cancelled = False
        self.valid = False
        self.success = False

        self.select_replaced_user_dialog = Ui_SelectReplacedPlayerDialog()
        self.select_replaced_user_dialog.setupUi(self)
        
        self.ok_button = self.signup_dialog.buttonBox
        #self.ok_button.accepted.connect(lambda: self.replace_player(self.link.username))
       
        self.cancel_button = self.signup_dialog.buttonBox
        self.cancel_button.rejected.connect(lambda: self.cancel())
        
    def replace_player(self, player_name, player_position, team_role, team_name, username):
        url = f'{self.link.server_address}:{self.link.server_port}/set_player'
        post_data = {
		    'player_name': player_name,
		    'player_position': player_position,
		    'team_role': team_role,  # inserted into te_id column of fantasy team
		    'team_name': team_name,
		    'username': username,
	    }

        r = requests.post(url=url, json=post_data, verify=self.link.server_cert)
        data = r.json()
        
        #self.success = data['success']
        #self.valid = data['valid_request']
    
    def cancel(self):
        self.cancelled = True
