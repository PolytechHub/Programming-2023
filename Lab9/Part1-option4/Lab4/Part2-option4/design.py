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
        Form.resize(708, 195)
        Form.setMinimumSize(QtCore.QSize(708, 195))
        Form.setMaximumSize(QtCore.QSize(708, 195))
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 671, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridControl = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridControl.setContentsMargins(0, 0, 0, 0)
        self.gridControl.setObjectName("gridControl")
        self.labelA = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.labelA.setFont(font)
        self.labelA.setObjectName("labelA")
        self.gridControl.addWidget(self.labelA, 0, 0, 1, 1)
        self.labelC = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelC.setObjectName("labelC")
        self.gridControl.addWidget(self.labelC, 3, 0, 1, 1)
        self.labelB = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelB.setObjectName("labelB")
        self.gridControl.addWidget(self.labelB, 2, 0, 1, 1)
        self.buttonRandom = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buttonRandom.setObjectName("buttonRandom")
        self.gridControl.addWidget(self.buttonRandom, 5, 1, 1, 1)
        self.boxC = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxC.setMinimum(0.0)
        self.boxC.setMaximum(0.99)
        self.boxC.setSingleStep(0.01)
        self.boxC.setObjectName("boxC")
        self.gridControl.addWidget(self.boxC, 3, 1, 1, 1)
        self.labelD = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.labelD.setFont(font)
        self.labelD.setObjectName("labelD")
        self.gridControl.addWidget(self.labelD, 4, 0, 1, 1)
        self.boxD = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxD.setMinimum(0.0)
        self.boxD.setMaximum(0.99)
        self.boxD.setSingleStep(0.01)
        self.boxD.setProperty("value", 0.05)
        self.boxD.setObjectName("boxD")
        self.gridControl.addWidget(self.boxD, 4, 1, 1, 1)
        self.buttonResult = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buttonResult.setObjectName("buttonResult")
        self.gridControl.addWidget(self.buttonResult, 5, 0, 1, 1)
        self.boxB = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.boxB.setMinimum(-100)
        self.boxB.setMaximum(100)
        self.boxB.setProperty("value", 5)
        self.boxB.setObjectName("boxB")
        self.gridControl.addWidget(self.boxB, 2, 1, 1, 1)
        self.boxA = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.boxA.setMinimum(-100)
        self.boxA.setMaximum(100)
        self.boxA.setProperty("value", 1)
        self.boxA.setObjectName("boxA")
        self.gridControl.addWidget(self.boxA, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вычисление десятичных антилогарифмов"))
        self.labelA.setText(_translate("Form", "Значение A"))
        self.labelC.setText(_translate("Form", "Значение С"))
        self.labelB.setText(_translate("Form", "Значение B"))
        self.buttonRandom.setText(_translate("Form", "Случайное значение"))
        self.labelD.setText(_translate("Form", "Значение D"))
        self.buttonResult.setText(_translate("Form", "Результат"))
