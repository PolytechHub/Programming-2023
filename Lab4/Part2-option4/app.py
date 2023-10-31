import sys
from random import random, randint
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt6.QtGui import QFont

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonRandom.clicked.connect(self.randomHandler)
        self.boxA.valueChanged.connect(self.boxChangedHandler)
        self.boxB.valueChanged.connect(self.boxChangedHandler)
        self.boxC.valueChanged.connect(self.boxChangedHandler)
        self.boxD.valueChanged.connect(self.boxChangedHandler)

    def resultHandler(self):
        if self.boxA.text() == '' or\
            self.boxB.text() == '' or\
                self.boxC.text() == '' or\
                    self.boxD.text() == '':
            
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите все значения!")
            return

        columns = abs(getBoxIntValue(self.boxA) - getBoxIntValue(self.boxB)) + 1
        rows = int(100*abs(getBoxFloatValue(self.boxC) - getBoxFloatValue(self.boxD))) + 1

        startColumn = min(getBoxIntValue(self.boxA), getBoxIntValue(self.boxB))
        endColumn = max(getBoxIntValue(self.boxA), getBoxIntValue(self.boxB))

        self.table.setColumnCount(columns)
        self.table.setHorizontalHeaderLabels(map(str, range(startColumn, endColumn+1)))

        startRow = min(getBoxFloatValue(self.boxC), getBoxFloatValue(self.boxD))
        endRow = max(getBoxFloatValue(self.boxC), getBoxFloatValue(self.boxD))

        self.table.setRowCount(rows)
        self.table.setVerticalHeaderLabels([str(i / 100) 
                                            for i in range(
                                                int(100*startRow), int(100*endRow+1))])
        
        iter = startColumn + startRow
        
        for row in range(rows):
            iter = iter % 1 + startColumn
            for column in range(columns):
                self.table.setItem(row, column, getTableItem(antilLog10(iter)))
                iter += 1
            iter += 0.01
    
    def randomHandler(self):
        self.boxA.setValue(randint(-100, 100))
        self.boxB.setValue(randint(-100, 100))
        self.boxC.setValue(random())
        self.boxD.setValue(random())

    def boxChangedHandler(self):
        # Лень писать систему связи, как в части 1
        # Костыль, но требования удовлетворяет
        if getBoxIntValue(self.boxA) > getBoxIntValue(self.boxB):
            self.labelA.setText('Значение B')
            self.labelB.setText('Значение A')
        elif getBoxIntValue(self.boxA) < getBoxIntValue(self.boxB):
            self.labelA.setText('Значение A')
            self.labelB.setText('Значение B')

        if getBoxFloatValue(self.boxC) > getBoxFloatValue(self.boxD):
            self.labelC.setText('Значение D')
            self.labelD.setText('Значение C')
        elif getBoxFloatValue(self.boxC) < getBoxFloatValue(self.boxD):
            self.labelC.setText('Значение C')
            self.labelD.setText('Значение D')

def getBoxFloatValue(box):
    return float(box.text().replace(',', '.'))

def getBoxIntValue(box):
    return int(box.text().replace(',', '.'))

def getTableItem(text):
        if type(text) == float:
            text = "{0:.5f}".format(text)
        item = QTableWidgetItem(str(text))
        item.setTextAlignment(4)
        item.setFont(QFont('Times New Roman'))
        return item

def antilLog10(x):
    return 10**x

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()