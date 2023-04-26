import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.another_window_widget import Ui_AnotherWindow
from link import Link
from client.add_player_success import AddPlayerSuccessDialog

class AnotherWindow(QMainWindow):
    def __init__(self, link: Link, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.link = link

        self.main_window = Ui_AnotherWindow()
        self.main_window.setupUi(self)

        # Verifiers
        self.main_window.receptions_edit.setValidator(QDoubleValidator())
        self.main_window.tfl_edit.setValidator(QDoubleValidator())
        self.main_window.yards_edit.setValidator(QDoubleValidator())
        self.main_window.interceptions_edit.setValidator(QDoubleValidator())
        self.main_window.touchdowns_edit.setValidator(QDoubleValidator())
        self.main_window.fumbles_edit.setValidator(QDoubleValidator())
        self.main_window.turnovers_edit.setValidator(QDoubleValidator())
        self.main_window.punting_edit.setValidator(QDoubleValidator())
        self.main_window.sacks_edit.setValidator(QDoubleValidator())
        self.main_window.fg_percentage_edit.setValidator(QDoubleValidator())

        self.main_window.submit_button.clicked.connect(self.record_weights)

        self.shortcut_fullscreen = QShortcut(QKeySequence('F11'), self)
        self.shortcut_fullscreen.activated.connect(self.toggle_fullscreen)

        self.shortcut_exit_fullscreen = QShortcut(QKeySequence('Escape'), self)
        self.shortcut_exit_fullscreen.activated.connect(self.exit_fullscreen)

        self.shortcut_quit = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_quit.activated.connect(self.sigHandler)

    def open_add_player_success(self):
        add_player_success_dialog_box = AddPlayerSuccessDialog(self.link)

        add_player_success_dialog_box.exec()
        
        self.showTeamTab()
        
    def showTeamTab(self):
        self.close()
        ##self.open = TeamTab()
        ##self.open.show()
    
    def record_weights(self):
        self.link.receptions = float(self.main_window.receptions_edit.text())
        self.link.tfl = float(self.main_window.tfl_edit.text())
        self.link.yards = float(self.main_window.yards_edit.text())
        self.link.interceptions = float(self.main_window.interceptions_edit.text())
        self.link.touchdowns = float(self.main_window.touchdowns_edit.text())
        self.link.fumbles = float(self.main_window.fumbles_edit.text())
        self.link.turnovers = float(self.main_window.turnovers_edit.text())
        self.link.punting_yards = float(self.main_window.punting_edit.text())
        self.link.sacks = float(self.main_window.sacks_edit.text())
        self.link.fg_percentage = float(self.main_window.fg_percentage_edit.text())

        self.weights = {
            "receptions": self.link.receptions,
            "tackles for loss": self.link.tfl,
            "total yards": self.link.yards,
            "interceptions": self.link.interceptions,
            "touchdowns": self.link.touchdowns,
            "fumbles recovered": self.link.fumbles,
            "turnovers lost": self.link.turnovers,
            "punting yards": self.link.punting_yards,
            "sacks": self.link.sacks,
            "field_goal_percentage": self.link.fg_percentage
        }

        json_object = json.dumps(self.weights, indent=4)

        with open("client/resources/weights.json", "w") as outfile:
            outfile.write(json_object)

        self.main_window.receptions_edit.setText("")
        self.main_window.tfl_edit.setText("")
        self.main_window.yards_edit.setText("")
        self.main_window.interceptions_edit.setText("")
        self.main_window.touchdowns_edit.setText("")
        self.main_window.fumbles_edit.setText("")
        self.main_window.turnovers_edit.setText("")
        self.main_window.punting_edit.setText("")
        self.main_window.sacks_edit.setText("")
        self.main_window.fg_percentage_edit.setText("")

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def exit_fullscreen(self):
        self.showNormal()

    def sigHandler(*args):
        QApplication.quit()