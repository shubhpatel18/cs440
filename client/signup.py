from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.signup_dialog import Ui_SignupDialog
from link import Link

class SignupDialog(QDialog):
    def __init__(self, link: Link):
        super().__init__()

        self.link = link

        self.login_dialog = Ui_SignupDialog()
        self.login_dialog.setupUi(self)