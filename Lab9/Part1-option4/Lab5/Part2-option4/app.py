import sys
from math import inf
import design
from PyQt6.QtWidgets import QMainWindow, QApplication,\
    QMessageBox, QDoubleSpinBox, QLineEdit, QFileDialog
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import PyQt6 as Qt


class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.boxTask1.setValidator(QRegularExpressionValidator(
            QRegularExpression("^[013]+$"), self.boxTask1))
        
        self.buttonResult1.clicked.connect(self.result1)

        self.table2.setHorizontalHeaderLabels(['Мощность', 'Стоимость'])

        self.boxN2.editingFinished.connect(self.editFinalNTask2)
        self.buttonResult2.clicked.connect(self.resultHandlerTask2)
        
    def result1(self):
        seq = self.boxTask1.text()

        entry3 = seq.find('3') if seq.count('3') > 0 else inf
        entry0 = seq.find('0') if seq.count('0') > 0 else inf

        result = ""

        if entry3 < entry0:
            result = 'Первым был выигрыш (3 очка)'
        elif entry0 < entry3:
            result = 'Первым был проигрыш (0 очков)'
        else:
            result = 'Не было ни выигрышей, ни проигрышей... Нас обманули!'
        
        filename, _ = QFileDialog.getSaveFileName(
                self, "Save first data", "data.txt", "Text (*.txt)")
        if filename == '':
            return
        
        with open(filename, 'w') as f:
            f.write(result + "\nСортировка: " + ArmashSort(self.boxTask1.text()))

########################################################################################

    def editFinalNTask2(self):
        rows = int(self.boxN2.text())
        self.table2.setRowCount(rows)

        for i in range(rows):
            for j in range(2):
                if self.table2.cellWidget(i, j) == None:
                    spinBox = QDoubleSpinBox(self.table2)
                    spinBox.setMinimum(0.01)
                    spinBox.setMaximum(1000.00)
                    spinBox.setDecimals(2)
                    spinBox.setValue(10)
                    self.table2.setCellWidget(i, j, spinBox)
            if self.table2.cellWidget(i, 2) == None:
                lineEdit = QLineEdit(self.table2)
                lineEdit.setReadOnly(True)
                self.table2.setCellWidget(i, 2, lineEdit)

    def resultHandlerTask2(self):
        if self.boxC2.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите значение C!")
            return
        if self.boxN2.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите значение N!")
            return
        
        if self.table2.rowCount() == 0:
            self.editFinalNTask2()
        
        C = getBoxFloatValue(self.boxC2)
        rows = int(self.boxN2.text())
        lowerC = []
        ratio = []
        for i in range(rows):
            power = getBoxFloatValue(self.table2.cellWidget(i, 0))
            cost = getBoxFloatValue(self.table2.cellWidget(i, 1))
            if power <= C:
                lowerC.append(cost)
            ratio.append(power / cost)
        
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save data", "data.txt", "Text (*.txt)")
        if filename == '':
            return
        with open(filename, 'w') as f:
            f.write("Lower C: " + ' '.join(map(str, lowerC)) 
                    +"\nRatio: " + ' '.join(map(str, ratio)))

def ArmashSort(arrStr):
    # техника древних джедаев, работает за O(n), но только с числами 0, 1 и 3
    return '3'*arrStr.count('3') + '1'*arrStr.count('1') + '0'*arrStr.count('0')

def getBoxFloatValue(box):
    return float(box.text().replace(',', '.'))

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()