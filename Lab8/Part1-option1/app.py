import sys
import design
from PyQt6.QtWidgets import QMainWindow, QApplication, QSpinBox, QLineEdit

class App(design.Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resultButton.clicked.connect(self.resultHandler)

    def resultHandler(self):
        self.resultBox.setText(function(
            self.eventBox.itemText(self.eventBox.currentIndex()),
            f"{self.usernameBox.text()}  {self.IDBox.text()}",
            self.messageBox.text()
        ))

def function(event, userdata, message=None):
    name, id = userdata.replace('  ', ' ').split(' ')

    if not name:
        name = "NoName"

    res = ""
    if event == "GREETING":
        res = f"For {id}: Hello, {name}. Welcome to our nice service!"
    elif event == "NOTIFY" or event == "DENIAL":
        res = f"For {id}: Sir/Madam {name}, regarding your application: {message}"
    else:
        return "wrong event"

    if len(res) > 253:
        res = res[:253]
        res += "..."

    return res
    
def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()