from PyQt6.QtWidgets import QTreeWidget, QAbstractItemView
from PyQt6.QtGui import QShortcut

class TreeWidget(QTreeWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setTabKeyNavigation(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setObjectName('tree')
        self.setHeaderLabel("Ваш домашний склад")
        self.setCurrentItem(self.headerItem())
        QShortcut('Escape', self).activated.connect(self.clearSelection)

    def clearSelection(self):
        super().clearSelection()
        self.setCurrentItem(self.headerItem())

    def mousePressEvent(self, event):
        if self.itemAt(event.pos()) is None:
            self.clearSelection()
        QTreeWidget.mousePressEvent(self, event)