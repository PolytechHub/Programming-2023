import sys
import design
from functions import calsDevs, f1
from PyQt6.QtWidgets import QMainWindow, QApplication, QSpinBox, QLineEdit
from random import randint

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxN.editingFinished.connect(self.boxFinishEdited)
        self.buttonResult.clicked.connect(self.result)
    
    def boxFinishEdited(self):
        n = self.boxN.value()
        self.table.setRowCount(n)
        self.table.setColumnCount(n + 1 if n != 0 else n)
        if n > 0:
            self.table.setHorizontalHeaderLabels(
                list(map(str, range(1, n + 1))) + ["Prod"])
            for i in range(n):
                for j in range(n):
                    if self.table.cellWidget(i, j) == None or self.table.cellWidget(i, j).isReadOnly():
                        spinbox = QSpinBox()
                        spinbox.setMinimum(-100)
                        spinbox.setMaximum(100)
                        spinbox.setValue(randint(-100, 100))
                        self.table.setCellWidget(i, j, spinbox)
            for i in range(n):
                if self.table.cellWidget(i, n) == None or not(self.table.cellWidget(i, j).isReadOnly()):
                    box = QLineEdit()
                    box.setReadOnly(True)
                    self.table.setCellWidget(i, n, box)

    def result(self):
        self.boxFinishEdited()
        n = self.boxN.value()
        if n > 0:
            matrix = []
            if self.boxC.text() == '':
                self.boxC.setValue(1)
            C = self.boxC.value()
            for i in range(n):
                matrix.append([])
                for j in range(n):
                    matrix[-1].append(self.table.cellWidget(i, j).value())
                    if calsDevs(self.table.cellWidget(i, j).value()) > C:
                        self.table.cellWidget(i, j).setStyleSheet('background-color: lightgreen;')
                    else:
                        self.table.cellWidget(i, j).setStyleSheet('background-color: white;')
            labels = f1(matrix)
            for i in range(n):
                self.table.cellWidget(i, n).setText(str(labels[i]))

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()