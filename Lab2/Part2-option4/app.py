import sys
import design
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QMainWindow, QApplication

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonResult.clicked.connect(self.resultHandler)

    def resultHandler(self):
        hours, minutes = map(int, self.boxTime.text().split(':'))
        self.boxTime.setTime(QTime(
            (12 - hours) % 12, (60 - minutes) % 60))

    
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()