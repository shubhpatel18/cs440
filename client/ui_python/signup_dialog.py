# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_xml/signup_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignupDialog(object):
    def setupUi(self, SignupDialog):
        SignupDialog.setObjectName("SignupDialog")
        SignupDialog.resize(390, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SignupDialog.sizePolicy().hasHeightForWidth())
        SignupDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(SignupDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(SignupDialog)
        self.label_3.setStyleSheet("font: 24pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(SignupDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.username_label = QtWidgets.QLabel(SignupDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_label.sizePolicy().hasHeightForWidth())
        self.username_label.setSizePolicy(sizePolicy)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.name_label = QtWidgets.QLabel(SignupDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.password_label = QtWidgets.QLabel(SignupDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_label.sizePolicy().hasHeightForWidth())
        self.password_label.setSizePolicy(sizePolicy)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.username_edit = QtWidgets.QLineEdit(SignupDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_edit.sizePolicy().hasHeightForWidth())
        self.username_edit.setSizePolicy(sizePolicy)
        self.username_edit.setObjectName("username_edit")
        self.gridLayout.addWidget(self.username_edit, 0, 1, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(SignupDialog)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 1, 1, 1, 1)
        self.password_edit = QtWidgets.QLineEdit(SignupDialog)
        self.password_edit.setObjectName("password_edit")
        self.gridLayout.addWidget(self.password_edit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SignupDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(SignupDialog)
        self.buttonBox.accepted.connect(SignupDialog.accept)
        self.buttonBox.rejected.connect(SignupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SignupDialog)

    def retranslateUi(self, SignupDialog):
        _translate = QtCore.QCoreApplication.translate
        SignupDialog.setWindowTitle(_translate("SignupDialog", "Sign Up"))
        self.label_3.setText(_translate("SignupDialog", "Please Sign Up"))
        self.username_label.setText(_translate("SignupDialog", "Username:"))
        self.name_label.setText(_translate("SignupDialog", "Name: "))
        self.password_label.setText(_translate("SignupDialog", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignupDialog = QtWidgets.QDialog()
    ui = Ui_SignupDialog()
    ui.setupUi(SignupDialog)
    SignupDialog.show()
    sys.exit(app.exec_())
