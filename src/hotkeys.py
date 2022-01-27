# Import PyQt and other libraries
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

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

    # Show the window
    widget.show()

    return widget
