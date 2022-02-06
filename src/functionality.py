from PyQt6 import QtCore, QtGui, QtWidgets

from btns import bind


# Load fonts form assets directory
def load_font():
    dir_ = QtCore.QDir("assets")
    _id = QtGui.QFontDatabase.addApplicationFont("assets/JetBrains.ttf")

    font = QtGui.QFont("JetBrainsMono NF")
    font.setPointSize(12)

    win_instance.editor.setFont(font)


# Move the window with left click on title bar
def move_window(event: QtGui.QMouseEvent):
    cursor_pos = QtCore.QPoint()
    cursor_pos.setX(win.width() // 2)

    if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
        win.move(win.pos() + event.pos() - cursor_pos)


# Add dropshadow to the window
def add_dropshadow():
    win.shadow = QtWidgets.QGraphicsDropShadowEffect(win)
    win.shadow.setBlurRadius(20)
    win.shadow.setXOffset(0)
    win.shadow.setYOffset(0)
    win.shadow.setColor(QtGui.QColor(0, 0, 0, 100))


def add_functionality(app, app_instance):
    global win, win_instance
    win, win_instance = app, app_instance
    win_instance.editor.setFocus()
    bind(win_instance)
    load_font()
    add_dropshadow()

    win_instance.title_bar.mouseMoveEvent = move_window

    # Disable Window Frames
    win.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)