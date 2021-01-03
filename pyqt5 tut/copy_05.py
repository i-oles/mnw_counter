from PyQt5.QtWidgets import QDialog, QGroupBox, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
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
        vbox = QVBoxLayout()    # always when you create layoutbox you have to setLayout

        label1 = QLabel("This is It!")
        vbox.addWidget(label1)

        label2 = QLabel("And This")
        label2.setFont(QtGui.QFont('Gill Sans', 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)

        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox()
        hboxlayout = QHBoxLayout()

        button = QPushButton('home', self)
        button.setIcon(QtGui.QIcon('home.png'))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setMinimumHeight(40)
        #button.setGeometry(QRect(120, 120, 100, 60)) # if layout: do not need setGeometry
        hboxlayout.addWidget(button)

        self.groupBox.setLayout(hboxlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())