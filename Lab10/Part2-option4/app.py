import sys
import design
import vector
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateVectors()
        self.boxX1.editingFinished.connect(self.updateVectors)
        self.boxX2.editingFinished.connect(self.updateVectors)
        self.boxY1.editingFinished.connect(self.updateVectors)
        self.boxY2.editingFinished.connect(self.updateVectors)
        self.buttonXAngle1.clicked.connect(self.displayOXAngle1)
        self.buttonXAngle2.clicked.connect(self.displayOXAngle2)
        self.buttonYAngle1.clicked.connect(self.displayOYAngle1)
        self.buttonYAngle2.clicked.connect(self.displayOYAngle2)
        self.buttonScalarProduct.clicked.connect(self.displayScalarProduct)
        self.buttonVectorProduct.clicked.connect(self.displayVectorProduct)
    
    def updateVectors(self):
        self.vector1 = vector.Vector(self.boxX1.value(), self.boxY1.value())
        self.vector2 = vector.Vector(self.boxX2.value(), self.boxY2.value())
        self.boxAngle.setText(str(self.vector1.get_angle_between(self.vector2)))

    def displayOXAngle1(self):
        QMessageBox.about(self, "", str(f"Угол вектора №1 к оси Ox = {round(self.vector1.get_x_angle(), 2)}°"))

    def displayOXAngle2(self):
        QMessageBox.about(self, "", str(f"Угол вектора №2 к оси Ox = {round(self.vector2.get_x_angle(), 2)}°"))

    def displayOYAngle1(self):
        QMessageBox.about(self, "", str(f"Угол вектора №1 к оси Oy = {round(self.vector1.get_y_angle(), 2)}°"))

    def displayOYAngle2(self):
        QMessageBox.about(self, "", str(f"Угол вектора №2 к оси Oy = {round(self.vector2.get_y_angle(), 2)}°"))

    def displayScalarProduct(self):
        QMessageBox.about(self, "", str(f"Скалярное произведение векторов = {round(self.vector1.get_scalar_product(self.vector1), 2)}"))

    def displayVectorProduct(self):
        QMessageBox.about(self, "", str(f"Векторное произведение векторов = {round(self.vector1.get_vector_product(self.vector1), 2)}"))

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()