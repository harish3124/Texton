# Import PyQt and other libraries
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui
import sys

# import local modules
from MainWindow import Ui_MainWindow
from functionality import add_functionality

if __name__ == "__main__":
    # Initiation
    app = QApplication(sys.argv)

    win = QMainWindow()

    win_instance = Ui_MainWindow()
    win_instance.setupUi(win)

    add_functionality(win, win_instance)

    # Show the window
    win.show()
    app.exec()
