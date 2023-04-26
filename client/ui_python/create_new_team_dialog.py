# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client/ui_xml/create_new_team_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateNewTeamDialog(object):
    def setupUi(self, CreateNewTeamDialog):
        CreateNewTeamDialog.setObjectName("CreateNewTeamDialog")
        CreateNewTeamDialog.resize(701, 524)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreateNewTeamDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 189, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(CreateNewTeamDialog)
        self.label_3.setStyleSheet("font: 24pt \"Ubuntu\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line = QtWidgets.QFrame(CreateNewTeamDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.team_name_edit = QtWidgets.QLineEdit(CreateNewTeamDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.team_name_edit.sizePolicy().hasHeightForWidth())
        self.team_name_edit.setSizePolicy(sizePolicy)
        self.team_name_edit.setAcceptDrops(False)
        self.team_name_edit.setObjectName("team_name_edit")
        self.gridLayout.addWidget(self.team_name_edit, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 189, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreateNewTeamDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CreateNewTeamDialog)
        QtCore.QMetaObject.connectSlotsByName(CreateNewTeamDialog)

    def retranslateUi(self, CreateNewTeamDialog):
        _translate = QtCore.QCoreApplication.translate
        CreateNewTeamDialog.setWindowTitle(_translate("CreateNewTeamDialog", "Create New Team"))
        self.label_3.setText(_translate("CreateNewTeamDialog", "Please Enter a New Team Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateNewTeamDialog = QtWidgets.QDialog()
    ui = Ui_CreateNewTeamDialog()
    ui.setupUi(CreateNewTeamDialog)
    CreateNewTeamDialog.show()
    sys.exit(app.exec_())
