from pickle import dump as pdump
from pickle import load as pload
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem

class TreeController():
    """Класс реализует набор методов для управления главным деревом склада."""
    def __init__(self, tree: QTreeWidget):
        """Конструктор класса TreeController, принимающий ссылку на главное дерево склада."""
        self.tree = tree
        """Ссылка на главное дерево склада."""

    def addItems(self, text, count, parent=None):
        """Функция добавления нового элемента в дерево. Принимает текст элемента, его количество, и родительский элемент (опционально)."""
        if not parent:
            items = [QTreeWidgetItem([text]) for _ in range(count)]
            self.tree.addTopLevelItems(items)
            for item in items:
                item.setSelected(True)
        else: 
            items = [QTreeWidgetItem(parent, [text]) for _ in range(count)]
            self.tree.addTopLevelItems(items)
            parent.setExpanded(True)
            parent.setSelected(True)

    @staticmethod
    def exploreItem(item: QTreeWidgetItem, container: list):
        """Рекурсивная функция обхода дерева. Принимает элемент, обход которого будет производиться, и ссылку на контейнер для результатов обхода (пустой list)."""
        container.append(item.text(0))
        
        childCount = item.childCount()
        if not childCount:
            return []
        
        for i in range(childCount):
            container.append([])
            TreeController.exploreItem(item.child(i), container[-1])

    def exploreTree(self):
        """Функция обхода главного дерева склада. Возвращает контейнер (list) с результатами обхода."""
        itemsCount = self.tree.topLevelItemCount()
        if not itemsCount:
            return dict()
        
        container = []
        for i in range(itemsCount):
            container.append([])
            TreeController.exploreItem(self.tree.topLevelItem(i), container[-1])

        return container
    
    def buildTree(self, container: list, parent=None):
        """Рекурсивная функция построения главного дерева склада из контейнера. Принимает контейнер. Аргумент «parent» служебный."""
        if not parent:
            self.tree.clear()
            for item in container:
                treeItem = QTreeWidgetItem([item[0]])
                self.tree.addTopLevelItem(treeItem)
                for child in item[1:]:
                    self.buildTree(child, treeItem)
        else:
            treeItem = QTreeWidgetItem(parent, [container[0]])
            self.tree.addTopLevelItem(treeItem)
            for child in container[1:]:
                self.buildTree(child, treeItem)
        self.tree.setCurrentItem(self.tree.headerItem())

    def saveTree(self, path='data/tree.pkl'):
        """Функция сохранения главного дерева склада в файл. Принимает путь к файлу сохранения."""
        with open(path, 'wb') as f:
            pdump(self.exploreTree(), f)

    def loadTree(self, path='data/tree.pkl'):
        """Функция загрузки главного дерева склада из файла. Принимает путь к файлу загрузки."""
        with open(path, 'rb') as f:
            self.buildTree(pload(f))