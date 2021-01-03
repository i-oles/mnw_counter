from PyQt5.QtWidgets import QDialog, QGroupBox, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = 'my app'
        self.top = 300
        self.left = 200
        self.width = 300
        self.height = 300
        self.iconName = 'h.png'

        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(self.iconName))

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()

        button1 = QPushButton('home', self)
        button1.setIcon(QtGui.QIcon('home.png'))
        button1.setIconSize(QtCore.QSize(40, 40))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1, 0, 0)

        button2 = QPushButton('home', self)
        button2.setIcon(QtGui.QIcon('home.png'))
        button2.setIconSize(QtCore.QSize(40, 40))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2, 0, 1)

        button3 = QPushButton('home', self)
        button3.setIcon(QtGui.QIcon('home.png'))
        button3.setIconSize(QtCore.QSize(40, 40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3, 1, 0)

        button4 = QPushButton('home', self)
        button4.setIcon(QtGui.QIcon('home.png'))
        button4.setIconSize(QtCore.QSize(40, 40))
        button4.setMinimumHeight(40)
        gridLayout.addWidget(button4, 1, 1)

        self.groupBox.setLayout(gridLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())