import sys
from math import sqrt
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6.QtGui import QFont

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.table.setHorizontalHeaderLabels(['X', 'Y'])
        header = self.table.horizontalHeader()
        for i in range(2):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
        
        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonClear.clicked.connect(self.clearHandler)
        self.boxStartValue.editingFinished.connect(
            self.boxStartValueEditerFinishedHandler)
        self.boxEndValue.editingFinished.connect(
            self.boxEndValueEditerFinishedHandler)
        self.boxStep.editingFinished.connect(self.boxStepCorrection)

    def resultHandler(self):
        if self.boxStartValue.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите начальное значение!")
            return
        if self.boxEndValue.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите конечное значение!")
            return
        if self.boxStep.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите шаг!")
            return
         
        iter = getBoxFloatValue(self.boxStartValue)
        border = getBoxFloatValue(self.boxEndValue)
        step = getBoxFloatValue(self.boxStep)
        
        if step == 0:
            if self.boxStartValue.text() == self.boxEndValue.text():
                self.table.setRowCount(1)
                self.table.setItem(0, 0, getTableItem(
                    getBoxFloatValue(self.boxStartValue)))
                self.table.setItem(0, 1, getTableItem(
                    computeFunction(getBoxFloatValue(self.boxStartValue))))
            return

        pairs = []
        while iter <= border:
            pairs.append((iter, computeFunction(iter)))
            iter += step

        self.table.setRowCount(len(pairs))
        for row, pair in enumerate(pairs):
            self.table.setItem(row, 0, getTableItem(pair[0]))
            self.table.setItem(row, 1, getTableItem(pair[1]))

    def clearHandler(self):
        self.boxStartValue.setValue(-10.0)
        self.boxEndValue.setValue(6.0)
        self.boxStep.setValue(1.0)
        self.table.setRowCount(0)

    def boxStartValueEditerFinishedHandler(self):
        if getBoxFloatValue(self.boxStartValue) > getBoxFloatValue(self.boxEndValue):
            self.boxStartValue.setValue(getBoxFloatValue(self.boxEndValue))
        self.boxStepCorrection()
        
    def boxEndValueEditerFinishedHandler(self):
        if getBoxFloatValue(self.boxEndValue) < getBoxFloatValue(self.boxStartValue):
            self.boxEndValue.setValue(getBoxFloatValue(self.boxStartValue))
        self.boxStepCorrection()

    def boxStepCorrection(self):
        maxstep = getBoxFloatValue(self.boxEndValue) - getBoxFloatValue(self.boxStartValue)
        if getBoxFloatValue(self.boxStep) > maxstep:
            self.boxStep.setValue(maxstep)

def getBoxFloatValue(box):
    return float(box.text().replace(',', '.'))

def computeFunction(X):
    if X >= -10 and X <= 0:
        return -0.5*X - 3
    elif X > 0 and X <= 3:
        return -sqrt(9 - X*X)
    elif X > 3 and X <= 6:
        return sqrt(-X*X + 12*X - 27)
    else:
        return None

def getTableItem(text):
        if type(text) == float:
            text = "{0:.2f}".format(text)
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(4)
        item.setFont(QFont('Times New Roman'))
        return item

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()