from PyQt6.QtWidgets import QTreeWidget, QAbstractItemView
from PyQt6.QtGui import QShortcut

class TreeWidget(QTreeWidget):
    """Класс реализует улучшенный QTreeWidget, позволяющий выполнять обход с помощью клавиши Tab."""
    def __init__(self, parent):
        """Конструктор класса TreeWidget, принимающий ссылку на родительский элемент."""
        super().__init__(parent)
        self.setTabKeyNavigation(True)
        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setObjectName('tree')
        self.setHeaderLabel("Ваш домашний склад")
        self.setCurrentItem(self.headerItem())
        QShortcut('Escape', self).activated.connect(self.clearSelection)

    def clearSelection(self):
        """Функция установки указателя на первый элемент дерева."""
        super().clearSelection()
        self.setCurrentItem(self.headerItem())

    def mousePressEvent(self, event):
        """Обработчик события клика мышью, устанавливающий указатель на первый элемент дерева."""
        if self.itemAt(event.pos()) is None:
            self.clearSelection()
        QTreeWidget.mousePressEvent(self, event)