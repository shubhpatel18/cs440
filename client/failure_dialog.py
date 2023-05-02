from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_python.failure_dialog import Ui_FailureDialog

class FailureDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.failure_dialog = Ui_FailureDialog()
        self.failure_dialog.setupUi(self)
        self.label = self.failure_dialog.label
