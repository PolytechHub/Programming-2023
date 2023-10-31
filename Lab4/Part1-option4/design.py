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
        Form.resize(708, 539)
        Form.setMinimumSize(QtCore.QSize(708, 539))
        Form.setMaximumSize(QtCore.QSize(708, 539))
        self.labelGraph = QtWidgets.QLabel(parent=Form)
        self.labelGraph.setGeometry(QtCore.QRect(10, 10, 371, 171))
        self.labelGraph.setText("")
        self.labelGraph.setPixmap(QtGui.QPixmap("graph.png"))
        self.labelGraph.setScaledContents(True)
        self.labelGraph.setObjectName("labelGraph")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(400, 10, 301, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridControl = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridControl.setContentsMargins(0, 0, 0, 0)
        self.gridControl.setObjectName("gridControl")
        self.boxStep = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxStep.setDecimals(2)
        self.boxStep.setMinimum(0.0)
        self.boxStep.setMaximum(16.0)
        self.boxStep.setProperty("value", 1.0)
        self.boxStep.setObjectName("boxStep")
        self.gridControl.addWidget(self.boxStep, 2, 1, 1, 1)
        self.labelEndValue = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelEndValue.setObjectName("labelEndValue")
        self.gridControl.addWidget(self.labelEndValue, 1, 0, 1, 1)
        self.labelStartValue = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.labelStartValue.setFont(font)
        self.labelStartValue.setObjectName("labelStartValue")
        self.gridControl.addWidget(self.labelStartValue, 0, 0, 1, 1)
        self.boxStartValue = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxStartValue.setDecimals(2)
        self.boxStartValue.setMinimum(-10.0)
        self.boxStartValue.setMaximum(6.0)
        self.boxStartValue.setProperty("value", -10.0)
        self.boxStartValue.setObjectName("boxStartValue")
        self.gridControl.addWidget(self.boxStartValue, 0, 1, 1, 1)
        self.labelStep = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.labelStep.setObjectName("labelStep")
        self.gridControl.addWidget(self.labelStep, 2, 0, 1, 1)
        self.boxEndValue = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.boxEndValue.setDecimals(2)
        self.boxEndValue.setMinimum(-10.0)
        self.boxEndValue.setMaximum(6.0)
        self.boxEndValue.setProperty("value", 6.0)
        self.boxEndValue.setObjectName("boxEndValue")
        self.gridControl.addWidget(self.boxEndValue, 1, 1, 1, 1)
        self.buttonResult = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buttonResult.setObjectName("buttonResult")
        self.gridControl.addWidget(self.buttonResult, 3, 0, 1, 1)
        self.buttonClear = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.buttonClear.setObjectName("buttonClear")
        self.gridControl.addWidget(self.buttonClear, 3, 1, 1, 1)
        self.table = QtWidgets.QTableWidget(parent=Form)
        self.table.setGeometry(QtCore.QRect(10, 210, 691, 321))
        self.table.setAutoFillBackground(False)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setObjectName("table")
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.horizontalHeader().setStretchLastSection(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вычисление значений функции"))
        self.labelEndValue.setText(_translate("Form", "Конечное значение"))
        self.labelStartValue.setText(_translate("Form", "Начальное значение"))
        self.labelStep.setText(_translate("Form", "Шаг"))
        self.buttonResult.setText(_translate("Form", "Результат"))
        self.buttonClear.setText(_translate("Form", "Очистить"))
        self.table.setSortingEnabled(False)
