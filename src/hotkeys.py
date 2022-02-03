# Import PyQt and other libraries
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6 import QtGui

from HotkeyWidget import Ui_hotkey_win


def show_hotkeys():
    # Initiation
    widget = QWidget()

    widget_instance = Ui_hotkey_win()
    widget_instance.setupUi(widget)

    # Disable Window Frames
    widget.setWindowFlag(Qt.WindowType.FramelessWindowHint)

    # Bind the close button
    widget_instance.btn_close.clicked.connect(lambda: widget.destroy())

    # load the font
    font = QtGui.QFont("JetBrainsMono NF")
    font.setPointSize(15)
    widget_instance.label.setFont(font)

    # Show the window
    widget.show()

    return widget
