import sys
from math import tan, cos, radians
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem,\
    QMessageBox, QFileDialog
from PyQt6.QtGui import QFont
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt

# Режим говнокода активирован

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
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
        if self.boxA.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, значение параметра A!")
            return
        
        if getBoxFloatValue(self.boxA) == 90 or getBoxFloatValue(self.boxA) == 270:
            QMessageBox.about(self, "Ошибка", 
                              "Тангенс не существует при таком параметре A!")
            return
        
         
        iter = getBoxFloatValue(self.boxStartValue)
        border = getBoxFloatValue(self.boxEndValue)
        step = getBoxFloatValue(self.boxStep)
        A = getBoxFloatValue(self.boxA)
        
        pairs = []

        if step == 0:
            if self.boxStartValue.text() == self.boxEndValue.text():
                pairs.append((getBoxFloatValue(self.boxStartValue), 
                    computeFunction(getBoxFloatValue(self.boxStartValue))))
        
        if len(pairs) == 0:
            while iter <= border:
                pairs.append((iter, computeFunction(iter, A)))
                iter += step

        dataframe = pd.DataFrame(pairs, columns=['X', 'Y'])
        filename, _ = QFileDialog.getSaveFileName(
                    self, "Save table", "table.csv", "Tables (*.csv)")
        if filename == '':
            return
        dataframe.to_csv(filename, sep='\t', encoding='utf-8', index=False)

        x, y = zip(*pairs)

        plt.plot(x, y)
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save plot", "plot.png", "Images (*.png)")
        plt.savefig(filename)


    def clearHandler(self):
        self.boxStartValue.setValue(-10.0)
        self.boxEndValue.setValue(6.0)
        self.boxStep.setValue(1.0)
        self.table.setRowCount(0)
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderItem(0, getTableItem('Таблица значений функции'))
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch)
        
        for i in reversed(range(self.layoutPlot.count())): 
            self.layoutPlot.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.layoutToolbar.count())): 
            self.layoutToolbar.itemAt(i).widget().setParent(None)

        fig = Figure()
        ax = fig.add_subplot()
        ax.plot([], [])

        canvas = FigureCanvas(fig)
        self.layoutPlot.addWidget(canvas)

        toolbar = NavigationToolbar(canvas, self)
        self.layoutToolbar.addWidget(toolbar)


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

def computeFunction(X, A):
    A = radians(A)
    return X*tan(A)-X**2/cos(A)**2

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