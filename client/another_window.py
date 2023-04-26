import json
import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.another_window_widget import Ui_AnotherWindow
from link import Link
from create_new_team import CreateNewTeamDialog

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

        self.main_window.view_players.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.main_window.view_players.verticalHeader().setVisible(False)
        self.main_window.view_players.insertRow(self.main_window.view_players.rowCount())

        self.main_window.available_players.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.main_window.available_players.verticalHeader().setVisible(False)
        self.main_window.available_players.insertRow(self.main_window.available_players.rowCount())
        self.main_window.available_players.setItem(0, 1, QTableWidgetItem("test"))
        self.main_window.available_players.cellDoubleClicked.connect(self.available_player_double_clicked)

        self.main_window.create_new_team.clicked.connect(self.create_new_team)
        self.main_window.create_new_team_3.clicked.connect(self.create_new_team)

        for row in range(self.main_window.available_players.rowCount()):

            btn = QPushButton(self.main_window.available_players)
            btn.clicked.connect(self.add_player)
            btn.setText('Add Player')
            self.main_window.available_players.setCellWidget(row, 0, btn)

            btn = QPushButton(self.main_window.view_players)
            btn.setText('Remove Player')
            self.main_window.view_players.setCellWidget(row, 0, btn)

            for column in range(self.main_window.available_players.columnCount()):
                item = self.main_window.available_players.item(row, column)
                if item != None:
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)

    def available_player_double_clicked(self, row, column):
        items = [self.main_window.available_players.item(row, column) for column in range(self.main_window.available_players.columnCount())]
        data = []
        for item in items:
            if item == None:
                data.append(None)
            else:
                data.append(item.text())
        print(f"Double-clicked on row {row}: {data}")
    
    def create_new_team(self):
        create_new_team_dialog = CreateNewTeamDialog(self.link)
        create_new_team_dialog.exec()
        
    def add_player(self, row):
        player_info = [self.main_window.available_players.item(row, column) for column in range(self.main_window.available_players.columnCount())]
        
        
        url = f'{self.link.server_address}:{self.link.server_port}/set_player'
        post_data = {
		    'player_name': player_info[2],
		    'player_position': player_info[1],
		    #'team_role': player_info[],  # player id
		    #'team_name': ,
		    'username': self.link.username,
	    }

        r = requests.post(url=url, json=post_data, verify=self.link.server_cert)
        data = r.json()
        print(json.dumps(data, indent=4))
    
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
            "field goal percentage": self.link.fg_percentage
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