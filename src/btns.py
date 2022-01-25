from MainWindow import Ui_MainWindow


def close():
    print("Closing pytext 😞")
    exit()


def open():
    pass


def save():
    pass


def save_as():
    pass


def close_file():
    pass


def show_hotkeys():
    pass


# Bind all the Buttons
def bind(win: Ui_MainWindow):
    win.btn_close.clicked.connect(close)
    win.btn_file_close.clicked.connect(close_file)
    win.btn_open.clicked.connect(open)
    win.btn_hotkey.clicked.connect(show_hotkeys)
    win.btn_save.clicked.connect(save)
    win.btn_save_as.clicked.connect(save_as)
