# Import PyQt and other libraries
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui
import sys

# import local modules
from btns import bind
from MainWindow import Ui_MainWindow

# Load fonts form assets directory
def load_font():
    dir_ = QtCore.QDir("assets")
    _id = QtGui.QFontDatabase.addApplicationFont("assets/JetBrains.ttf")

    font = QtGui.QFont("JetBrainsMono NF")
    font.setPointSize(12)

    win_instance.editor.setFont(font)


def add_functionality():
    win_instance.editor.setFocus()
    bind(win_instance)
    load_font()

    # Disable Window Frames
    win.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)


if __name__ == "__main__":
    # Initiation
    app = QApplication(sys.argv)

    win = QMainWindow()

    win_instance = Ui_MainWindow()
    win_instance.setupUi(win)

    add_functionality()

    # Show the window
    win.show()
    app.exec()
