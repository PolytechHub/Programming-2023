import sys
from math import sqrt
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt6.QtGui import QFont
import pandas as pd

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        
        self.buttonResult.clicked.connect(self.resultHandler)
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
                dataframe =\
                pd.DataFrame([[getBoxFloatValue(self.boxStartValue),
                                computeFunction(getBoxFloatValue(self.boxStartValue))]],
                                columns=['X', 'Y'])
                filename, _ = QFileDialog.getSaveFileName(
                    self, "Save table", "table.csv", "Tables (*.csv)")
                if filename == '':
                    return
                dataframe.to_csv(filename, sep='\t', encoding='utf-8', index=False)
            return

        pairs = []
        while iter <= border:
            pairs.append((iter, computeFunction(iter)))
            iter += step
        dataframe = pd.DataFrame(pairs, columns=['X', 'Y'])
        filename, _ = QFileDialog.getSaveFileName(
                    self, "Save table", "table.csv", "Tables (*.csv)")
        if filename == '':
            return
        dataframe.to_csv(filename, sep='\t', encoding='utf-8', index=False)

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

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()