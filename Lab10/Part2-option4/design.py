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
        Form.resize(621, 397)
        Form.setMinimumSize(QtCore.QSize(621, 397))
        Form.setMaximumSize(QtCore.QSize(621, 397))
        Form.setWindowTitle("Вектор в двумерном пространстве")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 561, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridVectors = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridVectors.setContentsMargins(0, 0, 0, 0)
        self.gridVectors.setObjectName("gridVectors")
        self.LabelVector2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.LabelVector2.setObjectName("LabelVector2")
        self.gridVectors.addWidget(self.LabelVector2, 2, 0, 1, 1)
        self.boxY2 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxY2.setMinimum(-1000.0)
        self.boxY2.setMaximum(1000.0)
        self.boxY2.setProperty("value", 1.0)
        self.boxY2.setObjectName("boxY2")
        self.gridVectors.addWidget(self.boxY2, 2, 2, 1, 1)
        self.boxX1 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxX1.setMinimum(-1000.0)
        self.boxX1.setMaximum(1000.0)
        self.boxX1.setProperty("value", 1.0)
        self.boxX1.setObjectName("boxX1")
        self.gridVectors.addWidget(self.boxX1, 1, 1, 1, 1)
        self.labelX = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelX.setObjectName("labelX")
        self.gridVectors.addWidget(self.labelX, 0, 1, 1, 1)
        self.boxY1 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxY1.setMinimum(-1000.0)
        self.boxY1.setMaximum(1000.0)
        self.boxY1.setProperty("value", 1.0)
        self.boxY1.setObjectName("boxY1")
        self.gridVectors.addWidget(self.boxY1, 1, 2, 1, 1)
        self.labelPlug = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelPlug.setText("")
        self.labelPlug.setObjectName("labelPlug")
        self.gridVectors.addWidget(self.labelPlug, 0, 0, 1, 1)
        self.labelVector1 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelVector1.setObjectName("labelVector1")
        self.gridVectors.addWidget(self.labelVector1, 1, 0, 1, 1)
        self.boxX2 = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxX2.setMinimum(-1000.0)
        self.boxX2.setMaximum(1000.0)
        self.boxX2.setProperty("value", 1.0)
        self.boxX2.setObjectName("boxX2")
        self.gridVectors.addWidget(self.boxX2, 2, 1, 1, 1)
        self.labelAngle = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelAngle.setObjectName("labelAngle")
        self.gridVectors.addWidget(self.labelAngle, 3, 0, 1, 1)
        self.labelY = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelY.setObjectName("labelY")
        self.gridVectors.addWidget(self.labelY, 0, 2, 1, 1)
        self.boxAngle = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.boxAngle.setReadOnly(True)
        self.boxAngle.setObjectName("boxAngle")
        self.gridVectors.addWidget(self.boxAngle, 3, 1, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 180, 561, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelScalarProduct = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.labelScalarProduct.setObjectName("labelScalarProduct")
        self.gridLayout.addWidget(self.labelScalarProduct, 3, 0, 1, 1)
        self.labelPlug_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.labelPlug_2.setText("")
        self.labelPlug_2.setObjectName("labelPlug_2")
        self.gridLayout.addWidget(self.labelPlug_2, 0, 0, 1, 1)
        self.labelXAngle = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.labelXAngle.setObjectName("labelXAngle")
        self.gridLayout.addWidget(self.labelXAngle, 1, 0, 1, 1)
        self.labelYAngle = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.labelYAngle.setObjectName("labelYAngle")
        self.gridLayout.addWidget(self.labelYAngle, 2, 0, 1, 1)
        self.labelVector1C = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.labelVector1C.setObjectName("labelVector1C")
        self.gridLayout.addWidget(self.labelVector1C, 0, 1, 1, 1)
        self.labelVector2C = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.labelVector2C.setObjectName("labelVector2C")
        self.gridLayout.addWidget(self.labelVector2C, 0, 2, 1, 1)
        self.labelVectorProduct = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.labelVectorProduct.setObjectName("labelVectorProduct")
        self.gridLayout.addWidget(self.labelVectorProduct, 4, 0, 1, 1)
        self.buttonXAngle1 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.buttonXAngle1.setObjectName("buttonXAngle1")
        self.gridLayout.addWidget(self.buttonXAngle1, 1, 1, 1, 1)
        self.buttonXAngle2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.buttonXAngle2.setObjectName("buttonXAngle2")
        self.gridLayout.addWidget(self.buttonXAngle2, 1, 2, 1, 1)
        self.buttonYAngle1 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.buttonYAngle1.setObjectName("buttonYAngle1")
        self.gridLayout.addWidget(self.buttonYAngle1, 2, 1, 1, 1)
        self.buttonYAngle2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.buttonYAngle2.setObjectName("buttonYAngle2")
        self.gridLayout.addWidget(self.buttonYAngle2, 2, 2, 1, 1)
        self.buttonScalarProduct = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.buttonScalarProduct.setObjectName("buttonScalarProduct")
        self.gridLayout.addWidget(self.buttonScalarProduct, 3, 1, 1, 2)
        self.buttonVectorProduct = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.buttonVectorProduct.setObjectName("buttonVectorProduct")
        self.gridLayout.addWidget(self.buttonVectorProduct, 4, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.LabelVector2.setText(_translate("Form", "Вектор 2"))
        self.labelX.setText(_translate("Form", "X"))
        self.labelVector1.setText(_translate("Form", "Вектор 1 "))
        self.labelAngle.setText(_translate("Form", "Угол"))
        self.labelY.setText(_translate("Form", "Y"))
        self.labelScalarProduct.setText(_translate("Form", "Скалярное произведение"))
        self.labelXAngle.setText(_translate("Form", "Угол к Ox"))
        self.labelYAngle.setText(_translate("Form", "Угол к Oy"))
        self.labelVector1C.setText(_translate("Form", "Вектор 1"))
        self.labelVector2C.setText(_translate("Form", "Вектор 2"))
        self.labelVectorProduct.setText(_translate("Form", "Векторное произведение"))
        self.buttonXAngle1.setText(_translate("Form", "Рассчитать"))
        self.buttonXAngle2.setText(_translate("Form", "Рассчитать"))
        self.buttonYAngle1.setText(_translate("Form", "Рассчитать"))
        self.buttonYAngle2.setText(_translate("Form", "Рассчитать"))
        self.buttonScalarProduct.setText(_translate("Form", "Рассчитать"))
        self.buttonVectorProduct.setText(_translate("Form", "Рассчитать"))