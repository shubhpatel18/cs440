# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_xml/add_player.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPlayerDialog(object):
    def setupUi(self, AddPlayerDialog):
        AddPlayerDialog.setObjectName("AddPlayerDialog")
        AddPlayerDialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddPlayerDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBox = QtWidgets.QComboBox(AddPlayerDialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 361, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(AddPlayerDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 351, 20))
        self.label.setObjectName("label")
        self.warning_box = QtWidgets.QLabel(AddPlayerDialog)
        self.warning_box.setGeometry(QtCore.QRect(20, 90, 361, 141))
        self.warning_box.setText("")
        self.warning_box.setObjectName("warning_box")

        self.retranslateUi(AddPlayerDialog)
        self.buttonBox.accepted.connect(AddPlayerDialog.accept)
        self.buttonBox.rejected.connect(AddPlayerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddPlayerDialog)

    def retranslateUi(self, AddPlayerDialog):
        _translate = QtCore.QCoreApplication.translate
        AddPlayerDialog.setWindowTitle(_translate("AddPlayerDialog", "Dialog"))
        self.comboBox.setItemText(0, _translate("AddPlayerDialog", "QB"))
        self.comboBox.setItemText(1, _translate("AddPlayerDialog", "RB"))
        self.comboBox.setItemText(2, _translate("AddPlayerDialog", "WR1"))
        self.comboBox.setItemText(3, _translate("AddPlayerDialog", "WR2"))
        self.comboBox.setItemText(4, _translate("AddPlayerDialog", "TE"))
        self.comboBox.setItemText(5, _translate("AddPlayerDialog", "Flex"))
        self.comboBox.setItemText(6, _translate("AddPlayerDialog", "Center"))
        self.comboBox.setItemText(7, _translate("AddPlayerDialog", "LG"))
        self.comboBox.setItemText(8, _translate("AddPlayerDialog", "RG"))
        self.comboBox.setItemText(9, _translate("AddPlayerDialog", "Punter"))
        self.comboBox.setItemText(10, _translate("AddPlayerDialog", "DE1"))
        self.comboBox.setItemText(11, _translate("AddPlayerDialog", "DE2"))
        self.comboBox.setItemText(12, _translate("AddPlayerDialog", "DT1"))
        self.comboBox.setItemText(13, _translate("AddPlayerDialog", "DT2"))
        self.comboBox.setItemText(14, _translate("AddPlayerDialog", "LB1"))
        self.comboBox.setItemText(15, _translate("AddPlayerDialog", "LB2"))
        self.comboBox.setItemText(16, _translate("AddPlayerDialog", "LB3"))
        self.comboBox.setItemText(17, _translate("AddPlayerDialog", "CB1"))
        self.comboBox.setItemText(18, _translate("AddPlayerDialog", "CB2"))
        self.comboBox.setItemText(19, _translate("AddPlayerDialog", "S1"))
        self.comboBox.setItemText(20, _translate("AddPlayerDialog", "S2"))
        self.comboBox.setItemText(21, _translate("AddPlayerDialog", "Kicker"))
        self.label.setText(_translate("AddPlayerDialog", "Pick a position to fill:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPlayerDialog = QtWidgets.QDialog()
    ui = Ui_AddPlayerDialog()
    ui.setupUi(AddPlayerDialog)
    AddPlayerDialog.show()
    sys.exit(app.exec_())
