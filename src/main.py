# Import PyQt and other libraries
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# import local modules
from btns import bind
from MainWindow import Ui_MainWindow


def add_functionality():
    win_instance.editor.setFocus()
    bind(win_instance)


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
