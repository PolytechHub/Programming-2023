import sys
from math import inf
import design
from PyQt6.QtWidgets import QMainWindow, QApplication,\
    QHeaderView, QMessageBox, QDoubleSpinBox, QLineEdit
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import PyQt6 as Qt


class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.boxTask1.setValidator(QRegularExpressionValidator(
            QRegularExpression("^[013]+$"), self.boxTask1))
        
        self.boxTask1.textEdited.connect(self.updateHandlerTask1)
        self.buttonSort1.clicked.connect(self.sortTask1)

        self.table2.setHorizontalHeaderLabels(['Мощность', 'Стоимость', 'Соотношение'])
        header = self.table2.horizontalHeader()
        for i in range(3):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

        self.boxN2.editingFinished.connect(self.editFinalNTask2)
        self.buttonResult2.clicked.connect(self.resultHandlerTask2)
        
    def updateHandlerTask1(self):
        seq = self.boxTask1.text()

        entry3 = seq.find('3') if seq.count('3') > 0 else inf
        entry0 = seq.find('0') if seq.count('0') > 0 else inf

        if entry3 < entry0:
            self.boxResult1.setText('Первым был выигрыш (3 очка)')
            self.boxResult1.setStyleSheet('color: green')
        elif entry0 < entry3:
            self.boxResult1.setText('Первым был проигрыш (0 очков)')
            self.boxResult1.setStyleSheet('color: red')
        else:
            self.boxResult1.setText('Не было ни выигрышей, ни проигрышей... Нас обманули!')
            self.boxResult1.setStyleSheet('color: black')

    def sortTask1(self):
        self.boxTask1.setText(ArmashSort(self.boxTask1.text()))

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
        
        C = getBoxFloatValue(self.boxC2)
        rows = int(self.boxN2.text())
        for i in range(rows):
            power = getBoxFloatValue(self.table2.cellWidget(i, 0))
            cost = getBoxFloatValue(self.table2.cellWidget(i, 1))
            lineEdit = QLineEdit(self.table2)
            lineEdit.setText(str(power / cost))
            lineEdit.setReadOnly(True)
            self.table2.setCellWidget(i, 2, lineEdit)

            if power <= C:
                spinbox = self.table2.cellWidget(i, 0)
                spinbox.setStyleSheet('background-color: lightgreen;')
                self.table2.setCellWidget(i, 0, spinbox)
            else:
                spinbox = self.table2.cellWidget(i, 0)
                spinbox.setStyleSheet('background-color: white;')
                self.table2.setCellWidget(i, 0, spinbox)


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