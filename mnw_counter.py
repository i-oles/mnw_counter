from PyQt5 import QtCore, QtGui, QtWidgets
from string_operations import StringOperations
import os
import re
import sys
import time


class Ui_MainWindow(object):
    def __init__(self):
        self.file_ext = 'jpg'
        self.component = 'mnw'
        self.char_1 = ','
        self.char_2 = '-'
        self.regex_search = f'.*\(0?1\)\.{self.file_ext}?$'


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 601)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_choose = QtWidgets.QLabel(self.centralwidget)
        self.label_choose.setGeometry(QtCore.QRect(20, 10, 331, 16))
        #self.label_choose.setObjectName("label_choose")
        self.label_choose.setText("Choose folder to browse (with or without subfolders):")

        self.line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.line_edit.setGeometry(QtCore.QRect(20, 30, 351, 21))
        self.line_edit.setObjectName("line_edit")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(380, 30, 31, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.browse_dir)

        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(200, 60, 161, 20))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(200, 80, 161, 20))
        self.checkBox_2.setObjectName("checkBox_2")

        self.btn_count = QtWidgets.QPushButton(self.centralwidget)
        self.btn_count.setGeometry(QtCore.QRect(20, 120, 391, 20))
        self.btn_count.setObjectName("btn_count")
        self.btn_count.clicked.connect(self.count_objects)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 150, 391, 10))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.label_counting = QtWidgets.QLabel(self.centralwidget)
        self.label_counting.setGeometry(QtCore.QRect(20, 200, 101, 16))
        self.label_counting.setObjectName("label_counting")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(20, 220, 161, 191))
        self.label_result.setObjectName("label_result")

        self.label_singles = QtWidgets.QLabel(self.centralwidget)
        self.label_singles.setGeometry(QtCore.QRect(200, 200, 211, 16))
        self.label_singles.setObjectName("label_singles")
        self.listWidget_singles = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_singles.setGeometry(QtCore.QRect(200, 220, 211, 191))
        self.listWidget_singles.setObjectName("listView_singles")

        self.label_sets = QtWidgets.QLabel(self.centralwidget)
        self.label_sets.setGeometry(QtCore.QRect(200, 430, 211, 16))
        self.label_sets.setObjectName("label_sets")
        self.listWidget_sets = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_sets.setGeometry(QtCore.QRect(200, 450, 211, 71))
        self.listWidget_sets.setObjectName("label_result_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionImport_list_as_PDF = QtWidgets.QAction(MainWindow)
        self.actionImport_list_as_PDF.setObjectName("actionImport_list_as_PDF")
        self.menuFile.addAction(self.actionImport_list_as_PDF)
        self.menuAbout.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.progressBar.setValue(0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_choose.setText(_translate("MainWindow", "Choose folder to browse (with or without subfolders):"))
        self.checkBox_1.setText(_translate("MainWindow", "display list of objects"))
        self.btn_count.setText(_translate("MainWindow", "count"))
        self.label_counting.setText(_translate("MainWindow", "Counting result:"))
        self.label_singles.setText(_translate("MainWindow", "List of photographed objects:"))
        self.label_sets.setText(_translate("MainWindow", "More info:"))
        self.label_result.setText(_translate("MainWindow", ""))
        self.checkBox_2.setText(_translate("MainWindow", "display list of sets"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionImport_list_as_PDF.setText(_translate("MainWindow", "Import list..."))

    def browse_dir(self):
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.line_edit.setText(f'{self.directory}')

    def count_objects(self):
        # dodaj clear to widgetlist
        self.walk_dir()
        self.make_singles_and_set_list()
        self.count_result = str(len(self.singles_long))
        self.label_result.setText(f"Photographed objects: \n{self.count_result}")
        if self.checkBox_1.isChecked():
            self.list_display(self.singles_long, self.listWidget_singles)
            self.list_display(self.sets_long, self.listWidget_sets)
        #elif self.checkBox_2.isChecked():


        #else -> popup window
        self.counting_progress()


    def walk_dir(self):
        self.ones_all = []
        for subdir, dirs, files in os.walk(self.directory):
            for file in files:
                first_file = re.findall(r'{}'.format(self.regex_search), file)
                if first_file:
                    self.ones_all.append(file)

    def make_singles_and_set_list(self):
        ones_splited = list(StringOperations.split_duets(self.ones_all, self.char_1, self.component))
        ones_without_mnw = [StringOperations.cut_char(item, self.component) for item in ones_splited]
        ones_unique = list(set(ones_without_mnw))
        ones_short = [StringOperations.cut_char(item, self.char_2) for item in ones_unique]
        ones_zipped = zip(ones_short, ones_unique)
        ones_dict = dict(ones_zipped)
        singles_short = list(set(ones_short))
        ones_dict_keys = ones_dict.keys()

        self.singles_long = []
        self.sets_long = ones_unique.copy()
        for item in singles_short:
            if item in ones_dict_keys:
                self.singles_long.append(ones_dict[item])
                self.sets_long.remove(ones_dict[item])

    # add sort

    def counting_progress(self):
        for percent in range(101):
            #time.sleep(0.05)
            self.progressBar.setValue(percent)

    def list_display(self, some_list, some_widget):
        for num, item in enumerate(some_list):
            some_widget.insertItem(num, item)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
