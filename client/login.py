from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.login_dialog import Ui_LoginDialog

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.login_dialog = Ui_LoginDialog()
        self.login_dialog.setupUi(self)