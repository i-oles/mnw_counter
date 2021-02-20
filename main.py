from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt
from string_operations import StringOperations, FileContent
from gui import Ui_MainWindow
from about_widget import Ui_widget
import os
import re
import sys
from datetime import date

#todo design logo
#todo fix progress bar
#todo commentary
#todo about window design
#todo make test file


class Ui_AboutWindow(Ui_widget, QMainWindow):
    def __init__(self, parent=None):
        super(Ui_AboutWindow, self).__init__(parent)
        self.setupUi(self)


class IzzyCounterWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(IzzyCounterWindow, self).__init__(parent)
        self.setupUi(self)
        self.center_on_screen()

        self.component = 'mnw'
        self.coma_char = ','
        self.hyphen_char = '-'
        self.report_dir = 'Daily_Reports'
        self.tiff_ext = 'tiff'
        self.jpg_ext = 'jpg'

        self.current_date = date.today()
        self.current_date.strftime("%d-%m-%Y")

        self.second_window = Ui_AboutWindow(self)

        # *** default app settings ***
        self.cBoxList.setChecked(True)
        self.cBoxCount.setChecked(True)
        self.cBoxTiff.setChecked(True)
        self.btnCount.setDisabled(True)
        self.exportResults.setDisabled(True)

        # *** widgets connections ***
        self.cBoxTiff.stateChanged.connect(self.uncheck_another_cBox)
        self.cBoxJpg.stateChanged.connect(self.uncheck_another_cBox)
        self.lineEdit.textChanged.connect(self.unlock_btn_count)
        self.btnBrowse.clicked.connect(self.browse_dir)
        self.btnCount.clicked.connect(self.when_btnCount_clicked)
        self.menuFile.triggered.connect(self.export_to_file)
        self.menuAbout.triggered.connect(self.show_about_IzzyCounter)
        self.menuFile.triggered.connect(
            lambda: self.show_popup(f"Your results was successfully exported to folder '{self.report_dir}' in your images folder"))

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

    # *** setting up directory path using btnBrowse ***
    def browse_dir(self):
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(f'{self.directory}')

    # *** actions called after btnCount clicked (clearing widgets, verifying directory path, checkboxes, and finally counting and making lists) ***
    def when_btnCount_clicked(self):
        self.clear_widgets_after_clicked()
        self.check_file_extention(self.tiff_ext, self.jpg_ext)
        self.check_is_empty(self.lineEdit, self.show_popup, 'Please choose directory path!')
        self.is_manual_path_typing_correct()
        if self.dir_path_ok:
            self.cBoxes_unchecked(self.cBoxTiff, self.cBoxJpg, self.show_popup, 'Please choose file extension!')
            if self.cBoxJpg.isChecked() or self.cBoxTiff.isChecked():
                self.cBoxes_unchecked(self.cBoxCount, self.cBoxList, self.show_popup, 'Please choose display option!')
                if self.dir_path_ok and (self.cBoxCount.isChecked() or self.cBoxList.isChecked()):
                    self.find_all_ones_from_dir()
                    self.make_singles_and_set_list()
                    self.counting_progress()
                    self.display_count_result()
                    self.display_item_lists()
                    self.allow_export_results_after_count()

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

    def is_manual_path_typing_correct(self):
        self.directory = str(self.lineEdit.text())
        self.dir_path_ok = os.path.isdir(self.directory)
        if self.lineEdit.text():
            if not self.dir_path_ok:
                self.show_popup('Path does not exist! Please type or choose correct path!')

    def cBoxes_unchecked(self, cBox1, cBox2, func, message):
        if not cBox1.isChecked() and not cBox2.isChecked():
            func(message)

    # *** finding all files ended with '(1)' (ones) from provided directory
    def find_all_ones_from_dir(self):
        self.ones_all = []
        self.regex_search = f'.*\(0?1\)\.{self.file_ext}?$'
        for subdir, dirs, files in os.walk(self.directory):
            for file in files:
                first_file = re.findall(r'{}'.format(self.regex_search), file)
                if first_file:
                    self.ones_all.append(file)

    # *** separating two object names from one filename, cutting everything after 'mnw' (included), making a set to find only unique ones
    # *** then it's filtering them and appending to lists of objects.
    def make_singles_and_set_list(self):
        self.singles_long = []

        ones_separated = list(StringOperations.split_two_items(self.ones_all, self.coma_char, self.component))
        ones_without_mnw = [StringOperations.cut_in_char(item, self.component) for item in ones_separated]
        ones_unique = list(set(ones_without_mnw))
        ones_short = [StringOperations.cut_in_char(item, self.hyphen_char) for item in ones_unique]
        ones_dict = dict(zip(ones_short, ones_unique))
        singles_short = list(set(ones_short))
        ones_dict_keys = ones_dict.keys()

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

    def display_count_result(self):
        if self.cBoxCount.isChecked():
            self.count_result = str(len(self.singles_long))
            self.labelResult.setText(self.count_result)

    def display_item_lists(self):
        if self.cBoxList.isChecked():
            self.list_display(self.singles_long, self.listWidgetSingles)
            self.list_display(self.sets_long, self.listWidgetSets)

    def allow_export_results_after_count(self):
        if self.listWidgetSingles.count() > 0 or len(self.labelResult.text()) > 0:
            self.exportResults.setDisabled(False)

    def show_about_IzzyCounter(self):
        self.second_window.show()

    def export_to_file(self):
        self.make_dir_if_not_exist(self.directory, self.report_dir)
        report_file = open(f'{self.directory}/{self.report_dir}/{self.current_date}.txt', 'w')
        FileContent.add_date(report_file, self.current_date, '\n\n')
        FileContent.add_count_result(report_file, self.count_result, '\n\n')
        FileContent.add_label(report_file, self.labelPhotographed, '\n')
        FileContent.add_list_view(report_file, self.list_format(self.singles_long), '\n\n')
        if self.listWidgetSets.count() > 0:
            FileContent.add_label(report_file, self.labelListSets, '\n')
            FileContent.add_list_view(report_file, self.list_format(self.sets_long), '\n')
        FileContent.close_file(report_file)

    def make_dir_if_not_exist(self, path, dir_name):
        if not os.path.exists(f'{path}/{dir_name}'):
            os.mkdir(f'{path}/{dir_name}')

    def list_format(self, some_list):
        return [(x + '\n') for x in some_list]

    def list_display(self, list, widget):
        for num, item in enumerate(list):
            widget.insertItem(num, item)

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = IzzyCounterWindow()
    app.setWindowIcon(QtGui.QIcon('app_logo.png'))
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
