import sys
from math import tan, cos, radians
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QMessageBox
from PyQt6.QtGui import QFont
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# Режим говнокода активирован

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.table.setHorizontalHeaderItem(0, getTableItem('Таблица значений функции'))
        self.table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeMode.Stretch)
        
        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonClear.clicked.connect(self.clearHandler)
        self.boxStartValue.editingFinished.connect(
            self.boxStartValueEditerFinishedHandler)
        self.boxEndValue.editingFinished.connect(
            self.boxEndValueEditerFinishedHandler)
        self.boxStep.editingFinished.connect(self.boxStepCorrection)

        fig = Figure()
        ax = fig.add_subplot()
        ax.plot([], [])

        canvas = FigureCanvas(fig)
        self.layoutPlot.addWidget(canvas)

        toolbar = NavigationToolbar(canvas, self)
        self.layoutToolbar.addWidget(toolbar)

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
        
        
        if self.table.columnCount() == 1:
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(['X', 'Y'])
            header = self.table.horizontalHeader()
            for i in range(2):
                header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
         
        iter = getBoxFloatValue(self.boxStartValue)
        border = getBoxFloatValue(self.boxEndValue)
        step = getBoxFloatValue(self.boxStep)
        A = getBoxFloatValue(self.boxA)
        
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
            pairs.append((iter, computeFunction(iter, A)))
            iter += step

        self.table.setRowCount(len(pairs))
        for row, pair in enumerate(pairs):
            self.table.setItem(row, 0, getTableItem(pair[0]))
            self.table.setItem(row, 1, getTableItem(pair[1]))

        x, y = zip(*pairs)
        
        for i in reversed(range(self.layoutPlot.count())): 
            self.layoutPlot.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.layoutToolbar.count())): 
            self.layoutToolbar.itemAt(i).widget().setParent(None)

        fig = Figure()
        ax = fig.add_subplot()
        ax.plot(x, y)

        canvas = FigureCanvas(fig)
        self.layoutPlot.addWidget(canvas)

        toolbar = NavigationToolbar(canvas, self)
        self.layoutToolbar.addWidget(toolbar)

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