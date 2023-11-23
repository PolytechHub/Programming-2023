import sys
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt6.QtCore import QRegularExpression as QRegExp
from PyQt6.QtGui import QRegularExpressionValidator as QRegExpValidator
from functions import get_array, f1a, f1b, f2

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxF1a.setValidator(QRegExpValidator(
            QRegExp("^(-?\d+(\s-?\d+)*)$"), self.boxF1a))
        self.buttonF1aGen.clicked.connect(self.generateF1aHandler)
        self.buttonF1aEval.clicked.connect(self.resultF1aHandler)
        self.boxF1b.setValidator(QRegExpValidator(
            QRegExp("^(-?\d+(\s-?\d+)*)$"), self.boxF1b))
        self.buttonF1bGen.clicked.connect(self.generateF1bHandler)
        self.buttonF1bEval.clicked.connect(self.resultF1bHandler)
        self.boxF2.setValidator(QRegExpValidator(
            QRegExp("^(-?\d+(\s-?\d+)*)$"), self.boxF2))
        self.buttonF2Gen.clicked.connect(self.generateF2Handler)
        self.buttonF2Eval.clicked.connect(self.resultF2Handler)

    def generateF1aHandler(self):
        self.boxF1a.setText(' '.join(get_array(10, strings=True)))
    
    def generateF1bHandler(self):
        self.boxF1b.setText(' '.join(get_array(10, strings=True)))

    def generateF2Handler(self):
        self.boxF2.setText(' '.join(get_array(10, strings=True)))

    def resultF1aHandler(self):
        if self.boxF1a.text() == '':
            QMessageBox.about(self, 'Ошибка', "Первое поле не может быть пустым!")
            return
        result = f1a(boxRipper(self.boxF1a), self.boxF1aA.value())
        if result == -1:
            result = "Таких элементов не найдено"
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save f1a", "dataf1a.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write(str(result))

    def resultF1bHandler(self):
        if self.boxF1b.text() == '':
            QMessageBox.about(self, 'Ошибка', "Второе поле не может быть пустым!")
            return
        arr = boxRipper(self.boxF1b)
        self.boxF1bK2.setValue(min(self.boxF1bK2.value(), len(arr)))
        self.boxF1bK1.setValue(min(self.boxF1bK2.value(), self.boxF1bK1.value()))
        result = f1b(arr, self.boxF1bK1.value(), self.boxF1bK2.value())
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save f1b", "dataf1b.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write(str(result))

    def resultF2Handler(self):
        if self.boxF2.text() == '':
            QMessageBox.about(self, 'Ошибка', "Третье поле не может быть пустым!")
            return
        result = f2(boxRipper(self.boxF2))
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save f2", "dataf2.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write(str(result))

def boxRipper(box):
    if box.text() == '' or box.text() == '-inf':
        return []
    return list(map(int, box.text().split(' ')))

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()