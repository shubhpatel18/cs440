#!/usr/bin/env python3.8

import json
import sys
import signal
import os
from pathlib import Path

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.main_window_widget import Ui_MainWindow
from another_window import AnotherWindow
from login import LoginDialog
from signup import SignupDialog
from link import Link

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.link = Link()

        icon_path = os.path.dirname("images/logo.png")
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowTitle("Roster Rookies")

        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        self.login_button = self.main_window.login_button
        self.login_button.clicked.connect(self.open_login)
        
        self.signup_button = self.main_window.sign_up_button
        self.signup_button.clicked.connect(self.open_signup)

        self.shortcut_fullscreen = QShortcut(QKeySequence('F11'), self)
        self.shortcut_fullscreen.activated.connect(self.toggle_fullscreen)

        self.shortcut_exit_fullscreen = QShortcut(QKeySequence('Escape'), self)
        self.shortcut_exit_fullscreen.activated.connect(self.exit_fullscreen)

        self.shortcut_quit = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_quit.activated.connect(self.sigHandler)

        self.error_label = self.main_window.error_label

    def open_login(self):
        login_dialog_box = LoginDialog(self.link)

        login_dialog_box.exec()

        if login_dialog_box.verified == False:
            self.error_label.setText("Login failed. Please try again.")
            self.error_label.setStyleSheet("color: rgb(239, 41, 41)")
            return
        
        self.showAnotherWindow()
        
    def open_signup(self):
        signup_dialog_box = SignupDialog(self.link)
        
        signup_dialog_box.exec()
        
        if signup_dialog_box.success == True:
            self.showAnotherWindow()
        elif signup_dialog_box.cancel == True:
            return
        elif signup_dialog_box.username_taken == True:
            self.error_label.setText("Username already taken. Please try a different username.")
            self.error_label.setStyleSheet("color: rgb(239, 41, 41)")
            return
        elif signup_dialog_box.valid == False:
            self.error_label.setText("Invalid sign up request. Please try again.")
            self.error_label.setStyleSheet("color: rgb(239, 41, 41)")
            return
        elif signup_dialog_box.success == False:
            self.error_label.setText("Sign up failed. Please try again.")
            self.error_label.setStyleSheet("color: rgb(239, 41, 41)")
            return

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def exit_fullscreen(self):
        self.showNormal()

    def sigHandler(*args):
        QApplication.quit()

    def showAnotherWindow(self):
        self.close()
        self.open = AnotherWindow(self.link)
        self.open.setWindowTitle("Roster Rookies")
        self.open.show()

# class AnotherWindow(QMainWindow):
#     def __init__(self, link: Link, *args, **kwargs) -> None:
#         super().__init__(*args, **kwargs)

#         self.link = Link()

#         icon_path = os.path.dirname("images/logo.png")
#         self.setWindowIcon(QIcon(str(icon_path)))

        # self.main_window = Ui_AnotherWindow()
        # self.main_window.setupUi(self)

        # self.main_window.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # self.main_window.tableWidget.verticalHeader().setVisible(False)
        # self.main_window.tableWidget.insertRow(self.main_window.tableWidget.rowCount())
        # self.main_window.tableWidget.setItem(0, 1, QTableWidgetItem("test"))
        # self.main_window.tableWidget.doubleClicked.connect()
        # url = f'{self.link.server_address}:{self.link.server_port}/available_players'
        # params = {
        #     'team_name': 'test',
        #     'username': link.username,
        #     'year': '',
        #     'week': ''
        # }

        # r = requests.get(url=url, params=params, verify=self.link.server_cert)
        # data = r.json()
        # for()
        # self.main_window.tableWidget.setItem()

class AppRunner():
    def __init__(self, WindowType: QMainWindow):
        self.WindowType = WindowType

    def start(self):
        app = QApplication(sys.argv)

        window = self.WindowType()
        window.show()

        signal.signal(signal.SIGINT, window.sigHandler)

        timer = QTimer()
        timer.start(500)
        timer.timeout.connect(lambda: None)

        sys.exit(app.exec_())

if __name__ == '__main__':
    app = AppRunner(MainWindow)
    app.start()