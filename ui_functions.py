from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


# import main GUI
from  main import *

# Globals
# set window minimised_restore value
global_state = 0


# init class
class UIFunctions(MainWindow):

    # method to maximize_restore
    def maximize_restore(self):
        global global_state
        status = global_state

        # Maximize window
        if status == 0:
            self.showMaximized()

            # set global to maximized
            global_state = 1

            # Remove margin and border radius if maximized
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.534091 rgba(0, 0, 30, 255), stop:0.761364 rgba(0, 0, 50, 255)); border-radius: 0px;")

        # Minimize window
        else:
            global_state = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.534091 rgba(0, 0, 30, 255), stop:0.761364 rgba(0, 0, 50, 255)); border-radius: 10px;")


    # UI definitions
    def uiDefinitions(self):

        # Remove Frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # Maximise / Restore function binding
        self.ui.btn_max.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # Minimize
        self.ui.btn_min.clicked.connect(lambda: self.showMinimized())


        # Set Dropshadow window
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 100))

        # Apply Dropshadow
        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)

        # Create Size Grip
        self.sizegrip = QtWidgets.QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px} QSizeGrip:hover { background-color: rgb(50, 42, 94) }")

    # return window status
    def returnStatus():
        return global_state
