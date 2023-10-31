import sys
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt6.QtCore import QCoreApplication, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from math import sin, cos, radians
import design

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxHypotenuse.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^\\d*(\\,\\d+)?$"), self.boxHypotenuse))
        self.boxHypotenuse.returnPressed.connect(self.resultHandler)
        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonClear.clicked.connect(self.clearHandler)
        self.buttonClose.clicked.connect(self.closeHandler)

    def resultHandler(self):
        if self.boxAngle.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите значение угла!")
            return
        if self.boxHypotenuse.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите значение гипотенузы!")
            return
        
        a = radians(float(self.boxAngle.text().replace(',', '.')))
        c = float(self.boxHypotenuse.text().replace(',', '.'))
        self.boxArea.setText(str(c*c*sin(a)*cos(a)/2))
        self.boxPerimeter.setText(str(c*sin(a) + c*cos(a) + c))

    def clearHandler(self):
        self.boxAngle.setValue(30.00)
        self.boxHypotenuse.clear()
        self.boxArea.clear()
        self.boxPerimeter.clear()

    def closeHandler(self):
        QCoreApplication.quit()

    
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()