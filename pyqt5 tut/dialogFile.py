from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLabel, QFileDialog
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
        self.btn = QPushButton("Browse")
        self.btn.clicked.connect(self.browseImage)
        vbox.addWidget(self.btn)

        self.label = QLabel()
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def browseImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Image files (*.jpg, *.png)')

        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        #self.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

