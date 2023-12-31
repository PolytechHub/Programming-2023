import sys
import datetime
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from math import sin, cos

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonLoad.clicked.connect(self.loadHandler)

    def resultHandler(self):
        A = self.boxA.value()
        B = self.boxB.value()
        if A > B:
            A, B = B, A
        Y = self.boxY.value()
        Z = self.boxZ.value()
        step = self.boxStep.value()
        res = ''
        cnt = 0
        while A <= B:
            val = str(func(A, Y, Z))
            cnt += 1
            res += f"'{val}'."
            if cnt % 4 == 0:
                res += '\n'
            A += step
        filename, _ = QFileDialog.getSaveFileName(
                    self, "Save data", "data.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write("Тихомиров Роман Вячеславович, группа 231-365\n" + res)

    def loadHandler(self):
        filename, _ = QFileDialog.getOpenFileName(
                    self, "Load data", "", "Text (*.txt)")
        if filename:
            with open(filename) as f:
                QMessageBox.about(self, "Считанные данные", f.read())

def func(x, y, z):
    return abs(cos(x) - cos(y))**(1+2*sin(y)*sin(y)) * (1+z+((z**2)/2+(z**3)/3+(z**4)/4))

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()