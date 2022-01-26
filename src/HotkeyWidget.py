# Form implementation generated from reading ui file 'UI/HotkeyWidget.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_hotkey_win(object):
    def setupUi(self, hotkey_win):
        hotkey_win.setObjectName("hotkey_win")
        hotkey_win.resize(400, 300)
        self.drop_shadow_frame = QtWidgets.QFrame(hotkey_win)
        self.drop_shadow_frame.setGeometry(QtCore.QRect(0, 0, 401, 301))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.drop_shadow_frame.setFont(font)
        self.drop_shadow_frame.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(55, 51, 60);")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_bar = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title_bar.setMaximumSize(QtCore.QSize(16777215, 20))
        self.title_bar.setStyleSheet("background-color: none")
        self.title_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_bar.setObjectName("title_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_bar)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spacer1 = QtWidgets.QFrame(self.title_bar)
        self.spacer1.setEnabled(False)
        self.spacer1.setMinimumSize(QtCore.QSize(16, 0))
        self.spacer1.setMaximumSize(QtCore.QSize(0, 0))
        self.spacer1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.spacer1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.spacer1.setObjectName("spacer1")
        self.horizontalLayout.addWidget(self.spacer1)
        self.label_title = QtWidgets.QLabel(self.title_bar)
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(213, 213, 213);\n"
"\n"
"")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.btn_close = QtWidgets.QPushButton(self.title_bar)
        self.btn_close.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close.setMaximumSize(QtCore.QSize(17, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(253, 81, 67);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(254, 79, 69, 150);\n"
"}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout.addWidget(self.title_bar)
        self.contents_frame = QtWidgets.QFrame(self.drop_shadow_frame)
        self.contents_frame.setStyleSheet("background-color: none")
        self.contents_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.contents_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.contents_frame.setObjectName("contents_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.contents_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hotkey_frame = QtWidgets.QFrame(self.contents_frame)
        self.hotkey_frame.setStyleSheet("background-color: rgb(80, 75, 88);")
        self.hotkey_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.hotkey_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.hotkey_frame.setObjectName("hotkey_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.hotkey_frame)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.hotkey_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.hotkey_frame)
        self.verticalLayout.addWidget(self.contents_frame)

        self.retranslateUi(hotkey_win)
        QtCore.QMetaObject.connectSlotsByName(hotkey_win)

    def retranslateUi(self, hotkey_win):
        _translate = QtCore.QCoreApplication.translate
        hotkey_win.setWindowTitle(_translate("hotkey_win", "Form"))
        self.label_title.setText(_translate("hotkey_win", "Hotkeys"))
        self.btn_close.setShortcut(_translate("hotkey_win", "Ctrl+Shift+Q"))
        self.label.setText(_translate("hotkey_win", "Open : Ctrl+O\n"
"\n"
"Save : Ctrl+S\n"
"\n"
"Save As : Ctrl+Shift+s\n"
"\n"
"Close File : Ctrl+W\n"
"\n"
"Quit : Ctrl+Shift+Q"))
