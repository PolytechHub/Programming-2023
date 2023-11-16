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
        self.boxF2k.editingFinished.connect(self.boxF2kFinished)
        
    def boxF2kFinished(self):
        self.boxF2k.setValue(min(len(boxRipper(self.boxF2)) - 1, self.boxF2k.value()))

    def generateF1aHandler(self):
        self.boxF1a.setText(' '.join(get_array(10, strings=True)))
    
    def generateF1bHandler(self):
        self.boxF1b.setText(' '.join(get_array(10, strings=True)))

    def generateF2Handler(self):
        self.boxF2.setText(' '.join(get_array(7, strings=True)))

    def resultF1aHandler(self):
        if self.boxF1a.text() == '':
            QMessageBox.about(self, 'Ошибка', "Первое поле не может быть пустым!")
            return
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save f1a", "dataf1a.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write(' '.join(map(str, f1a(boxRipper(self.boxF1a)))))

    def resultF1bHandler(self):
        if self.boxF1b.text() == '':
            QMessageBox.about(self, 'Ошибка', "Второе поле не может быть пустым!")
            return
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save f1b", "dataf1b.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write(' '.join(map(str, f1b(boxRipper(self.boxF1b)))))

    def resultF2Handler(self):
        if self.boxF2.text() == '':
            QMessageBox.about(self, 'Ошибка', "Третье поле не может быть пустым!")
            return
        self.boxF2kFinished()
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save f2", "dataf2.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write(str(f2(
                boxRipper(self.boxF2), self.boxF2k.value(), self.boxF2C.value())))

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