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
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.boxTime = QtWidgets.QTimeEdit(parent=Form)
        self.boxTime.setGeometry(QtCore.QRect(80, 90, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(80)
        self.boxTime.setFont(font)
        self.boxTime.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.boxTime.setStyleSheet("background-color: red;\n"
"color: white;")
        self.boxTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.boxTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(1999, 12, 31), QtCore.QTime(11, 59, 59)))
        self.boxTime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1999, 12, 30), QtCore.QTime(0, 0, 0)))
        self.boxTime.setMaximumDate(QtCore.QDate(1999, 12, 31))
        self.boxTime.setMaximumTime(QtCore.QTime(11, 59, 59))
        self.boxTime.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.boxTime.setCalendarPopup(False)
        self.boxTime.setTime(QtCore.QTime(9, 0, 0))
        self.boxTime.setObjectName("boxTime")
        self.labelGetTime = QtWidgets.QLabel(parent=Form)
        self.labelGetTime.setGeometry(QtCore.QRect(100, 60, 201, 25))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelGetTime.setFont(font)
        self.labelGetTime.setStyleSheet("background-color: red;\n"
"color: white;")
        self.labelGetTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelGetTime.setWordWrap(True)
        self.labelGetTime.setObjectName("labelGetTime")
        self.buttonResult = QtWidgets.QPushButton(parent=Form)
        self.buttonResult.setGeometry(QtCore.QRect(120, 200, 151, 32))
        self.buttonResult.setStyleSheet("background-color: red;\n"
"color: white")
        self.buttonResult.setObjectName("buttonResult")
        self.labelBackground = QtWidgets.QLabel(parent=Form)
        self.labelBackground.setGeometry(QtCore.QRect(-30, -10, 451, 311))
        self.labelBackground.setMinimumSize(QtCore.QSize(451, 311))
        self.labelBackground.setMaximumSize(QtCore.QSize(451, 311))
        self.labelBackground.setFocusPolicy(QtCore.Qt.FocusPolicy.WheelFocus)
        self.labelBackground.setText("")
        self.labelBackground.setPixmap(QtGui.QPixmap("res/backgroung.png"))
        self.labelBackground.setScaledContents(True)
        self.labelBackground.setObjectName("labelBackground")
        self.labelBackground.raise_()
        self.boxTime.raise_()
        self.labelGetTime.raise_()
        self.buttonResult.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Злой Ваня v1.0.0"))
        self.labelGetTime.setText(_translate("Form", "Введите время"))
        self.buttonResult.setText(_translate("Form", "Конвертировать"))
