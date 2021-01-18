from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from string_operations import StringOperations
import os
import re
import sys
from datetime import date

class Ui_MainWindow(object):
    def __init__(self):
        self.file_ext = 'jpg'
        self.component = 'mnw'
        self.char_1 = ','
        self.char_2 = '-'
        self.regex_search = f'.*\(0?1\)\.{self.file_ext}?$'
        self.report_dir = 'Daily_Reports'

        self.current_date = date.today()
        self.current_date.strftime("%d-%m-%Y")

        self.logo = 'app_logo.jpg'

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setWindowIcon(QtGui.QIcon(self.logo))

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.labelChoose = QtWidgets.QLabel(self.centralwidget)
        self.labelChoose.setObjectName("labelChoose")
        self.gridLayout.addWidget(self.labelChoose, 0, 0, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.btnBrowse = QtWidgets.QToolButton(self.centralwidget)
        self.btnBrowse.setMaximumSize(QtCore.QSize(50, 50))
        self.btnBrowse.setObjectName("btnBrowse")
        self.btnBrowse.clicked.connect(self.browse_dir)
        self.gridLayout.addWidget(self.btnBrowse, 1, 2, 1, 1)

        self.cBoxCount = QtWidgets.QCheckBox(self.centralwidget)
        self.cBoxCount.setObjectName("cBoxCount")
        self.gridLayout.addWidget(self.cBoxCount, 2, 0, 1, 1)
        self.cBoxList = QtWidgets.QCheckBox(self.centralwidget)
        self.cBoxList.setObjectName("cBoxList")
        self.gridLayout.addWidget(self.cBoxList, 3, 0, 1, 1)

        self.btnCount = QtWidgets.QPushButton(self.centralwidget)
        self.btnCount.setMinimumSize(QtCore.QSize(0, 50))
        self.btnCount.setObjectName("btnCount")
        self.btnCount.setDisabled(True)
        self.lineEdit.textChanged.connect(self.btn_count_disabled)
        self.btnCount.clicked.connect(self.count_btn_clicked)

        self.gridLayout.addWidget(self.btnCount, 4, 0, 1, 3)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)

        self.labelPhotographed = QtWidgets.QLabel(self.centralwidget)
        self.labelPhotographed.setObjectName("labelPhotographed")
        self.gridLayout.addWidget(self.labelPhotographed, 6, 0, 1, 1)
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.gridLayout.addWidget(self.labelResult, 6, 1, 1, 1)
        self.labelListSingles = QtWidgets.QLabel(self.centralwidget)
        self.labelListSingles.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelListSingles.setObjectName("labelListSingles")
        self.gridLayout.addWidget(self.labelListSingles, 7, 0, 1, 1)
        self.listWidgetSingles = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetSingles.setMinimumSize(QtCore.QSize(0, 200))
        self.listWidgetSingles.setObjectName("listWidgetSingles")
        self.gridLayout.addWidget(self.listWidgetSingles, 7, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.labelListSets = QtWidgets.QLabel(self.centralwidget)
        self.labelListSets.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelListSets.setObjectName("labelListSets")
        self.gridLayout.addWidget(self.labelListSets, 9, 0, 1, 1)
        self.listWidgetSets = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetSets.setMinimumSize(QtCore.QSize(0, 160))
        self.listWidgetSets.setMaximumSize(QtCore.QSize(16777215, 160))
        self.listWidgetSets.setObjectName("listWidgetSets")
        self.gridLayout.addWidget(self.listWidgetSets, 9, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exportResults = QtWidgets.QAction(MainWindow)
        self.exportResults.setObjectName("exportResults")
        self.exportResults.setDisabled(True)

        self.menuFile.triggered.connect(self.save_to_file)
        self.menuFile.triggered.connect(lambda: self.show_popup('Info', f'Your data was successfully exported to folder {self.report_dir} in your images directory'))

        self.aboutCounter = QtWidgets.QAction(MainWindow)
        self.aboutCounter.setObjectName("aboutCounter")
        self.menuFile.addAction(self.exportResults)
        self.menuAbout.addAction(self.aboutCounter)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MNW counter"))
        self.labelListSingles.setText(_translate("MainWindow", "List of objects:"))
        self.cBoxList.setText(_translate("MainWindow", "Display objects list"))
        self.cBoxCount.setText(_translate("MainWindow", "Display counting result"))
        self.btnBrowse.setText(_translate("MainWindow", "..."))
        self.labelListSets.setText(_translate("MainWindow", "List of objects in sets:"))
        self.labelChoose.setText(_translate("MainWindow", "Choose folder to browse (with or without subfolders):"))
        self.labelPhotographed.setText(_translate("MainWindow", "Photographed objects:"))
        self.btnCount.setText(_translate("MainWindow", "count"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.exportResults.setText(_translate("MainWindow", "Export results..."))
        self.exportResults.setStatusTip(_translate("MainWindow", "Export all results to file"))
        self.exportResults.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.aboutCounter.setText(_translate("MainWindow", "About counter"))
        self.aboutCounter.setStatusTip(_translate("MainWindow", "All information about program"))
        self.aboutCounter.setShortcut(_translate("MainWindow", "F1"))

    def btn_count_disabled(self):
        if len(self.lineEdit.text()) > 0:
            self.btnCount.setDisabled(False)

    def save_as_disabled(self):
        if self.listWidgetSingles.count() > 0 or len(self.labelResult.text()) > 0:
            self.exportResults.setDisabled(False)

    def browse_dir(self):
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(f'{self.directory}')

    def clear_widgets_after_clicked(self):
        self.progressBar.setValue(0)
        self.labelResult.clear()
        self.listWidgetSingles.clear()
        self.listWidgetSets.clear()

    def count_btn_clicked(self):
        self.clear_widgets_after_clicked()
        self.verify_lineEdit()

        if not self.cBoxCount.isChecked() and not self.cBoxList.isChecked():
            self.show_popup('Info', 'Please choose one of the following display options')
        elif self.cBoxCount.isChecked() or self.cBoxList.isChecked():
            self.walk_dir()
            self.make_singles_and_set_list()
            self.counting_progress()
            if self.cBoxCount.isChecked():
                self.count_result = str(len(self.singles_long))
                self.labelResult.setText(self.count_result)
            if self.cBoxList.isChecked():
                self.list_display(self.singles_long, self.listWidgetSingles)
                self.list_display(self.sets_long, self.listWidgetSets)
        self.save_as_disabled()

    def verify_lineEdit(self):
        if len(self.lineEdit.text()) > 0:
            self.directory = str(self.lineEdit.text())
        elif len(self.lineEdit.text()) == 0:
            self.lineEdit.clear()
            self.clear_widgets_after_clicked()
            self.show_popup('Info', 'Choose directory path!')

    def show_popup(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()

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
        self.singles_long = sorted(self.singles_long)
        self.sets_long = sorted(self.sets_long)

    def counting_progress(self):
        for percent in range(101):
            self.progressBar.setValue(percent)

    def list_display(self, list, widget):
        for num, item in enumerate(list):
            widget.insertItem(num, item)

    def save_to_file(self):
        if not os.path.exists(f'{self.directory}/{self.report_dir}'):
            os.mkdir(f'{self.directory}/{self.report_dir}')

        def list_format(some_list):
            return [(x + '\n') for x in some_list]

        result_file = open(r'{}/{}/{}.txt'.format(self.directory, self.report_dir, self.current_date), 'w')
        date_line = f'Date: {self.current_date} \n \n'
        counter_line = f'You had taken pictures of {self.count_result} objects. \n \n'
        label_singles = f'{self.labelPhotographed.text()} \n'
        label_sets = f'{self.labelListSets.text()} \n'
        result_file.write(date_line)
        result_file.write(counter_line)
        result_file.write(label_singles)
        result_file.writelines(list_format(self.singles_long))
        result_file.write('\n\n')
        if not self.listWidgetSets.count() == 0:
            result_file.write(label_sets)
            result_file.writelines(list_format(self.sets_long))
        result_file.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
