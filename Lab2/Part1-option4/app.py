import sys
from PyQt6.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from math import cos, sin, tan
import design

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxA.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^-?\\d*(\\,\\d+)?$"), self.boxA))
        self.boxA.returnPressed.connect(self.resultHandler)
        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonClear.clicked.connect(self.clearHandler)
        self.buttonClose.clicked.connect(self.closeHandler)

    def resultHandler(self):
        if self.boxA.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите значение A!")
            return
        a = float(self.boxA.text().replace(',', '.'))
        depth = self.boxAccuracy.value()
        res1 = (2*cos(a)*sin(2*a) - sin(a)) / (cos(a) - 2*sin(a)*sin(2*a))
        res2 = tan(3*a)
        QMessageBox.about(self, "Result", ("Z1: " + ("{0:." + str(depth) +"f}").format(res1))+"\n"+("Z2: " +("{0:." + str(depth) +"f}").format(res2)))

    def clearHandler(self):
        self.boxA.clear()
        self.boxAccuracy.setValue(2)

    def closeHandler(self):
        QCoreApplication.quit()

    
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()