#!/usr/bin/env python3

"""Главный файл, запускающий все остальные модули."""
import sys
from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow


def main():
    """Функция создает объект приложения и главного окна, после чего производит их запуск."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()