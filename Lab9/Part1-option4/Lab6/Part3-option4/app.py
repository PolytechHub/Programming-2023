from math import sqrt
from random import randint
import sys
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QFileDialog
import pandas as pd

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonStart.clicked.connect(self.startHandler)

    def startHandler(self):
        self.correctBoxes()
        rows = self.boxShot.value()
        r = self.boxRad.value()
        threes = []
        for row in range(rows):
            x, y = randint(-1000, 1000), randint(-1000, 1000)
            threes.append([x, y, "Попадание" if checkShot(x, y, r) else "Промах"])
        dataframe = pd.DataFrame(threes, columns=['X', 'Y', 'Результат'])
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save result", "result.csv", "Table (*.csv)")
        if filename == '':
            return
        dataframe.to_csv(filename, sep='\t', encoding='utf-8', index=False)
        

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