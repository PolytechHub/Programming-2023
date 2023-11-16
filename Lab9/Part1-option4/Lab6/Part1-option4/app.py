import sys
from functions import get_array, get_num, f1a, f1b, f2
from PyQt6.QtWidgets import QFileDialog, QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
filename, _ = QFileDialog.getSaveFileName(
    window, "Save data", "data.txt", "Text (*.txt)")
if filename != '':
    with open(filename, 'w') as f:
        array = get_array()
        a = get_num(0)
        k1 = get_num(0, len(array) - 2)
        k2 = get_num(k1, len(array) - 1)
        f.write(f"Array: {array}\n")
        f.write(f"a: {a}\n")
        f.write(f"k1: {k1}\n")
        f.write(f"k2: {k2}\n")
        f.write(f"f1a: {f1a(array, a)}\n")
        f.write(f"f1b: {f1b(array, k1, k2)}\n")
        f.write(f"f2: {f2(array)}\n")