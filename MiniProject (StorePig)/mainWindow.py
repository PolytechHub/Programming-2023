from os import path, makedirs
from pathlib import Path
from platform import system
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QAction
from mainWindowUI import Ui_Form
from treeWidget import TreeWidget
from treeController import TreeController
from addElement import AddElement

class MainWindow(Ui_Form, QMainWindow):
    """Класс реализует главное окно StorePig."""
    def __init__(self):
        """Конструктор класса MainWindow."""
        # Window Init
        super().__init__()
        self.setupUi(self)

        # Add main tree
        self.tree = TreeWidget(self)
        """Объект главного дерева склада."""
        self.setCentralWidget(self.tree)

        # Add tree controller
        self.treeController = TreeController(self.tree)
        """Объект контроллера главного дерева склада."""

        # Add control menu button
        self.storeMenu = self.menuBar().addMenu('&Склад')
        """Объект пользовательского меню."""

        # Add add element button
        self.addElementButton = QAction('Добавить новые элементы', self)
        """Объект кнопки «Добавить новые элементы»."""
        self.storeMenu.addAction(self.addElementButton)
        self.addElementButton.triggered.connect(self.addItems)
        self.addElementButton.setShortcut('Ctrl+N')

        # Add delete element button
        self.deleteElementButton = QAction('Удалить выбранные элементы', self)
        """Объект кнопки Удалить выбранные элементы»."""
        self.storeMenu.addAction(self.deleteElementButton)
        self.deleteElementButton.triggered.connect(self.deleteSelectedItems)
        self.deleteElementButton.setShortcut('Ctrl+Backspace')

        # Add expand all elements button
        self.expandAllElementsButton = QAction('Раскрыть все элементы', self)
        """Объект кнопки «Раскрыть все элементы»."""
        self.storeMenu.addAction(self.expandAllElementsButton)
        self.expandAllElementsButton.triggered.connect(self.expandAllItems)
        self.expandAllElementsButton.setShortcut('Ctrl+J')

        # Configuring Data Storage
        if system() == 'Darwin':
            self.dataFolder =\
                f'{Path.home()}/Library/Mobile Documents/com~apple~CloudDocs/StorePig'
        else:
            self.dataFolder = 'StorePigData'

        # Load main tree
        if path.exists(f'{self.dataFolder}/tree.pkl'):
            self.treeController.loadTree(f'{self.dataFolder}/tree.pkl')
    
    def closeEvent(self, event):
        """Обработчик события закрытия окна, вызывающий сохранение данных склада."""
        if not path.exists(self.dataFolder):
            makedirs(self.dataFolder)
        self.treeController.saveTree(f'{self.dataFolder}/tree.pkl')
        super(MainWindow, self).closeEvent(event)

    def addItems(self):
        """Функция вызова окна добавления нового элемента."""
        self.addElement = AddElement(self)
        self.addElement.show()

    def deleteSelectedItems(self):
        """Функция, удаляющая выделенные элементы."""
        selectedItems = self.tree.selectedItems()
        if not selectedItems:
            return

        # Show accept dialog
        messageBox = QMessageBox(self)
        messageBox.setText("Удалить выбранные элементы?")
        messageBox.addButton("Отмена", QMessageBox.ButtonRole.RejectRole)
        messageBox.addButton("OK", QMessageBox.ButtonRole.AcceptRole)
        ok = messageBox.exec()
        
        # Delete selected items
        if ok:
            root = self.tree.invisibleRootItem()
            for item in selectedItems:
                (item.parent() or root).removeChild(item)

    def expandAllItems(self):
        """Функция, раскрывающая все элементы."""
        self.tree.expandAll()