# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(708, 470)
        Form.setMinimumSize(QtCore.QSize(708, 470))
        Form.setMaximumSize(QtCore.QSize(708, 470))
        self.boxN = QtWidgets.QSpinBox(parent=Form)
        self.boxN.setGeometry(QtCore.QRect(20, 10, 42, 22))
        self.boxN.setObjectName("boxN")
        self.labelN = QtWidgets.QLabel(parent=Form)
        self.labelN.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.labelN.setObjectName("labelN")
        self.table = QtWidgets.QTableWidget(parent=Form)
        self.table.setGeometry(QtCore.QRect(10, 70, 691, 381))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.buttonResult = QtWidgets.QPushButton(parent=Form)
        self.buttonResult.setGeometry(QtCore.QRect(160, 10, 80, 26))
        self.buttonResult.setObjectName("buttonResult")
        self.boxC = QtWidgets.QSpinBox(parent=Form)
        self.boxC.setGeometry(QtCore.QRect(90, 10, 42, 22))
        self.boxC.setObjectName("boxC")
        self.labelC = QtWidgets.QLabel(parent=Form)
        self.labelC.setGeometry(QtCore.QRect(80, 10, 16, 16))
        self.labelC.setObjectName("labelC")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lab7"))
        self.labelN.setText(_translate("Form", "n"))
        self.buttonResult.setText(_translate("Form", "Посчитать"))
        self.labelC.setText(_translate("Form", "C"))
