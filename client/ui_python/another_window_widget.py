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
        AnotherWindow.resize(922, 680)
        self.centralwidget = QtWidgets.QWidget(AnotherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.create_team_tab = QtWidgets.QWidget()
        self.create_team_tab.setObjectName("create_team_tab")
        self.tabWidget.addTab(self.create_team_tab, "")
        self.view_team_tab = QtWidgets.QWidget()
        self.view_team_tab.setObjectName("view_team_tab")
        self.tabWidget.addTab(self.view_team_tab, "")
        self.player_stats_tab = QtWidgets.QWidget()
        self.player_stats_tab.setObjectName("player_stats_tab")
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
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(AnotherWindow)

    def retranslateUi(self, AnotherWindow):
        _translate = QtCore.QCoreApplication.translate
        AnotherWindow.setWindowTitle(_translate("AnotherWindow", "Roster Rookies"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_team_tab), _translate("AnotherWindow", "Create Team"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view_team_tab), _translate("AnotherWindow", "View Team"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.player_stats_tab), _translate("AnotherWindow", "Player Stats"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnotherWindow = QtWidgets.QMainWindow()
    ui = Ui_AnotherWindow()
    ui.setupUi(AnotherWindow)
    AnotherWindow.show()
    sys.exit(app.exec_())
