import sys
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt6.QtCore import QCoreApplication, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import design

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxNum1.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^[-+]?[0-9]+$"), self.boxNum1))
        self.boxNum2.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^[-+]?[0-9]+$"), self.boxNum2))
        self.boxNum3.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^[-+]?[0-9]+$"), self.boxNum3))
        self.buttonResult.clicked.connect(self.resultHandler)
        self.buttonClear.clicked.connect(self.clearHandler)
        self.buttonClose.clicked.connect(self.closeHandler)

    def resultHandler(self):
        if self.boxNum1.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите число №1!")
            return
        if self.boxNum2.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите число №2!")
            return
        if self.boxNum3.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите число №3!")
            return
        
        nums = [int(self.boxNum1.text()),
                int(self.boxNum2.text()), 
                int(self.boxNum3.text())]
        nums.sort()

        self.boxResult.setText(str(nums[1]))

    def clearHandler(self):
        self.boxNum1.clear()
        self.boxNum2.clear()
        self.boxNum3.clear()
        self.boxResult.clear()

    def closeHandler(self):
        QCoreApplication.quit()

    
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()