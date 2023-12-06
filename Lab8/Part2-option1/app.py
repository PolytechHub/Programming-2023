import sys
import datetime
import design
from random import randint
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMainWindow, QApplication, QDateEdit, QSpinBox,\
    QLineEdit, QDoubleSpinBox

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableInitialData.setHorizontalHeaderLabels(["Наименование товара", 
                                                         "Дата годности",
                                                         "Количество товара", 
                                                         "Цена в рублях"
                                                        ])
        self.tableInitialData.resizeColumnsToContents()
        self.tableReport.setHorizontalHeaderLabels(["Наименование товара",
                                                    "Цена в рублях с учётом скидки",
                                                    "Количество товара",
                                                    "Сумма рублях"
                                                    ])
        self.tableReport.resizeColumnsToContents()
        self.boxStringsTotal.editingFinished.connect(self.boxEditedFinished)
        self.buttonResult.clicked.connect(self.result)
        self.labelDate.setText(f'«{datetime.datetime.today().date().strftime("%d.%m.%Y")}»')

    def boxEditedFinished(self):
        n = self.boxStringsTotal.value()
        self.tableInitialData.setRowCount(n)
        if n > 0:
            for i in range(n):
                if self.tableInitialData.cellWidget(i, 0) == None:
                    name = QLineEdit()
                    name.setText(f"Item №{i + 1}")
                    self.tableInitialData.setCellWidget(i, 0, name)
                    date = QDateEdit()
                    date.setDate(QDate(
                        randint(1950, 2100),
                        randint(1, 12),
                        randint(1, 28)))
                    self.tableInitialData.setCellWidget(i, 1, date)
                    count = QSpinBox()
                    count.setMaximum(10000)
                    count.setValue(randint(1, 10000))
                    self.tableInitialData.setCellWidget(i, 2, count)
                    cost = QDoubleSpinBox()
                    cost.setMaximum(10000)
                    cost.setValue(randint(1, 10000))
                    self.tableInitialData.setCellWidget(i, 3, cost)

    def result(self):
        border = self.borderBox.date()
        ratio = self.ratioBox.value()
        threshhold = self.treshBox.value()
        values = sieve(self.getInitialTableValues(), border, ratio, threshhold)
        self.tableReport.setRowCount(0)
        self.tableReport.setRowCount(len(values))
        totalSum = 0
        for i, val in enumerate(values):
            name = QLineEdit()
            name.setReadOnly(True)
            name.setText(val['name'])
            self.tableReport.setCellWidget(i, 0, name)
            cost = QLineEdit()
            cost.setReadOnly(True)
            cost.setText(str(val['cost']))
            self.tableReport.setCellWidget(i, 1, cost)
            count = QLineEdit()
            count.setReadOnly(True)
            count.setText(str(val['count']))
            self.tableReport.setCellWidget(i, 2, count)
            discount = QLineEdit()
            discount.setReadOnly(True)
            discount.setText(str(val['sum']))
            self.tableReport.setCellWidget(i, 3, discount)
            totalSum += val['sum']
        self.boxTotalSum.setText(str(totalSum))
    
    def getInitialTableValues(self):
        n = self.boxStringsTotal.value()
        values = []
        for i in range(n):
            m = dict()
            if self.tableInitialData.cellWidget(i, 0) != None:
                m['name'] = self.tableInitialData.cellWidget(i, 0).text()
            else:
                continue
            if self.tableInitialData.cellWidget(i, 1) != None and\
                self.tableInitialData.cellWidget(i, 1).text() != '':
                m['date'] = self.tableInitialData.cellWidget(i, 1).date()
            else:
                continue
            if self.tableInitialData.cellWidget(i, 2) != None:
                m['count'] = self.tableInitialData.cellWidget(i, 2).value()
            else:
                continue
            if self.tableInitialData.cellWidget(i, 3) != None:
                m['cost'] = self.tableInitialData.cellWidget(i, 3).value()
            else:
                continue
            values.append(m)
        return values


def sieve(items, border, ratio, threshhold):
    res = []
    for val in items:
        if val['date'] < border:
            if val['count'] >= threshhold:
                val['cost'] *= round(1 - ratio / 100, 2)
            val['sum'] = round(val['cost'] * val['count'], 2)
            res.append(val)
    return res

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()