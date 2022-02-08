from PyQt6.QtWidgets import QFileDialog, QDialogButtonBox

from MainWindow import Ui_MainWindow
from FileSaveDialog import FileSaveDialog
from hotkeys import show_hotkeys

win_instance: Ui_MainWindow
file_path = ""
is_saved = False


# Set Title to file name
def set_title():
    if file_path == "":
        win_instance.label_title.setText("Untitled")
        return

    # Use Platform specific seperators ( "\" for windows and "/" for *NIX)
    path_seperator = "\\" if "\\" in file_path else "/"
    file_name = file_path.split(path_seperator)[-1]
    win_instance.label_title.setText(file_name)


# Prompt the FileSaveDialog
def file_save_prompt():
    if win_instance.editor.toPlainText() == "":
        return True

    # Create dialog
    file_dialog = FileSaveDialog()
    pressed_button = file_dialog.exec()

    # Check the keycodes returned:
    # Save --> 1
    # No --> 0
    if pressed_button == 1:
        save()
        return True
    elif pressed_button == 0:
        return True
    else:
        return False


# Exit
def close():
    if file_save_prompt():
        exit()


# Open a file
def open_file():

    # Save before opening a new file
    save_as()

    global file_path
    file_path = QFileDialog().getOpenFileName()[0]

    # Check if the dialog does not return a file name
    if file_path == "":
        return

    with open(file_path, "r") as fp:
        win_instance.editor.setPlainText(fp.read())
        print(fp.read())
        fp.close()

    set_title()


def save():
    # If the File Path is empty then call the save_as function
    if file_path == "":
        save_as()
        return

    with open(file_path, "w") as fp:
        fp.write(win_instance.editor.toPlainText())
        fp.close()

    set_title()


def save_as():
    global file_path
    file_path = QFileDialog().getSaveFileName()[0]

    # Check if the dialog does not return a file name
    if file_path == "":
        return

    save()


# Save the file and then clear the editor
def close_file():
    if file_save_prompt():
        win_instance.editor.setPlainText("")
        set_title()


# Bind all the Buttons
def bind(win: Ui_MainWindow):

    global win_instance
    win_instance = win

    win.btn_close.clicked.connect(close)
    win.btn_file_close.clicked.connect(close_file)
    win.btn_open.clicked.connect(open_file)
    win.btn_save.clicked.connect(save)
    win.btn_save_as.clicked.connect(save_as)

    win.btn_hotkey.clicked.connect(show_hotkeys)
