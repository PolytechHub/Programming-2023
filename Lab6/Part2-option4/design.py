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
        Form.resize(510, 468)
        Form.setMinimumSize(QtCore.QSize(510, 468))
        Form.setMaximumSize(QtCore.QSize(510, 468))
        self.labelF1a = QtWidgets.QLabel(parent=Form)
        self.labelF1a.setGeometry(QtCore.QRect(10, 10, 481, 41))
        self.labelF1a.setText("")
        self.labelF1a.setPixmap(QtGui.QPixmap("images/f1a.png"))
        self.labelF1a.setScaledContents(True)
        self.labelF1a.setObjectName("labelF1a")
        self.boxF1a = QtWidgets.QLineEdit(parent=Form)
        self.boxF1a.setGeometry(QtCore.QRect(10, 60, 481, 22))
        self.boxF1a.setObjectName("boxF1a")
        self.buttonF1aGen = QtWidgets.QPushButton(parent=Form)
        self.buttonF1aGen.setGeometry(QtCore.QRect(10, 120, 171, 31))
        self.buttonF1aGen.setObjectName("buttonF1aGen")
        self.buttonF1aEval = QtWidgets.QPushButton(parent=Form)
        self.buttonF1aEval.setGeometry(QtCore.QRect(310, 120, 181, 31))
        self.buttonF1aEval.setObjectName("buttonF1aEval")
        self.labelF1b = QtWidgets.QLabel(parent=Form)
        self.labelF1b.setGeometry(QtCore.QRect(10, 160, 481, 51))
        self.labelF1b.setText("")
        self.labelF1b.setPixmap(QtGui.QPixmap("images/f1b.png"))
        self.labelF1b.setScaledContents(True)
        self.labelF1b.setObjectName("labelF1b")
        self.buttonF1bGen = QtWidgets.QPushButton(parent=Form)
        self.buttonF1bGen.setGeometry(QtCore.QRect(10, 280, 171, 31))
        self.buttonF1bGen.setObjectName("buttonF1bGen")
        self.buttonF1bEval = QtWidgets.QPushButton(parent=Form)
        self.buttonF1bEval.setGeometry(QtCore.QRect(300, 280, 181, 31))
        self.buttonF1bEval.setObjectName("buttonF1bEval")
        self.LabelF2 = QtWidgets.QLabel(parent=Form)
        self.LabelF2.setGeometry(QtCore.QRect(10, 320, 481, 41))
        self.LabelF2.setText("")
        self.LabelF2.setPixmap(QtGui.QPixmap("images/f2.png"))
        self.LabelF2.setScaledContents(True)
        self.LabelF2.setObjectName("LabelF2")
        self.boxF1b = QtWidgets.QLineEdit(parent=Form)
        self.boxF1b.setGeometry(QtCore.QRect(10, 220, 481, 22))
        self.boxF1b.setObjectName("boxF1b")
        self.labelF2k = QtWidgets.QLabel(parent=Form)
        self.labelF2k.setGeometry(QtCore.QRect(10, 430, 16, 16))
        self.labelF2k.setObjectName("labelF2k")
        self.labelF2C = QtWidgets.QLabel(parent=Form)
        self.labelF2C.setGeometry(QtCore.QRect(65, 430, 16, 16))
        self.labelF2C.setObjectName("labelF2C")
        self.boxF2 = QtWidgets.QLineEdit(parent=Form)
        self.boxF2.setGeometry(QtCore.QRect(10, 370, 481, 22))
        self.boxF2.setObjectName("boxF2")
        self.buttonF2Gen = QtWidgets.QPushButton(parent=Form)
        self.buttonF2Gen.setGeometry(QtCore.QRect(120, 430, 171, 31))
        self.buttonF2Gen.setObjectName("buttonF2Gen")
        self.buttonF2Eval = QtWidgets.QPushButton(parent=Form)
        self.buttonF2Eval.setGeometry(QtCore.QRect(300, 430, 181, 31))
        self.buttonF2Eval.setObjectName("buttonF2Eval")
        self.boxF2k = QtWidgets.QSpinBox(parent=Form)
        self.boxF2k.setGeometry(QtCore.QRect(20, 430, 42, 22))
        self.boxF2k.setObjectName("boxF2k")
        self.boxF2C = QtWidgets.QSpinBox(parent=Form)
        self.boxF2C.setGeometry(QtCore.QRect(75, 430, 42, 22))
        self.boxF2C.setMinimum(1)
        self.boxF2C.setObjectName("boxF2C")
        self.boxF1aAns = QtWidgets.QLineEdit(parent=Form)
        self.boxF1aAns.setGeometry(QtCore.QRect(10, 90, 481, 22))
        self.boxF1aAns.setReadOnly(True)
        self.boxF1aAns.setObjectName("boxF1aAns")
        self.boxF1bAns = QtWidgets.QLineEdit(parent=Form)
        self.boxF1bAns.setGeometry(QtCore.QRect(10, 250, 481, 22))
        self.boxF1bAns.setReadOnly(True)
        self.boxF1bAns.setObjectName("boxF1bAns")
        self.boxF2Ans = QtWidgets.QLineEdit(parent=Form)
        self.boxF2Ans.setGeometry(QtCore.QRect(10, 400, 481, 22))
        self.boxF2Ans.setReadOnly(True)
        self.boxF2Ans.setObjectName("boxF2Ans")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Лабораторная работа №6. Часть 2"))
        self.boxF1a.setPlaceholderText(_translate("Form", "Введите элементы массива через пробел, либо нажмите \"Сгенерировать\""))
        self.buttonF1aGen.setText(_translate("Form", "Сгенерировать"))
        self.buttonF1aEval.setText(_translate("Form", "Выполнить"))
        self.buttonF1bGen.setText(_translate("Form", "Сгенерировать"))
        self.buttonF1bEval.setText(_translate("Form", "Выполнить"))
        self.boxF1b.setPlaceholderText(_translate("Form", "Введите элементы массива через пробел, либо нажмите \"Сгенерировать\""))
        self.labelF2k.setText(_translate("Form", "k"))
        self.labelF2C.setText(_translate("Form", "C"))
        self.boxF2.setPlaceholderText(_translate("Form", "Введите элементы массива через пробел, либо нажмите \"Сгенерировать\""))
        self.buttonF2Gen.setText(_translate("Form", "Сгенерировать"))
        self.buttonF2Eval.setText(_translate("Form", "Выполнить"))
        self.boxF1aAns.setPlaceholderText(_translate("Form", "Здесь будет ответ"))
        self.boxF1bAns.setPlaceholderText(_translate("Form", "Здесь будет ответ"))
        self.boxF2Ans.setPlaceholderText(_translate("Form", "Здесь будет ответ"))
