from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QVBoxLayout, QHBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Layout Menagement"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 100
        self.iconName = 'h.png'

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.createLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.groupBox)
        self.setLayout(hbox)

        self.show()


    def createLayout(self):
        self.groupBox = QGroupBox("What is your favourite sport?")
        vboxlayout = QVBoxLayout()

        button1 = QPushButton("Football", self)
        button1.setIcon(QtGui.QIcon(self.iconName))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(40)
        vboxlayout.addWidget(button1)

        button2 = QPushButton("Cricket", self)
        button2.setIcon(QtGui.QIcon(self.iconName))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(40)
        vboxlayout.addWidget(button2)

        button3 = QPushButton("Tenis", self)
        button3.setIcon(QtGui.QIcon(self.iconName))
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setMinimumHeight(40)
        vboxlayout.addWidget(button3)

        self.groupBox.setLayout(vboxlayout)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())