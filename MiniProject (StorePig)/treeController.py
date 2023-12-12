from pickle import dump as pdump
from pickle import load as pload
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem

class TreeController():
    def __init__(self, tree: QTreeWidget):
        self.tree = tree

    def addItems(self, text, count, parent=None):
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
        container.append(item.text(0))
        
        childCount = item.childCount()
        if not childCount:
            return []
        
        for i in range(childCount):
            container.append([])
            TreeController.exploreItem(item.child(i), container[-1])

    def exploreTree(self):
        itemsCount = self.tree.topLevelItemCount()
        if not itemsCount:
            return dict()
        
        container = []
        for i in range(itemsCount):
            container.append([])
            TreeController.exploreItem(self.tree.topLevelItem(i), container[-1])

        return container
    
    def buildTree(self, container: list, parent=None):
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
        with open(path, 'wb') as f:
            pdump(self.exploreTree(), f)

    def loadTree(self, path='data/tree.pkl'):
        with open(path, 'rb') as f:
            self.buildTree(pload(f))