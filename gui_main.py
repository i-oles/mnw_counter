from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import QRect
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.title = 'mnw counter'
        self.app_logo = 'app_logo.jpg'
        self.left = 420
        self.top = 250
        self.width = 600
        self.height = 400

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.app_logo))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.initUI()

    def initUI(self):
        self.btn = QPushButton(self)
        self.btn.setIcon(QtGui.QIcon('dir_icon.jpg'))
        self.btn.setIconSize(QtCore.QSize(30, 30))
        self.btn.setGeometry(100, 0, 50, 50)
        self.btn.clicked.connect(self.btn_clicked)

        self.edit_line = QLineEdit(self)

    def btn_clicked(self):
        self.edit_line.setText('my path')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
