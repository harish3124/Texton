from PyQt6.QtWidgets import QFileDialog

from MainWindow import Ui_MainWindow

win_instance: Ui_MainWindow
file_path = ""

# Exit
def close():
    exit()


# Open a file
def open_file():
    global file_path
    file_path = QFileDialog().getOpenFileName()[0]

    # Check if the dialog does not return a file name
    if file_path == "":
        return

    with open(file_path, "r") as fp:
        win_instance.editor.setPlainText(fp.read())
        print(fp.read())
        fp.close()


def save():
    # If the File Path is empty then call the save_as function
    if file_path == "":
        save_as()

    with open(file_path, "w") as fp:
        fp.write(win_instance.editor.toPlainText())
        fp.close()


def save_as():
    global file_path
    file_path = QFileDialog().getSaveFileName()[0]

    # Check if the dialog does not return a file name
    if file_path == "":
        return

    save()


# Save the file and then clear the editor
def close_file():
    save_as()
    win_instance.editor.setPlainText("")


def show_hotkeys():
    pass


# Bind all the Buttons
def bind(win: Ui_MainWindow):

    global win_instance
    win_instance = win

    win.btn_close.clicked.connect(close)
    win.btn_file_close.clicked.connect(close_file)
    win.btn_open.clicked.connect(open_file)
    win.btn_hotkey.clicked.connect(show_hotkeys)
    win.btn_save.clicked.connect(save)
    win.btn_save_as.clicked.connect(save_as)
