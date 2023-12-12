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
    def __init__(self):
        # Window Init
        super().__init__()
        self.setupUi(self)

        # Add main tree
        self.tree = TreeWidget(self)
        self.setCentralWidget(self.tree)

        # Add tree controller
        self.treeController = TreeController(self.tree)

        # Add control menu button
        self.storeMenu = self.menuBar().addMenu('&Склад')

        # Add add element button
        self.addElementButton = QAction('Добавить новые элементы', self)
        self.storeMenu.addAction(self.addElementButton)
        self.addElementButton.triggered.connect(self.addItems)
        self.addElementButton.setShortcut('Ctrl+N')

        # Add delete element button
        self.deleteElementButton = QAction('Удалить выбранные элементы', self)
        self.storeMenu.addAction(self.deleteElementButton)
        self.deleteElementButton.triggered.connect(self.deleteSelectedItems)
        self.deleteElementButton.setShortcut('Ctrl+Backspace')

        # Add expand all elements button
        self.expandAllElementsButton = QAction('Раскрыть все элементы', self)
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
        if not path.exists(self.dataFolder):
            makedirs(self.dataFolder)
        self.treeController.saveTree(f'{self.dataFolder}/tree.pkl')
        super(MainWindow, self).closeEvent(event)

    def addItems(self):
        self.addElement = AddElement(self)
        self.addElement.show()

    def deleteSelectedItems(self):
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
        self.tree.expandAll()