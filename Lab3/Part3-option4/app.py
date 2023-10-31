import sys
from math import sqrt
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QPixmap
from graphbuilder import buildGraph
import design

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxR.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^\\d*(\\,\\d+)?$"), self.boxR))
        self.boxX.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^-?\\d*(\\,\\d+)?$"), self.boxX))
        self.boxY.setValidator(
            QRegularExpressionValidator(
                QRegularExpression("^-?\\d*(\\,\\d+)?$"), self.boxY))
        self.buttonCompute.clicked.connect(self.computeHandler)
        self.boxR.returnPressed.connect(self.computeHandler)
        self.boxX.returnPressed.connect(self.computeHandler)
        self.boxY.returnPressed.connect(self.computeHandler)

        R, X, Y = 10, 5, 5
        self.boxR.setText(str(R))
        self.boxX.setText(str(X))
        self.boxY.setText(str(Y))
        buildGraph(r=R, pointX=X, pointY=Y, filename='plot.png')
        self.labelGraph.setPixmap(QPixmap('plot.png'))
        self.boxResult.setText('внутри графика')
        self.boxResult.setStyleSheet('color: green')

    def computeHandler(self):
        if self.boxR.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите число R!")
            return
        if self.boxX.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите X точки!")
            return
        if self.boxY.text() == '':
            QMessageBox.about(self, "Ошибка", "Пожалуйста, введите Y точки!")
            return
        
        R = float(self.boxR.text().replace(',', '.'))
        X = float(self.boxX.text().replace(',', '.'))
        Y = float(self.boxY.text().replace(',', '.'))

        if abs(R) < 100000 and abs(X) < 100000 and abs(Y) < 100000:
            buildGraph(r=R, pointX=X, pointY=Y, filename='plot.png')
            self.labelGraph.setPixmap(QPixmap('plot.png'))
        else: 
            self.labelGraph.setPixmap(QPixmap('defaultplot.png'))
        
        result = True
        if Y == 0:
            if abs(X) > R:
                result = False
        elif Y > 0:
            if abs(X) > R:
                result = False
            elif Y > sqrt(R**2 - X**2):
                result = False
        elif Y < 0:
            if X > 0:
                result = False
            elif Y < -R:
                result = False
            elif X < Y:
                result = False

        if result:
            self.boxResult.setText('внутри графика')
            self.boxResult.setStyleSheet('color: green')
        else:
            self.boxResult.setText('вне графика')
            self.boxResult.setStyleSheet('color: red')      
    
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()