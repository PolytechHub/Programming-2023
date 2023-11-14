from math import sqrt
from random import randint
import sys
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableShotRes.setHorizontalHeaderLabels(['X', 'Y', 'Результат'])
        self.buttonStart.clicked.connect(self.startHandler)

    def startHandler(self):
        self.correctBoxes()
        rows = self.boxShot.value()
        self.tableShotRes.setRowCount(rows)
        r = self.boxRad.value()
        for row in range(rows):
            x, y = randint(-1000, 1000), randint(-1000, 1000)
            self.tableShotRes.setItem(row, 0, QTableWidgetItem(str(x)))
            self.tableShotRes.setItem(row, 1, QTableWidgetItem(str(y)))
            self.tableShotRes.setItem(row, 2, QTableWidgetItem(
                "Попадание" if checkShot(x, y, r) else "Промах"))

    def correctBoxes(self):
        if self.boxShot.text() == '':
            self.boxShot.setValue(1)
        if self.boxRad.text() == '':
            self.boxRad.setValue(1.)

def checkShot(x, y, r):
    if abs(x) > r or abs(y) > r:
        return False
    if (x < 0 and y > 0) or (x > 0 and y < 0):
        return abs(y) <= abs(r/(10*x))
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        return abs(y) <= sqrt(r*r - x*x)
    return True

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()