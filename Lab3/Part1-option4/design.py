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
        Form.setEnabled(True)
        Form.resize(350, 151)
        Form.setMinimumSize(QtCore.QSize(350, 151))
        Form.setMaximumSize(QtCore.QSize(350, 151))
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelNum2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelNum2.setObjectName("labelNum2")
        self.gridLayout.addWidget(self.labelNum2, 1, 0, 1, 1)
        self.boxNum1 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.boxNum1.setObjectName("boxNum1")
        self.gridLayout.addWidget(self.boxNum1, 0, 1, 1, 1)
        self.labelResult = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelResult.setFont(font)
        self.labelResult.setWordWrap(True)
        self.labelResult.setObjectName("labelResult")
        self.gridLayout.addWidget(self.labelResult, 3, 0, 1, 1)
        self.boxNum3 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.boxNum3.setObjectName("boxNum3")
        self.gridLayout.addWidget(self.boxNum3, 2, 1, 1, 1)
        self.labelNum3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelNum3.setObjectName("labelNum3")
        self.gridLayout.addWidget(self.labelNum3, 2, 0, 1, 1)
        self.boxNum2 = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.boxNum2.setObjectName("boxNum2")
        self.gridLayout.addWidget(self.boxNum2, 1, 1, 1, 1)
        self.labelNum1 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelNum1.setObjectName("labelNum1")
        self.gridLayout.addWidget(self.labelNum1, 0, 0, 1, 1)
        self.buttonResult = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buttonResult.setObjectName("buttonResult")
        self.gridLayout.addWidget(self.buttonResult, 0, 2, 1, 1)
        self.buttonClear = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buttonClear.setObjectName("buttonClear")
        self.gridLayout.addWidget(self.buttonClear, 1, 2, 1, 1)
        self.buttonClose = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buttonClose.setObjectName("buttonClose")
        self.gridLayout.addWidget(self.buttonClose, 2, 2, 1, 1)
        self.boxResult = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.boxResult.setReadOnly(True)
        self.boxResult.setObjectName("boxResult")
        self.gridLayout.addWidget(self.boxResult, 3, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Поиск среднего числа"))
        self.labelNum2.setText(_translate("Form", "Число №2"))
        self.labelResult.setText(_translate("Form", "Результат:"))
        self.labelNum3.setText(_translate("Form", "Число №3"))
        self.labelNum1.setText(_translate("Form", "Число №1"))
        self.buttonResult.setText(_translate("Form", "Результат"))
        self.buttonClear.setText(_translate("Form", "Очистить"))
        self.buttonClose.setText(_translate("Form", "Закрыть"))