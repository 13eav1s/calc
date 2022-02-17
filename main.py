'''
Программа калькулятор
Краснов Леонид ИУ7-21Б
'''

from PyQt6.QtWidgets import QApplication, QMainWindow

import design
import sys


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    design.Ui_MainWindow().setupUi(window)

    window.show()
    sys.exit(app.exec())


application()
