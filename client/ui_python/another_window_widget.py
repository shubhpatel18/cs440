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
        self.profile_tab = QtWidgets.QWidget()
        self.profile_tab.setObjectName("profile_tab")
        self.tabWidget.addTab(self.profile_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        AnotherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AnotherWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AnotherWindow)

    def retranslateUi(self, AnotherWindow):
        _translate = QtCore.QCoreApplication.translate
        AnotherWindow.setWindowTitle(_translate("AnotherWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile_tab), _translate("AnotherWindow", "Profile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AnotherWindow = QtWidgets.QMainWindow()
    ui = Ui_AnotherWindow()
    ui.setupUi(AnotherWindow)
    AnotherWindow.show()
    sys.exit(app.exec_())
