import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.add_player_success_dialog import Ui_AddPlayerSuccessDialog

class AddPlayerSuccessDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.add_player_success_dialog = Ui_AddPlayerSuccessDialog()
        self.add_player_success_dialog.setupUi(self)
