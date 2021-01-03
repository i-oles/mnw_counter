from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLabel, QFileDialog, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
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

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(self.iconName))

        vbox = QVBoxLayout()
        self.lineEdit = QLineEdit()

        self.btn = QPushButton("Browse")
        self.btn.clicked.connect(self.browseDir)

        vbox.addWidget(self.btn)


        self.setLayout(vbox)
        self.show()

    def browseDir(self):
        directory = str(QFileDialog.getExistingDirectory())
        self.lineEdit.setText(f'{directory}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

