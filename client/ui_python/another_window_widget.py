# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_xml/another_window_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnotherWindow(object):
    def setupUi(self, AnotherWindow):
        AnotherWindow.setObjectName("AnotherWindow")
        AnotherWindow.resize(1206, 738)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui_xml/../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("ui_xml/../images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        AnotherWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AnotherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.view_team_tab = QtWidgets.QWidget()
        self.view_team_tab.setObjectName("view_team_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.view_team_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.view_players_team_name_dropdown = QtWidgets.QComboBox(self.view_team_tab)
        self.view_players_team_name_dropdown.setObjectName("view_players_team_name_dropdown")
        self.gridLayout_3.addWidget(self.view_players_team_name_dropdown, 0, 0, 1, 1)
        self.create_new_team_3 = QtWidgets.QPushButton(self.view_team_tab)
        self.create_new_team_3.setObjectName("create_new_team_3")
        self.gridLayout_3.addWidget(self.create_new_team_3, 0, 1, 1, 1)
        self.view_players_week_dropdown = QtWidgets.QComboBox(self.view_team_tab)
        self.view_players_week_dropdown.setObjectName("view_players_week_dropdown")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.view_players_week_dropdown.addItem("")
        self.gridLayout_3.addWidget(self.view_players_week_dropdown, 0, 2, 1, 1)
        self.view_players_label = QtWidgets.QLabel(self.view_team_tab)
        self.view_players_label.setStyleSheet("font: 30pt \"Ubuntu\";")
        self.view_players_label.setText("")
        self.view_players_label.setObjectName("view_players_label")
        self.gridLayout_3.addWidget(self.view_players_label, 1, 0, 1, 3)
        self.view_players = QtWidgets.QTableWidget(self.view_team_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_players.sizePolicy().hasHeightForWidth())
        self.view_players.setSizePolicy(sizePolicy)
        self.view_players.setMinimumSize(QtCore.QSize(1029, 0))
        self.view_players.setObjectName("view_players")
        self.view_players.setColumnCount(17)
        self.view_players.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.view_players.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.view_players.setHorizontalHeaderItem(16, item)
        self.view_players.horizontalHeader().setCascadingSectionResizes(True)
        self.view_players.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.view_players, 2, 0, 1, 3)
        self.tabWidget.addTab(self.view_team_tab, "")
        self.player_stats_tab = QtWidgets.QWidget()
        self.player_stats_tab.setObjectName("player_stats_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.player_stats_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.available_players_team_name_dropdown = QtWidgets.QComboBox(self.player_stats_tab)
        self.available_players_team_name_dropdown.setObjectName("available_players_team_name_dropdown")
        self.gridLayout_2.addWidget(self.available_players_team_name_dropdown, 0, 0, 1, 1)
        self.create_new_team = QtWidgets.QPushButton(self.player_stats_tab)
        self.create_new_team.setObjectName("create_new_team")
        self.gridLayout_2.addWidget(self.create_new_team, 0, 1, 1, 1)
        self.available_players_week_dropdown = QtWidgets.QComboBox(self.player_stats_tab)
        self.available_players_week_dropdown.setObjectName("available_players_week_dropdown")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.available_players_week_dropdown.addItem("")
        self.gridLayout_2.addWidget(self.available_players_week_dropdown, 0, 2, 1, 1)
        self.team_role_combobox = QtWidgets.QComboBox(self.player_stats_tab)
        self.team_role_combobox.setObjectName("team_role_combobox")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.team_role_combobox.addItem("")
        self.gridLayout_2.addWidget(self.team_role_combobox, 0, 3, 1, 1)
        self.available_players = QtWidgets.QTableWidget(self.player_stats_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.available_players.sizePolicy().hasHeightForWidth())
        self.available_players.setSizePolicy(sizePolicy)
        self.available_players.setMinimumSize(QtCore.QSize(1029, 0))
        self.available_players.setObjectName("available_players")
        self.available_players.setColumnCount(16)
        self.available_players.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.available_players.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.available_players.setHorizontalHeaderItem(16, item)
        self.available_players.horizontalHeader().setCascadingSectionResizes(True)
        self.available_players.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.available_players, 1, 0, 1, 4)
        self.tabWidget.addTab(self.player_stats_tab, "")
        self.profile_tab = QtWidgets.QWidget()
        self.profile_tab.setObjectName("profile_tab")
        self.pushButton = QtWidgets.QPushButton(self.profile_tab)
        self.pushButton.setGeometry(QtCore.QRect(588, 10, 141, 25))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.profile_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.settings_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tfl_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tfl_edit.sizePolicy().hasHeightForWidth())
        self.tfl_edit.setSizePolicy(sizePolicy)
        self.tfl_edit.setClearButtonEnabled(False)
        self.tfl_edit.setObjectName("tfl_edit")
        self.gridLayout.addWidget(self.tfl_edit, 3, 3, 1, 1)
        self.receptions_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receptions_edit.sizePolicy().hasHeightForWidth())
        self.receptions_edit.setSizePolicy(sizePolicy)
        self.receptions_edit.setObjectName("receptions_edit")
        self.gridLayout.addWidget(self.receptions_edit, 3, 1, 1, 1)
        self.fg_percentage_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fg_percentage_edit.sizePolicy().hasHeightForWidth())
        self.fg_percentage_edit.setSizePolicy(sizePolicy)
        self.fg_percentage_edit.setObjectName("fg_percentage_edit")
        self.gridLayout.addWidget(self.fg_percentage_edit, 7, 3, 1, 1)
        self.punting_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.punting_edit.sizePolicy().hasHeightForWidth())
        self.punting_edit.setSizePolicy(sizePolicy)
        self.punting_edit.setObjectName("punting_edit")
        self.gridLayout.addWidget(self.punting_edit, 6, 3, 1, 1)
        self.yards_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yards_edit.sizePolicy().hasHeightForWidth())
        self.yards_edit.setSizePolicy(sizePolicy)
        self.yards_edit.setObjectName("yards_edit")
        self.gridLayout.addWidget(self.yards_edit, 4, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.settings_tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 4)
        self.turnovers_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turnovers_edit.sizePolicy().hasHeightForWidth())
        self.turnovers_edit.setSizePolicy(sizePolicy)
        self.turnovers_edit.setObjectName("turnovers_edit")
        self.gridLayout.addWidget(self.turnovers_edit, 6, 1, 1, 1)
        self.touchdowns_label = QtWidgets.QLabel(self.settings_tab)
        self.touchdowns_label.setObjectName("touchdowns_label")
        self.gridLayout.addWidget(self.touchdowns_label, 5, 0, 1, 1)
        self.interceptions_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interceptions_edit.sizePolicy().hasHeightForWidth())
        self.interceptions_edit.setSizePolicy(sizePolicy)
        self.interceptions_edit.setObjectName("interceptions_edit")
        self.gridLayout.addWidget(self.interceptions_edit, 4, 3, 1, 1)
        self.title_label = QtWidgets.QLabel(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setStyleSheet("font: 26pt \"Ubuntu\";")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 4)
        self.fg_percentage_label = QtWidgets.QLabel(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fg_percentage_label.sizePolicy().hasHeightForWidth())
        self.fg_percentage_label.setSizePolicy(sizePolicy)
        self.fg_percentage_label.setObjectName("fg_percentage_label")
        self.gridLayout.addWidget(self.fg_percentage_label, 7, 2, 1, 1)
        self.fumbles_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fumbles_edit.sizePolicy().hasHeightForWidth())
        self.fumbles_edit.setSizePolicy(sizePolicy)
        self.fumbles_edit.setObjectName("fumbles_edit")
        self.gridLayout.addWidget(self.fumbles_edit, 5, 3, 1, 1)
        self.submit_button = QtWidgets.QPushButton(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)
        self.submit_button.setObjectName("submit_button")
        self.gridLayout.addWidget(self.submit_button, 9, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.receptions_label = QtWidgets.QLabel(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receptions_label.sizePolicy().hasHeightForWidth())
        self.receptions_label.setSizePolicy(sizePolicy)
        self.receptions_label.setObjectName("receptions_label")
        self.gridLayout.addWidget(self.receptions_label, 3, 0, 1, 1)
        self.sacks_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sacks_edit.sizePolicy().hasHeightForWidth())
        self.sacks_edit.setSizePolicy(sizePolicy)
        self.sacks_edit.setObjectName("sacks_edit")
        self.gridLayout.addWidget(self.sacks_edit, 7, 1, 1, 1)
        self.punting_label = QtWidgets.QLabel(self.settings_tab)
        self.punting_label.setObjectName("punting_label")
        self.gridLayout.addWidget(self.punting_label, 6, 2, 1, 1)
        self.yards_label = QtWidgets.QLabel(self.settings_tab)
        self.yards_label.setObjectName("yards_label")
        self.gridLayout.addWidget(self.yards_label, 4, 0, 1, 1)
        self.touchdowns_edit = QtWidgets.QLineEdit(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.touchdowns_edit.sizePolicy().hasHeightForWidth())
        self.touchdowns_edit.setSizePolicy(sizePolicy)
        self.touchdowns_edit.setObjectName("touchdowns_edit")
        self.gridLayout.addWidget(self.touchdowns_edit, 5, 1, 1, 1)
        self.sacks_label = QtWidgets.QLabel(self.settings_tab)
        self.sacks_label.setObjectName("sacks_label")
        self.gridLayout.addWidget(self.sacks_label, 7, 0, 1, 1)
        self.fumbles_label = QtWidgets.QLabel(self.settings_tab)
        self.fumbles_label.setObjectName("fumbles_label")
        self.gridLayout.addWidget(self.fumbles_label, 5, 2, 1, 1)
        self.interceptions_label = QtWidgets.QLabel(self.settings_tab)
        self.interceptions_label.setObjectName("interceptions_label")
        self.gridLayout.addWidget(self.interceptions_label, 4, 2, 1, 1)
        self.turnovers_label = QtWidgets.QLabel(self.settings_tab)
        self.turnovers_label.setObjectName("turnovers_label")
        self.gridLayout.addWidget(self.turnovers_label, 6, 0, 1, 1)
        self.tfl_label = QtWidgets.QLabel(self.settings_tab)
        self.tfl_label.setObjectName("tfl_label")
        self.gridLayout.addWidget(self.tfl_label, 3, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.settings_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.settings_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        AnotherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AnotherWindow)
        self.tabWidget.setCurrentIndex(0)
        self.view_players_week_dropdown.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AnotherWindow)
        AnotherWindow.setTabOrder(self.receptions_edit, self.yards_edit)
        AnotherWindow.setTabOrder(self.yards_edit, self.touchdowns_edit)
        AnotherWindow.setTabOrder(self.touchdowns_edit, self.turnovers_edit)
        AnotherWindow.setTabOrder(self.turnovers_edit, self.sacks_edit)
        AnotherWindow.setTabOrder(self.sacks_edit, self.tfl_edit)
        AnotherWindow.setTabOrder(self.tfl_edit, self.interceptions_edit)
        AnotherWindow.setTabOrder(self.interceptions_edit, self.fumbles_edit)
        AnotherWindow.setTabOrder(self.fumbles_edit, self.punting_edit)
        AnotherWindow.setTabOrder(self.punting_edit, self.fg_percentage_edit)
        AnotherWindow.setTabOrder(self.fg_percentage_edit, self.submit_button)
        AnotherWindow.setTabOrder(self.submit_button, self.view_players_team_name_dropdown)
        AnotherWindow.setTabOrder(self.view_players_team_name_dropdown, self.create_new_team)
        AnotherWindow.setTabOrder(self.create_new_team, self.tabWidget)
        AnotherWindow.setTabOrder(self.tabWidget, self.view_players_week_dropdown)
        AnotherWindow.setTabOrder(self.view_players_week_dropdown, self.available_players)
        AnotherWindow.setTabOrder(self.available_players, self.available_players_team_name_dropdown)
        AnotherWindow.setTabOrder(self.available_players_team_name_dropdown, self.available_players_week_dropdown)
        AnotherWindow.setTabOrder(self.available_players_week_dropdown, self.pushButton)
        AnotherWindow.setTabOrder(self.pushButton, self.create_new_team_3)
        AnotherWindow.setTabOrder(self.create_new_team_3, self.team_role_combobox)
        AnotherWindow.setTabOrder(self.team_role_combobox, self.view_players)

    def retranslateUi(self, AnotherWindow):
        _translate = QtCore.QCoreApplication.translate
        AnotherWindow.setWindowTitle(_translate("AnotherWindow", "Roster Rookies"))
        self.create_new_team_3.setText(_translate("AnotherWindow", "Create New Team"))
        self.view_players_week_dropdown.setItemText(0, _translate("AnotherWindow", "Week 1"))
        self.view_players_week_dropdown.setItemText(1, _translate("AnotherWindow", "Week 2"))
        self.view_players_week_dropdown.setItemText(2, _translate("AnotherWindow", "Week 3"))
        self.view_players_week_dropdown.setItemText(3, _translate("AnotherWindow", "Week 4"))
        self.view_players_week_dropdown.setItemText(4, _translate("AnotherWindow", "Week 5"))
        self.view_players_week_dropdown.setItemText(5, _translate("AnotherWindow", "Week 6"))
        self.view_players_week_dropdown.setItemText(6, _translate("AnotherWindow", "Week 7"))
        self.view_players_week_dropdown.setItemText(7, _translate("AnotherWindow", "Week 8"))
        self.view_players_week_dropdown.setItemText(8, _translate("AnotherWindow", "Week 9"))
        self.view_players_week_dropdown.setItemText(9, _translate("AnotherWindow", "Week 10"))
        self.view_players_week_dropdown.setItemText(10, _translate("AnotherWindow", "Week 11"))
        self.view_players_week_dropdown.setItemText(11, _translate("AnotherWindow", "Week 12"))
        self.view_players_week_dropdown.setItemText(12, _translate("AnotherWindow", "Week 13"))
        self.view_players_week_dropdown.setItemText(13, _translate("AnotherWindow", "Week 14"))
        self.view_players.setSortingEnabled(True)
        item = self.view_players.horizontalHeaderItem(1)
        item.setText(_translate("AnotherWindow", "Team Role"))
        item = self.view_players.horizontalHeaderItem(2)
        item.setText(_translate("AnotherWindow", "Player Name"))
        item = self.view_players.horizontalHeaderItem(3)
        item.setText(_translate("AnotherWindow", "Position"))
        item = self.view_players.horizontalHeaderItem(4)
        item.setText(_translate("AnotherWindow", "Receptions"))
        item = self.view_players.horizontalHeaderItem(5)
        item.setText(_translate("AnotherWindow", "Total Yards"))
        item = self.view_players.horizontalHeaderItem(6)
        item.setText(_translate("AnotherWindow", "Touchdowns"))
        item = self.view_players.horizontalHeaderItem(7)
        item.setText(_translate("AnotherWindow", "Turnovers Lost"))
        item = self.view_players.horizontalHeaderItem(8)
        item.setText(_translate("AnotherWindow", "Sacks"))
        item = self.view_players.horizontalHeaderItem(9)
        item.setText(_translate("AnotherWindow", "Tackles for Loss"))
        item = self.view_players.horizontalHeaderItem(10)
        item.setText(_translate("AnotherWindow", "Interceptions"))
        item = self.view_players.horizontalHeaderItem(11)
        item.setText(_translate("AnotherWindow", "Fumbles Recovered"))
        item = self.view_players.horizontalHeaderItem(12)
        item.setText(_translate("AnotherWindow", "Punting Yards"))
        item = self.view_players.horizontalHeaderItem(13)
        item.setText(_translate("AnotherWindow", "FG Percentage"))
        item = self.view_players.horizontalHeaderItem(14)
        item.setText(_translate("AnotherWindow", "Injury Status"))
        item = self.view_players.horizontalHeaderItem(15)
        item.setText(_translate("AnotherWindow", "College"))
        item = self.view_players.horizontalHeaderItem(16)
        item.setText(_translate("AnotherWindow", "Score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view_team_tab), _translate("AnotherWindow", "View Team"))
        self.create_new_team.setText(_translate("AnotherWindow", "Create New Team"))
        self.available_players_week_dropdown.setItemText(0, _translate("AnotherWindow", "Week 1"))
        self.available_players_week_dropdown.setItemText(1, _translate("AnotherWindow", "Week 2"))
        self.available_players_week_dropdown.setItemText(2, _translate("AnotherWindow", "Week 3"))
        self.available_players_week_dropdown.setItemText(3, _translate("AnotherWindow", "Week 4"))
        self.available_players_week_dropdown.setItemText(4, _translate("AnotherWindow", "Week 5"))
        self.available_players_week_dropdown.setItemText(5, _translate("AnotherWindow", "Week 6"))
        self.available_players_week_dropdown.setItemText(6, _translate("AnotherWindow", "Week 7"))
        self.available_players_week_dropdown.setItemText(7, _translate("AnotherWindow", "Week 8"))
        self.available_players_week_dropdown.setItemText(8, _translate("AnotherWindow", "Week 9"))
        self.available_players_week_dropdown.setItemText(9, _translate("AnotherWindow", "Week 10"))
        self.available_players_week_dropdown.setItemText(10, _translate("AnotherWindow", "Week 11"))
        self.available_players_week_dropdown.setItemText(11, _translate("AnotherWindow", "Week 12"))
        self.available_players_week_dropdown.setItemText(12, _translate("AnotherWindow", "Week 13"))
        self.available_players_week_dropdown.setItemText(13, _translate("AnotherWindow", "Week 14"))
        self.team_role_combobox.setItemText(0, _translate("AnotherWindow", "all"))
        self.team_role_combobox.setItemText(1, _translate("AnotherWindow", "qb"))
        self.team_role_combobox.setItemText(2, _translate("AnotherWindow", "rb"))
        self.team_role_combobox.setItemText(3, _translate("AnotherWindow", "wr1"))
        self.team_role_combobox.setItemText(4, _translate("AnotherWindow", "wr2"))
        self.team_role_combobox.setItemText(5, _translate("AnotherWindow", "te"))
        self.team_role_combobox.setItemText(6, _translate("AnotherWindow", "flex"))
        self.team_role_combobox.setItemText(7, _translate("AnotherWindow", "center"))
        self.team_role_combobox.setItemText(8, _translate("AnotherWindow", "lg"))
        self.team_role_combobox.setItemText(9, _translate("AnotherWindow", "rg"))
        self.team_role_combobox.setItemText(10, _translate("AnotherWindow", "punter"))
        self.team_role_combobox.setItemText(11, _translate("AnotherWindow", "de1"))
        self.team_role_combobox.setItemText(12, _translate("AnotherWindow", "de2"))
        self.team_role_combobox.setItemText(13, _translate("AnotherWindow", "dt1"))
        self.team_role_combobox.setItemText(14, _translate("AnotherWindow", "dt2"))
        self.team_role_combobox.setItemText(15, _translate("AnotherWindow", "lb1"))
        self.team_role_combobox.setItemText(16, _translate("AnotherWindow", "lb2"))
        self.team_role_combobox.setItemText(17, _translate("AnotherWindow", "lb3"))
        self.team_role_combobox.setItemText(18, _translate("AnotherWindow", "cb1"))
        self.team_role_combobox.setItemText(19, _translate("AnotherWindow", "cb2"))
        self.team_role_combobox.setItemText(20, _translate("AnotherWindow", "s1"))
        self.team_role_combobox.setItemText(21, _translate("AnotherWindow", "s2"))
        self.team_role_combobox.setItemText(22, _translate("AnotherWindow", "kicker"))
        self.available_players.setSortingEnabled(True)
        item = self.available_players.horizontalHeaderItem(1)
        item.setText(_translate("AnotherWindow", "Player Name"))
        item = self.available_players.horizontalHeaderItem(2)
        item.setText(_translate("AnotherWindow", "Position"))
        item = self.available_players.horizontalHeaderItem(3)
        item.setText(_translate("AnotherWindow", "Receptions"))
        item = self.available_players.horizontalHeaderItem(4)
        item.setText(_translate("AnotherWindow", "Total Yards"))
        item = self.available_players.horizontalHeaderItem(5)
        item.setText(_translate("AnotherWindow", "Touchdowns"))
        item = self.available_players.horizontalHeaderItem(6)
        item.setText(_translate("AnotherWindow", "Turnovers Lost"))
        item = self.available_players.horizontalHeaderItem(7)
        item.setText(_translate("AnotherWindow", "Sacks"))
        item = self.available_players.horizontalHeaderItem(8)
        item.setText(_translate("AnotherWindow", "Tackles for Loss"))
        item = self.available_players.horizontalHeaderItem(9)
        item.setText(_translate("AnotherWindow", "Interceptions"))
        item = self.available_players.horizontalHeaderItem(10)
        item.setText(_translate("AnotherWindow", "Fumbles Recovered"))
        item = self.available_players.horizontalHeaderItem(11)
        item.setText(_translate("AnotherWindow", "Punting Yards"))
        item = self.available_players.horizontalHeaderItem(12)
        item.setText(_translate("AnotherWindow", "FG Percentage"))
        item = self.available_players.horizontalHeaderItem(13)
        item.setText(_translate("AnotherWindow", "Injury Status"))
        item = self.available_players.horizontalHeaderItem(14)
        item.setText(_translate("AnotherWindow", "College"))
        item = self.available_players.horizontalHeaderItem(15)
        item.setText(_translate("AnotherWindow", "Score"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.player_stats_tab), _translate("AnotherWindow", "Available Players"))
        self.pushButton.setText(_translate("AnotherWindow", "Change Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_tab), _translate("AnotherWindow", "Profile"))
        self.touchdowns_label.setText(_translate("AnotherWindow", "Touchdowns:"))
        self.title_label.setText(_translate("AnotherWindow", "Fill the weighted values below:"))
        self.fg_percentage_label.setText(_translate("AnotherWindow", "Field Goal Percentage:"))
        self.submit_button.setText(_translate("AnotherWindow", "Submit"))
        self.receptions_label.setText(_translate("AnotherWindow", "Receptions:"))
        self.punting_label.setText(_translate("AnotherWindow", "Punting Yards:"))
        self.yards_label.setText(_translate("AnotherWindow", "Total Yards:"))
        self.sacks_label.setText(_translate("AnotherWindow", "Sacks:"))
        self.fumbles_label.setText(_translate("AnotherWindow", "Fumbles Recovered:"))
        self.interceptions_label.setText(_translate("AnotherWindow", "Interceptions:"))
        self.turnovers_label.setText(_translate("AnotherWindow", "Turnovers Lost:"))
        self.tfl_label.setText(_translate("AnotherWindow", "Tackles for Loss:"))
        self.label.setText(_translate("AnotherWindow", "Enter 0.0 for no weight"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("AnotherWindow", "Settings"))
