import json
import requests

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_python.another_window_widget import Ui_AnotherWindow
from link import Link
from change_password import ChangePasswordDialog
from create_new_team import CreateNewTeamDialog
from add_player import AddPlayerDialog
from success_dialog import SuccessDialog

class AnotherWindow(QMainWindow):
    def __init__(self, link: Link, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.link = link

        self.main_window = Ui_AnotherWindow()
        self.main_window.setupUi(self)

        # valid settings inputs
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

        self.changepass_button = self.main_window.pushButton
        self.changepass_button.clicked.connect(self.open_change_password)

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

        self.init_fantasy_teams()
        self.init_available_players()
        self.main_window.available_players_team_name_dropdown.setCurrentIndex(0)
        self.main_window.view_players_team_name_dropdown.setCurrentIndex(0)

        self.main_window.available_players_team_name_dropdown.currentIndexChanged.connect(self.fantasy_team_changed)
        self.main_window.view_players_team_name_dropdown.currentIndexChanged.connect(self.fantasy_team_changed)
        self.main_window.available_players_week_dropdown.currentIndexChanged.connect(self.update_available_players)
        self.main_window.team_role_combobox.currentTextChanged.connect(self.update_available_players)

    def change_fantasy_team(self, index: int):
        self.main_window.available_players_team_name_dropdown.setCurrentIndex(index)
        self.main_window.view_players_team_name_dropdown.setCurrentIndex(index)

    def fantasy_team_changed(self, index: int):
        self.update_fantasy_teams()
        self.update_available_players()
        self.main_window.view_players_label.setText('')

    def init_available_players(self):
        if self.main_window.available_players_team_name_dropdown.currentText():
            self.update_available_players()

    def update_available_players(self):
        url = f'{self.link.server_address}:{self.link.server_port}/available_players'
        params = {
            'team_name': self.main_window.available_players_team_name_dropdown.currentText(),
            'username': self.link.username,
            'team_role': self.main_window.team_role_combobox.currentText(),
            'year': 2022,
            'week': self.main_window.available_players_week_dropdown.currentText().split(' ')[1],
            'receptions_multiplier': self.link.receptions,
            'total_yards_multiplier': self.link.yards,
            'touchdowns_multiplier': self.link.touchdowns,
            'turnovers_lost_mulitplier': self.link.turnovers,
            'sacks_multiplier': self.link.sacks,
            'tackles_for_loss_multiplier': self.link.tfl,
            'interceptions_multiplier': self.link.interceptions,
            'fumbles_recovered_multiplier': self.link.fumbles,
            'punting_yards_multiplier': self.link.punting_yards,
            'fg_percentage_multiplier': self.link.fg_percentage,
        }

        r = requests.get(url=url, params=params, verify=self.link.server_cert)
        data = r.json()
        r.close()

        available_player_data = data['available_players']
        self.main_window.available_players.clearSelection()
        self.main_window.available_players.clearContents()
        self.main_window.available_players.setRowCount(len(available_player_data))
        for row, player_data in enumerate(available_player_data):

            # add add player button
            btn = QPushButton(self.main_window.available_players)
            btn.setProperty('row', row)
            btn.setText('Add Player')
            btn.clicked.connect(self.add_player)
            self.main_window.available_players.setCellWidget(row, 0, btn)

            for column, stat in enumerate(player_data):
                # skip player id
                if column == 0:
                    continue

                item = QTableWidgetItem()
                item.setText(str(stat))
                item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                self.main_window.available_players.setItem(row, column, item)

        self.main_window.available_players.resizeColumnToContents(0)

    def init_fantasy_teams(self):
        self.update_fantasy_teams()

    def update_fantasy_teams(self):
        url = f'{self.link.server_address}:{self.link.server_port}/fantasy_teams'
        params = {
            'username': self.link.username,
            'year': 2022,
            'week': self.main_window.view_players_week_dropdown.currentText().split(' ')[1],
            'receptions_multiplier': self.link.receptions,
            'total_yards_multiplier': self.link.yards,
            'touchdowns_multiplier': self.link.touchdowns,
            'turnovers_lost_mulitplier': self.link.turnovers,
            'sacks_multiplier': self.link.sacks,
            'tackles_for_loss_multiplier': self.link.tfl,
            'interceptions_multiplier': self.link.interceptions,
            'fumbles_recovered_multiplier': self.link.fumbles,
            'punting_yards_multiplier': self.link.punting_yards,
            'fg_percentage_multiplier': self.link.fg_percentage,
        }

        r = requests.get(url=url, params=params, verify=self.link.server_cert)
        data = r.json()
        r.close()

        if data['team_exists'] == True:

            # update team name dropdowns
            self.main_window.available_players_team_name_dropdown.blockSignals(True)
            self.main_window.view_players_team_name_dropdown.blockSignals(True)
            self.main_window.available_players_team_name_dropdown.clear()
            self.main_window.view_players_team_name_dropdown.clear()
            for fantasy_team_name in data['fantasy_teams']:
                self.main_window.available_players_team_name_dropdown.addItem(fantasy_team_name)
                self.main_window.view_players_team_name_dropdown.addItem(fantasy_team_name)
            self.main_window.available_players_team_name_dropdown.blockSignals(False)
            self.main_window.view_players_team_name_dropdown.blockSignals(False)

            # populate table with fantasy team data
            team_name = self.main_window.view_players_team_name_dropdown.currentText()
            fantasy_team_data = data['fantasy_teams'][team_name]
            self.main_window.view_players.clearSelection()
            self.main_window.view_players.clearContents()
            self.main_window.view_players.setRowCount(len(fantasy_team_data))
            for row, item in enumerate(fantasy_team_data.items()):
                role, player_data = item

                # add remove player button
                btn = QPushButton(self.main_window.view_players)
                btn.setProperty('row', row)
                btn.setText('Remove Player')
                btn.clicked.connect(self.remove_player)
                self.main_window.view_players.setCellWidget(row, 0, btn)

                player_data = data['fantasy_teams'][team_name][role]
                if len(player_data) > 0:

                    for column, stat in enumerate(player_data):
                        # skip player id, but insert team role
                        text = str(role).upper() if column == 0 else str(stat)
                        item = QTableWidgetItem()
                        item.setFlags(item.flags() ^ Qt.ItemIsEditable)
                        item.setText(text)
                        self.main_window.view_players.setItem(row, column+1, item)  # skip button column

            self.main_window.view_players.resizeColumnToContents(0)

    def create_new_team(self):
        create_new_team_dialog = CreateNewTeamDialog(self.link)
        create_new_team_dialog.exec()
        if create_new_team_dialog.accepted:
            self.update_fantasy_teams()
            self.update_available_players()

    def add_player(self):
        btn = self.sender()
        row = btn.property("row")

        player_info = []
        for column in range(1, self.main_window.available_players.columnCount()):  # skip buttons
            player_info.append(self.main_window.available_players.item(row, column).text())

        player_name = player_info[0]
        player_position = player_info[1]
        team_name = self.main_window.view_players_team_name_dropdown.currentText()

        add_player_dialog = AddPlayerDialog(self.link, player_name, player_position, team_name)
        add_player_dialog.exec()

        if add_player_dialog.successful == True:
            self.update_fantasy_teams()
            
            success_dialog = SuccessDialog()
            success_dialog.label.setText(player_name + " successfully added to team " + team_name + ".")
            success_dialog.exec()
            self.update_available_players()

            self.main_window.tabWidget.setCurrentIndex(0)

    def remove_player(self):
        btn = self.sender()
        row = btn.property("row")

        player_info = []
        for column in range(1, self.main_window.view_players.columnCount()):  # skip buttons
            player_info.append(self.main_window.view_players.item(row, column).text())

        team_role = player_info[0].lower()
        player_name = player_info[1]
        team_name = self.main_window.view_players_team_name_dropdown.currentText()

        url = f'{self.link.server_address}:{self.link.server_port}/clear_role'
        post_data = {
            'team_role': team_role,
            'team_name': team_name,
            'username': self.link.username
        }

        r = requests.post(url=url, json=post_data, verify=self.link.server_cert)
        data = r.json()
        r.close()

        if data['clear_role_successful'] == True:
            self.update_fantasy_teams()
            self.update_available_players()

            self.main_window.view_players_label.setText(player_name + " successfully removed from team " + team_name + ".")
            self.main_window.view_players_label.setStyleSheet("color: rgb(0, 128, 0)")

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

        self.update_available_players()

    def open_change_password(self):
        change_password_dialog_box = ChangePasswordDialog(self.link)

        change_password_dialog_box.exec()

        if change_password_dialog_box.success == False:
            self.error_label.setText("Change Password failed. Please try again.")
            self.error_label.setStyleSheet("color: rgb(239, 41, 41)")
            return
        elif change_password_dialog_box.valid == False:
            self.error_label.setText("Invalid password change request. Please try again.")
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

    # for use with signout button
    def showMainWindow(self):
        self.link.username = ""
        self.close()
