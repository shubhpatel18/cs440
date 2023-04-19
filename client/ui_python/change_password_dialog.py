# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_password_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setObjectName("ChangePasswordDialog")
        ChangePasswordDialog.resize(672, 726)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChangePasswordDialog.sizePolicy().hasHeightForWidth())
        ChangePasswordDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChangePasswordDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(ChangePasswordDialog)
        self.label_3.setStyleSheet("font: 24pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(ChangePasswordDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.current_password_label = QtWidgets.QLabel(ChangePasswordDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_password_label.sizePolicy().hasHeightForWidth())
        self.current_password_label.setSizePolicy(sizePolicy)
        self.current_password_label.setObjectName("current_password_label")
        self.gridLayout.addWidget(self.current_password_label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.new_password_label_2 = QtWidgets.QLabel(ChangePasswordDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_password_label_2.sizePolicy().hasHeightForWidth())
        self.new_password_label_2.setSizePolicy(sizePolicy)
        self.new_password_label_2.setObjectName("new_password_label_2")
        self.gridLayout.addWidget(self.new_password_label_2, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.current_password_edit = QtWidgets.QLineEdit(ChangePasswordDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_password_edit.sizePolicy().hasHeightForWidth())
        self.current_password_edit.setSizePolicy(sizePolicy)
        self.current_password_edit.setObjectName("current_password_edit")
        self.current_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.current_password_edit, 0, 2, 1, 1)
        self.new_password_edit_1 = QtWidgets.QLineEdit(ChangePasswordDialog)
        self.new_password_edit_1.setObjectName("new_password_edit_1")
        self.new_password_edit_1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.new_password_edit_1, 1, 2, 1, 1)
        self.new_password_edit_2 = QtWidgets.QLineEdit(ChangePasswordDialog)
        self.new_password_edit_2.setObjectName("new_password_edit_2")
        self.new_password_edit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.new_password_edit_2, 2, 2, 1, 1)
        self.new_password_label_1 = QtWidgets.QLabel(ChangePasswordDialog)
        self.new_password_label_1.setObjectName("new_password_label_1")
        self.gridLayout.addWidget(self.new_password_label_1, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChangePasswordDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(ChangePasswordDialog)
        self.buttonBox.accepted.connect(ChangePasswordDialog.accept)
        self.buttonBox.rejected.connect(ChangePasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(_translate("ChangePasswordDialog", "Change Password"))
        self.label_3.setText(_translate("ChangePasswordDialog", "Change Password"))
        self.current_password_label.setText(_translate("ChangePasswordDialog", "Current Password:"))
        self.new_password_label_2.setText(_translate("ChangePasswordDialog", "Verify New Password:"))
        self.new_password_label_1.setText(_translate("ChangePasswordDialog", "New Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChangePasswordDialog = QtWidgets.QDialog()
    ui = Ui_ChangePasswordDialog()
    ui.setupUi(ChangePasswordDialog)
    ChangePasswordDialog.show()
    sys.exit(app.exec_())
