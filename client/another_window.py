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

        self.main_window.available_players.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.main_window.available_players.verticalHeader().setVisible(False)

        self.main_window.create_new_team.clicked.connect(self.create_new_team)
        self.main_window.create_new_team_3.clicked.connect(self.create_new_team)

        self.main_window.available_players.setColumnHidden(1, True)
        self.main_window.view_players.setColumnHidden(1, True)

        self.init_fantasy_team()
        self.init_available_players()

    def init_available_players(self):
        url = f'{self.link.server_address}:{self.link.server_port}/available_players'
        params = {
            'team_name': self.main_window.available_players_team_name_dropdown.currentText(),
            'username': self.link.username,
            'year': 2022,
            'week': self.main_window.available_players_week_dropdown.currentText().split(' ')[1],
        }

        r = requests.get(url=url, params=params, verify=self.link.server_cert)
        data = r.json()
        r.close()

        for row in range(len(data['available_players'])):

            if self.main_window.available_players.item(row, 1) == None:
                self.main_window.available_players.insertRow(row)
            btn = QPushButton(self.main_window.available_players)
            btn.setProperty("row", row)
            btn.clicked.connect(self.add_player)
            btn.setText('Add Player')
            self.main_window.available_players.setCellWidget(row, 0, btn)

            for column in range(len(data['available_players'][0])):
                self.main_window.available_players.setItem(row, column+1, QTableWidgetItem())
                item = self.main_window.available_players.item(row, column+1)
                item.setText(str(data['available_players'][row][column]))
                if item != None:
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)

    def init_fantasy_team(self):
        url = f'{self.link.server_address}:{self.link.server_port}/fantasy_teams'
        params = {
            'username': self.link.username,
            'year': 2022,
            'week': self.main_window.view_players_week_dropdown.currentText().split(' ')[1],
        }

        r = requests.get(url=url, params=params, verify=self.link.server_cert)
        data = r.json()
        r.close()

        for fantasy_team in data['fantasy_teams']:
            self.main_window.available_players_team_name_dropdown.addItem(fantasy_team)
            self.main_window.view_players_team_name_dropdown.addItem(fantasy_team)

        row = 0
        for key in data['fantasy_teams'][self.main_window.view_players_team_name_dropdown.currentText()].keys():
            
            self.main_window.view_players.insertRow(row)
            btn = QPushButton(self.main_window.view_players)
            btn.setText('Remove Player')
            self.main_window.view_players.setCellWidget(row, 0, btn)
            self.main_window.view_players.cellClicked.connect(self.remove_player)


            data_array:list = data['fantasy_teams'][self.main_window.view_players_team_name_dropdown.currentText()][key]
            if len(data_array) > 0:

                for stat in range(len(data_array)):
                    self.main_window.view_players.setItem(row, stat+2, QTableWidgetItem())
                    item = self.main_window.view_players.item(row, stat+2)
                    if item != None:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setText(str(data_array[stat]))
                    
            row = row + 1

    def update_fantasy_team(self):
        url = f'{self.link.server_address}:{self.link.server_port}/fantasy_teams'
        params = {
            'username': self.link.username,
            'year': 2022,
            'week': self.main_window.view_players_week_dropdown.currentText().split(' ')[1],
        }

        r = requests.get(url=url, params=params, verify=self.link.server_cert)
        data = r.json()
        r.close()

        for fantasy_team in data['fantasy_teams']:
            self.main_window.available_players_team_name_dropdown.addItem(fantasy_team)
            self.main_window.view_players_team_name_dropdown.addItem(fantasy_team)

        row = 0
        for key in data['fantasy_teams'][self.main_window.view_players_team_name_dropdown.currentText()].keys():
            
            btn = QPushButton(self.main_window.view_players)
            btn.setText('Remove Player')
            self.main_window.view_players.setCellWidget(row, 0, btn)
            self.main_window.view_players.cellClicked.connect(self.remove_player)


            data_array:list = data['fantasy_teams'][self.main_window.view_players_team_name_dropdown.currentText()][key]
            if len(data_array) > 0:

                for stat in range(len(data_array)):
                    self.main_window.view_players.setItem(row, stat+2, QTableWidgetItem())
                    item = self.main_window.view_players.item(row, stat+2)
                    if item != None:
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setText(str(data_array[stat]))
                    
            row = row + 1

    def create_new_team(self):
        create_new_team_dialog = CreateNewTeamDialog(self.link)
        create_new_team_dialog.exec()
        
    def add_player(self):
        btn = self.sender()
        row = btn.property("row")
        success = False
        
        player_info = []
        for column in range(1, self.main_window.available_players.columnCount() - 1):
            player_info.append(self.main_window.available_players.item(row, column).text())
        
        player_name = player_info[1]
        player_position = player_info[2]
        team_role = self.main_window.position_to_fill.currentText()
        team_name = self.main_window.view_players_team_name_dropdown.currentText()
        
        url = f'{self.link.server_address}:{self.link.server_port}/set_player'
        data = {
		    'player_name': player_name,
		    'player_position': player_position,
		    'team_role': team_role,  # player id
		    'team_name': team_name,
		    'username': self.link.username,
	    }

        r = requests.post(url=url, json=data, verify=self.link.server_cert)
        data = r.json()
        print(data)
        self.update_fantasy_team()
        success = data['add_player_successful']
        
        if success == True:
            self.main_window.view_players_label.setText(player_name + " successfully added to team " + team_name + ".")
            self.main_window.view_players_label.setStyleSheet("color: rgb(0, 128, 0)")
            self.main_window.tabWidget.setCurrentIndex(0)
        else:
            self.main_window.view_players_label.setText(player_name + " could not be added to team. " + player_position + " already filled. Remove player already in position and try again")
            self.main_window.view_players_label.setStyleSheet("color: rgb(239, 41, 41)")
            self.main_window.tabWidget.setCurrentIndex(self, 0)
    
    def remove_player(self):
        print('remove_player')
        
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