from PyQt5 import QtWidgets, QtGui
from collections import defaultdict
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt
from string_operations import StringOperations
from file_exporter import FileExporter, REPORT_DIR_NAME
from gui import Ui_MainWindow
from about_widget import Ui_widget
import os
import re
import sys


class Ui_AboutWindow(Ui_widget, QMainWindow):
    def __init__(self, parent=None):
        super(Ui_AboutWindow, self).__init__(parent)
        self.setupUi(self)

        about_app_description = QtGui.QPixmap()
        about_app_description.load('about_IzzyCounter.png')
        self.imageLabel.setPixmap(about_app_description)
        self.verticalLayout.addWidget(self.imageLabel)


class IzzyCounterWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(IzzyCounterWindow, self).__init__(parent)
        self.setupUi(self)
        self.center_on_screen()

        self.component = 'mnw'
        self.coma_char = ','
        self.hyphen_char = '-'
        self.tiff_ext = 'tiff'
        self.jpg_ext = 'jpg'

        self.second_window = Ui_AboutWindow(self)

        #default settings
        self.cBoxList.setChecked(True)
        self.cBoxCount.setChecked(True)
        self.cBoxTiff.setChecked(True)
        self.btnCount.setDisabled(True)
        self.exportResults.setDisabled(True)

        #widgets connections
        self.cBoxTiff.stateChanged.connect(self.uncheck_another_cBox)
        self.cBoxJpg.stateChanged.connect(self.uncheck_another_cBox)
        self.lineEdit.textChanged.connect(self.unlock_btn_count)
        self.btnBrowse.clicked.connect(self.set_dir_path_in_lineEdit)
        self.btnCount.clicked.connect(self.when_btnCount_clicked)
        self.menuFile.triggered.connect(self.export_to_file)
        self.menuAbout.triggered.connect(self.show_about_IzzyCounter)
        self.menuFile.triggered.connect(
            lambda: self.show_popup(f"Your results was successfully exported to folder '{REPORT_DIR_NAME}' in your images folder"))

    def center_on_screen(self):
        geometry = self.frameGeometry()
        center_p = QDesktopWidget().availableGeometry().center()
        geometry.moveCenter(center_p)
        self.move(geometry.topLeft())

    def uncheck_another_cBox(self, state):
        if state == Qt.Checked:
            if self.sender() == self.cBoxTiff:
                self.cBoxJpg.setChecked(False)
            else:
                self.cBoxTiff.setChecked(False)

    def unlock_btn_count(self):
        if len(self.lineEdit.text()) > 0:
            self.btnCount.setDisabled(False)

    def set_dir_path_in_lineEdit(self):
        self.directory_path = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(f'{self.directory_path}')

    # *** actions called after btnCount clicked ***
    def when_btnCount_clicked(self):
        self.clear_widgets_after_clicked()
        self.check_file_extention(self.tiff_ext, self.jpg_ext)
        self.check_is_empty(self.lineEdit, self.show_popup, 'Please choose directory path!')
        self.is_manual_path_ok()
        if self.dir_path_ok:
            self.when_all_cBox_unchecked(self.cBoxTiff, self.cBoxJpg, self.show_popup, 'Please choose file extension!')
            if self.cBoxJpg.isChecked() or self.cBoxTiff.isChecked():
                self.when_all_cBox_unchecked(self.cBoxCount, self.cBoxList, self.show_popup, 'Please choose display option!')
                if self.dir_path_ok and (self.cBoxCount.isChecked() or self.cBoxList.isChecked()):
                    self.find_all_ones_from_dir()
                    self.make_singles_and_set_list()
                    self.counting_progress()
                    self.display_count_result()
                    self.display_item_lists()
                    self.allow_export_results()

    def clear_widgets_after_clicked(self):
        self.progressBar.setValue(0)
        self.labelResult.clear()
        self.listWidgetSingles.clear()
        self.listWidgetSets.clear()

    def check_file_extention(self, ext_1, ext_2):
        if self.cBoxTiff.isChecked():
            self.file_ext = ext_1
        else:
            self.file_ext = ext_2

    def check_is_empty(self, widget, func, message):
        if not widget.text():
            func(message)

    # *** checking directory path typed manually ***
    def is_manual_path_ok(self):
        self.directory_path = str(self.lineEdit.text())
        self.dir_path_ok = os.path.isdir(self.directory_path)
        if self.lineEdit.text():
            if not self.dir_path_ok:
                self.show_popup('Path does not exist! Please type or choose correct path!')

    def when_all_cBox_unchecked(self, cBox1, cBox2, func, message):
        if not cBox1.isChecked() and not cBox2.isChecked():
            func(message)

    # *** finding all files ended with '(1)' (ones) from provided directory
    def find_all_ones_from_dir(self):
        self.ones_all = []
        self.regex_search = rf'.*\(0?0?0?1\)\.{self.file_ext}?$'
        for subdir, dirs, files in os.walk(self.directory_path):
            for file in files:
                first_file = re.findall(r'{}'.format(self.regex_search), file)
                if first_file:
                    self.ones_all.append(file)

    # *******   1. some of files can have two objects in filename --> function at first separate them
    #           2. all files has 'mnw' in filename --> function cut everything from 'mnw' (include)
    #           3. cutting 'mnw' cause many duplicates --> making a set to develop only unique names

    def make_singles_and_set_list(self):
        ones_separated = list(StringOperations.split_two_items(self.ones_all, self.coma_char, self.component))
        ones_without_mnw = [StringOperations.cut_in_char(item, self.component) for item in ones_separated]
        ones_unique = sorted(list(set(ones_without_mnw)))
        ones_short = [StringOperations.cut_in_char(item, self.hyphen_char) for item in ones_unique]
        ones_zipped = list(zip(ones_short, ones_unique))
        ones_in_multi_keys_dict = defaultdict(list)
        StringOperations.add_ones_to_multi_keys_dict(ones_zipped, ones_in_multi_keys_dict)
        singles_short = list(set(ones_short))
        ones_dict_keys = ones_in_multi_keys_dict.keys()

        self.singles_long = []
        self.sets_long = ones_unique.copy()
        for item in singles_short:
            if item in ones_dict_keys:
                self.singles_long.append(ones_in_multi_keys_dict[item][0])
                self.sets_long.remove(ones_in_multi_keys_dict[item][0])
        self.singles_long = sorted(self.singles_long)
        self.sets_long = sorted(self.sets_long)
        return self.singles_long, self.sets_long

    def counting_progress(self):
        for percent in range(101):
            self.progressBar.setValue(percent)

    def display_count_result(self):
        if self.cBoxCount.isChecked():
            self.count_result = str(len(self.singles_long))
            self.labelResult.setText(self.count_result)

    def display_item_lists(self):
        if self.cBoxList.isChecked():
            self.list_display(self.singles_long, self.listWidgetSingles)
            self.list_display(self.sets_long, self.listWidgetSets)

    def allow_export_results(self):
        if self.listWidgetSingles.count() > 0 or len(self.labelResult.text()) > 0:
            self.exportResults.setDisabled(False)

    def show_about_IzzyCounter(self):
        self.second_window.show()

    def list_display(self, list, widget):
        for num, item in enumerate(list):
            widget.insertItem(num, item)

    def export_to_file(self):
        exporter = FileExporter(self.directory_path, self.count_result, self.singles_long, self.sets_long)
        exporter.generate_report()

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = IzzyCounterWindow()
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app_logo.png')
    app.setWindowIcon(QtGui.QIcon(icon_path))
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
