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
        Form.resize(471, 300)
        Form.setMinimumSize(QtCore.QSize(471, 300))
        Form.setMaximumSize(QtCore.QSize(471, 300))
        Form.setWindowOpacity(1.0)
        self.frameRed = QtWidgets.QFrame(parent=Form)
        self.frameRed.setGeometry(QtCore.QRect(0, 0, 121, 301))
        self.frameRed.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.frameRed.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameRed.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameRed.setObjectName("frameRed")
        self.labelHelloUser = QtWidgets.QLabel(parent=self.frameRed)
        self.labelHelloUser.setGeometry(QtCore.QRect(10, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.labelHelloUser.setFont(font)
        self.labelHelloUser.setScaledContents(False)
        self.labelHelloUser.setWordWrap(True)
        self.labelHelloUser.setObjectName("labelHelloUser")
        self.buttonAuthorization = QtWidgets.QPushButton(parent=self.frameRed)
        self.buttonAuthorization.setGeometry(QtCore.QRect(5, 130, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonAuthorization.setFont(font)
        self.buttonAuthorization.setStyleSheet("color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"")
        self.buttonAuthorization.setObjectName("buttonAuthorization")
        self.buttonRegistration = QtWidgets.QPushButton(parent=self.frameRed)
        self.buttonRegistration.setGeometry(QtCore.QRect(5, 170, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonRegistration.setFont(font)
        self.buttonRegistration.setStyleSheet("color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"")
        self.buttonRegistration.setObjectName("buttonRegistration")
        self.buttonSupport = QtWidgets.QPushButton(parent=self.frameRed)
        self.buttonSupport.setGeometry(QtCore.QRect(5, 260, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonSupport.setFont(font)
        self.buttonSupport.setStyleSheet("color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.buttonSupport.setIcon(icon)
        self.buttonSupport.setObjectName("buttonSupport")
        self.labelAuthorization = QtWidgets.QLabel(parent=Form)
        self.labelAuthorization.setGeometry(QtCore.QRect(240, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.labelAuthorization.setFont(font)
        self.labelAuthorization.setScaledContents(False)
        self.labelAuthorization.setWordWrap(True)
        self.labelAuthorization.setObjectName("labelAuthorization")
        self.boxLogin = QtWidgets.QLineEdit(parent=Form)
        self.boxLogin.setGeometry(QtCore.QRect(210, 110, 161, 25))
        self.boxLogin.setAutoFillBackground(False)
        self.boxLogin.setStyleSheet("border: 1px solid rgb(100, 100, 100);\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;\n"
"color: rgb(100, 100, 100);")
        self.boxLogin.setInputMask("")
        self.boxLogin.setText("")
        self.boxLogin.setClearButtonEnabled(False)
        self.boxLogin.setObjectName("boxLogin")
        self.boxPassword = QtWidgets.QLineEdit(parent=Form)
        self.boxPassword.setGeometry(QtCore.QRect(210, 150, 161, 25))
        self.boxPassword.setAutoFillBackground(False)
        self.boxPassword.setStyleSheet("border: 1px solid rgb(100, 100, 100);\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 5px;\n"
"color: rgb(100, 100, 100);")
        self.boxPassword.setInputMask("")
        self.boxPassword.setText("")
        self.boxPassword.setObjectName("boxPassword")
        self.buttonEntry = QtWidgets.QPushButton(parent=Form)
        self.buttonEntry.setGeometry(QtCore.QRect(240, 190, 101, 23))
        self.buttonEntry.setStyleSheet("color: white;\n"
"border: 1px solid transparent;\n"
"border-radius: 5px;\n"
"background-color: rgb(170, 0, 0)")
        self.buttonEntry.setObjectName("buttonEntry")
        self.labelBackground = QtWidgets.QLabel(parent=Form)
        self.labelBackground.setGeometry(QtCore.QRect(120, -7, 351, 311))
        self.labelBackground.setText("")
        self.labelBackground.setPixmap(QtGui.QPixmap("res/background.png"))
        self.labelBackground.setScaledContents(True)
        self.labelBackground.setObjectName("labelBackground")
        self.labelBackground.raise_()
        self.frameRed.raise_()
        self.boxLogin.raise_()
        self.buttonEntry.raise_()
        self.boxPassword.raise_()
        self.labelAuthorization.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Математический тренажер"))
        self.labelHelloUser.setText(_translate("Form", "Добрый день, пользователь"))
        self.buttonAuthorization.setText(_translate("Form", "АВТОРИЗАЦИЯ"))
        self.buttonRegistration.setText(_translate("Form", "РЕГИСТРАЦИЯ"))
        self.buttonSupport.setText(_translate("Form", "ПОДДЕРЖКА"))
        self.labelAuthorization.setText(_translate("Form", "Авторизация"))
        self.boxLogin.setPlaceholderText(_translate("Form", "Логин..."))
        self.boxPassword.setPlaceholderText(_translate("Form", "Пароль..."))
        self.buttonEntry.setText(_translate("Form", "ВХОД"))
