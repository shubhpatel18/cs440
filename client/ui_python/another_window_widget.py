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
        AnotherWindow.resize(800, 600)
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
        self.tabWidget.addTab(self.settings_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        AnotherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AnotherWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(AnotherWindow)

    def retranslateUi(self, AnotherWindow):
        _translate = QtCore.QCoreApplication.translate
        AnotherWindow.setWindowTitle(_translate("AnotherWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_team_tab), _translate("AnotherWindow", "Create Team"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view_team_tab), _translate("AnotherWindow", "View Team"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.player_stats_tab), _translate("AnotherWindow", "Player Stats"))
        self.pushButton.setText(_translate("AnotherWindow", "Change Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_tab), _translate("AnotherWindow", "Profile"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("AnotherWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnotherWindow = QtWidgets.QMainWindow()
    ui = Ui_AnotherWindow()
    ui.setupUi(AnotherWindow)
    AnotherWindow.show()
    sys.exit(app.exec_())
