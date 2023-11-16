import sys
import datetime
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QSpinBox, QLineEdit, QDoubleSpinBox

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableInitialData.setHorizontalHeaderLabels(["Категория товара", 
                                                         "Наименование товара",
                                                         "Кол-во", "Цена р."])
        self.tableInitialData.resizeColumnsToContents()
        self.tableReport.setHorizontalHeaderLabels(["Наименование товара",
                                                    "Цена", "Кол-во", "Сумма скидки"])
        self.tableReport.resizeColumnsToContents()
        self.boxStringsTotal.editingFinished.connect(self.boxEditedFinished)
        self.buttonResult.clicked.connect(self.result)
        self.labelDate.setText(str(datetime.datetime.today().date()))

    def boxEditedFinished(self):
        n = self.boxStringsTotal.value()
        self.tableInitialData.setRowCount(n)
        if n > 0:
            for i in range(n):
                if self.tableInitialData.cellWidget(i, 0) == None:
                    cat = QSpinBox()
                    cat.setMaximum(10000)
                    self.tableInitialData.setCellWidget(i, 0, cat)
                    name = QLineEdit()
                    self.tableInitialData.setCellWidget(i, 1, name)
                    count = QSpinBox()
                    count.setMaximum(10000)
                    self.tableInitialData.setCellWidget(i, 2, count)
                    cost = QDoubleSpinBox()
                    cost.setMaximum(10000)
                    self.tableInitialData.setCellWidget(i, 3, cost)

    def result(self):
        k, p = self.boxK.value(), self.boxP.value()
        values = cals(k, p, self.getInitialTableValues())
        self.tableReport.setRowCount(0)
        self.tableReport.setRowCount(len(values))
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
            discount.setText(str(val['discount']))
            self.tableReport.setCellWidget(i, 3, discount)
    
    def getInitialTableValues(self):
        n = self.boxStringsTotal.value()
        values = []
        for i in range(n):
            m = dict()
            if self.tableInitialData.cellWidget(i, 0) != None:
                m['cat'] = self.tableInitialData.cellWidget(i, 0).value()
            else:
                continue
            if self.tableInitialData.cellWidget(i, 1) != None and\
                self.tableInitialData.cellWidget(i, 1).text() != '':
                m['name'] = self.tableInitialData.cellWidget(i, 1).text()
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


def cals(k, p, items):
    res = []
    for i in items:
        if i['count'] < k:
            continue
        discount = i['cost'] / 100 * p
        i['discount'] = discount * i['count']
        res.append(i)
    return res

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()