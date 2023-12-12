from PyQt6.QtWidgets import QDialog
from addElementUI import Ui_Form

class AddElement(Ui_Form, QDialog):
    def __init__(self, parentWindow):
        # Window Init
        super().__init__()
        self.setupUi(self)
        self.boxName.setFocus()
        self.buttonOK.setDefault(True)

        # Add button handlers
        self.parentWindow = parentWindow # temp
        self.buttonCancel.clicked.connect(self.close)
        self.buttonOK.clicked.connect(self.OKHandler)

        # Add variables
        self.parentWindow = parentWindow

    def OKHandler(self):
        selected = self.parentWindow.tree.selectedItems()
        text = self.boxName.text()
        count = self.boxCount.value()

        if not text:
            self.boxName.setStyleSheet(
                "border-width: 1px; border-color: red; border-style: solid")
            return

        if selected:
            for parent in selected:
                self.parentWindow.treeController.addItems(text, count, parent)
        else:
            self.parentWindow.treeController.addItems(text, count)
        self.close()