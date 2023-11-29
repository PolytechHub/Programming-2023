#!/usr/bin/env python3

import sys
from datetime import timedelta
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import auto

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonGoToCity.clicked.connect(self.goToCity)
        self.buttonDistanceToPoint.clicked.connect(self.distanceToPoint)
        self.buttonCostOfTrip.clicked.connect(self.costOfTrip)
        self.buttonTimeOfTrip.clicked.connect(self.timeOfTrip)
        self.buttonPriceLoss.clicked.connect(self.priceLoss)

    def goToCity(self):
        auto = self.getAuto()
        if auto.go_to_city([self.boxGPSXGoToCity.value(), self.boxGPSYGoToCity.value()]):
            QMessageBox.about(self, "Проверка", "Вы доедете до города")
        else:
            QMessageBox.about(self, "Проверка", "У вас не хватит топлива")

    def distanceToPoint(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Проверка", 
                          f"До точки {auto.distance_to_point([self.boxGPSXDistanceToPoint.value(), self.boxGPSYDistanceToPoint.value()])} км")
        
    def costOfTrip(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Проверка", 
                            f"Цена поездки ${auto.cost_of_trip([self.boxGPSXCostOfTrip.value(), self.boxGPSYCostOfTrip.value()], self.boxFuelCostCostOfTrip.value())}")
    
    def timeOfTrip(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Проверка", 
                            f"Время поездки {auto.time_of_trip_with_max_speed([self.boxGPSXTimeOfTrip.value(), self.boxGPSYTimeOfTrip.value()])} ч")
        
    def priceLoss(self):
        auto = self.getAuto()
        QMessageBox.about(self, "Проверка", 
                            f"Автомобиль потерял ${auto.price_loss()}")

    def getAuto(self):
        return auto.Auto(color=self.boxColor.text(), 
                        brand=self.boxBrand.text(),
                        drive_type=self.boxDriveType.text(),
                        mileage=self.boxMileage.value(),
                        newcost=self.boxNewCost.value(),
                        cost=self.boxNowCost.value(),
                        gps=[self.boxGPSX.value(), self.boxGPSY.value()],
                        maxspeed=self.boxMaxSpeed.value(),
                        engine_type=self.boxEngineType.text(),
                        remaning_fuel=self.boxRemaningFuel.value(),
                        fuel_consumption=self.boxFuelConsumption.value(),
                        service_interval=timedelta(
                            days=int(self.boxServiceInterval.value())))

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()