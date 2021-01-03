from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.iconName = 'home.png'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.UiComponents()
        self.CloseButton()

        self.show()

    def UiComponents(self):
        button = QPushButton("Click Me", self)
        #button.move(50, 50)
        button.setGeometry(QRect(100, 100, 130, 60))
        button.setIcon(QtGui.QIcon('h.png'))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("This is button")
        #button.setToolTip(<h1>"This is button"</h1>)

    def CloseButton(self):
        button = QPushButton("Close App", self)
        button.setGeometry(QRect(100, 150, 130, 60))
        button.setIcon(QtGui.QIcon('home.png'))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("This button close app")
        button.clicked.connect(self.Close)

    def Close(self):
        sys.exit()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
