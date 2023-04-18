# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(672, 726)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(LoginDialog)
        self.label_3.setStyleSheet("font: 24pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(LoginDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.current_password_label = QtWidgets.QLabel(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_password_label.sizePolicy().hasHeightForWidth())
        self.current_password_label.setSizePolicy(sizePolicy)
        self.current_password_label.setObjectName("current_password_label")
        self.gridLayout.addWidget(self.current_password_label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.new_password_label2 = QtWidgets.QLabel(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_password_label2.sizePolicy().hasHeightForWidth())
        self.new_password_label2.setSizePolicy(sizePolicy)
        self.new_password_label2.setObjectName("new_password_label2")
        self.gridLayout.addWidget(self.new_password_label2, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.current_password_edit = QtWidgets.QLineEdit(LoginDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_password_edit.sizePolicy().hasHeightForWidth())
        self.current_password_edit.setSizePolicy(sizePolicy)
        self.current_password_edit.setObjectName("current_password_edit")
        self.gridLayout.addWidget(self.current_password_edit, 0, 2, 1, 1)
        self.new_password_edit_2 = QtWidgets.QLineEdit(LoginDialog)
        self.new_password_edit_2.setObjectName("new_password_edit_2")
        self.gridLayout.addWidget(self.new_password_edit_2, 2, 2, 1, 1)
        self.new_password_edit_1 = QtWidgets.QLineEdit(LoginDialog)
        self.new_password_edit_1.setObjectName("new_password_edit_1")
        self.gridLayout.addWidget(self.new_password_edit_1, 1, 2, 1, 1)
        self.new_password_label_1 = QtWidgets.QLabel(LoginDialog)
        self.new_password_label_1.setObjectName("new_password_label_1")
        self.gridLayout.addWidget(self.new_password_label_1, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoginDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(LoginDialog)
        self.buttonBox.accepted.connect(LoginDialog.accept)
        self.buttonBox.rejected.connect(LoginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Sign In"))
        self.label_3.setText(_translate("LoginDialog", "Edit Profile"))
        self.current_password_label.setText(_translate("LoginDialog", "Current Password:"))
        self.new_password_label2.setText(_translate("LoginDialog", "Verify New Password:"))
        self.new_password_label_1.setText(_translate("LoginDialog", "New Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginDialog = QtWidgets.QDialog()
    ui = Ui_LoginDialog()
    ui.setupUi(LoginDialog)
    LoginDialog.show()
    sys.exit(app.exec_())
