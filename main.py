from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
import sys


# import GUI file
from ui_main import Ui_MainWindow


# import functions
from ui_functions import *


# Globals
# File name
file_name = ""

# initialize window
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Move Window
        def moveWindow(event):

            # Check is Minimized
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)
            # if left click move window
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow

        # Set UI definitions
        UIFunctions.uiDefinitions(self)

        # Connect keys
        self.ui.btn_open.clicked.connect(lambda: self.open_file())

        self.ui.btn_save.clicked.connect(lambda: self.save())

        self.ui.btn_save_as.clicked.connect(lambda: self.save_as())

        self.ui.btn_doc_close.clicked.connect(lambda: self.close_doc())

        self.ui.btn_close.clicked.connect(lambda: self.exit_win())
        # show window
        self.show()

    # Save and exit
    def exit_win(self):
        if file_name == "" and self.ui.textEdit.toPlainText() == "":
            self.close()
        else:
            self.save()
            self.close()

    # Close doc
    def close_doc(self):
        global file_name

        self.save()

        file_name = ""

        self.ui.textEdit.setText("")
        self.ui.label_title.setText("Untitled")
        self.ui.label_status.setText("Untitled")

    # open file and write
    def save(self):
        global file_name
        if file_name == "":
            self.save_as()

        else:
            try:
                content = self.ui.textEdit.toPlainText()
                if content != "":
                    with open(file_name, "w") as file_n:
                        file_n.write(content)
                        self.ui.label_status.setText("Saved")
                        file_n.close()

            except:
                pass

    # Save_As method 
    def save_as(self):
        global file_name
            
        try:
            name = QtWidgets.QFileDialog.getSaveFileName(self, "Save As")
            if name[0] != "":
                file_name = name[0]
                self.ui.label_title.setText((file_name.split("/"))[-1])
                self.save()
        except:
            pass

    # open file
    def open_file(self):
        global file_name
        try:
            name = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")

            if name[0] != "":
                file_name = name[0]
                with open(file_name, "r") as file_n:
                    data = file_n.read()
                    self.ui.textEdit.setText(str(data))
                    self.ui.label_title.setText((file_name.split("/"))[-1])
                    self.ui.label_status.setText("Opened")
                    file_n.close()

        except:
            pass


    # App Events
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

# run GUI app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())