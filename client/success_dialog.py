import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_python.success_dialog import Ui_SuccessDialog

class SuccessDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.success_dialog = Ui_SuccessDialog()
        self.success_dialog.setupUi(self)
        self.label = self.success_dialog.label
