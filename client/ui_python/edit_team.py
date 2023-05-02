# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client/ui_xml/edit_team_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditTeamDialog(object):
    def setupUi(self, EditTeamDialog):
        EditTeamDialog.setObjectName("EditTeamDialog")
        EditTeamDialog.resize(672, 609)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditTeamDialog.sizePolicy().hasHeightForWidth())
        EditTeamDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditTeamDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(EditTeamDialog)
        self.label_3.setStyleSheet("font: 24pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(EditTeamDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.current_password_label = QtWidgets.QLabel(EditTeamDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_password_label.sizePolicy().hasHeightForWidth())
        self.current_password_label.setSizePolicy(sizePolicy)
        self.current_password_label.setText("")
        self.current_password_label.setObjectName("current_password_label")
        self.gridLayout.addWidget(self.current_password_label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.edit_team_input = QtWidgets.QLineEdit(EditTeamDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_team_input.sizePolicy().hasHeightForWidth())
        self.edit_team_input.setSizePolicy(sizePolicy)
        self.edit_team_input.setObjectName("edit_team_input")
        self.gridLayout.addWidget(self.edit_team_input, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditTeamDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(EditTeamDialog)
        self.buttonBox.accepted.connect(EditTeamDialog.accept)
        self.buttonBox.rejected.connect(EditTeamDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditTeamDialog)

    def retranslateUi(self, EditTeamDialog):
        _translate = QtCore.QCoreApplication.translate
        EditTeamDialog.setWindowTitle(_translate("EditTeamDialog", "Sign In"))
        self.label_3.setText(_translate("EditTeamDialog", "Enter a new Team Name"))
