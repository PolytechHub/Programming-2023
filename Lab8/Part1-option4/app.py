import sys
import design
from function import change_register
from PyQt6.QtWidgets import QMainWindow, QApplication, QSpinBox, QLineEdit

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.box.editingFinished.connect(self.convert)

    def convert(self):
        self.box.setText(change_register(self.box.text()))

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()