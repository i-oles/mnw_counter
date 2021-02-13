from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from PyQt5.QtCore import Qt
from string_operations import StringOperations
from gui import Ui_MainWindow
from about_widget import Ui_widget
import os
import re
import sys
from datetime import date

#todo uncheck count and list cBox
#todo logo
#todo uncheck tiff bug: popup or unable check
#todo center app on screen
#todo correct count method - separate couting from settings


class Ui_AboutWindow(Ui_widget, QMainWindow):
    def __init__(self, parent=None):
        super(Ui_AboutWindow, self).__init__(parent)
        self.setupUi(self)


class IzzyCounterWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(IzzyCounterWindow, self).__init__(parent)
        self.setupUi(self)

        self.component = 'mnw'
        self.char_1 = ','
        self.char_2 = '-'
        self.report_dir = 'Daily_Reports'
        self.tiff_extension = 'tiff'
        self.jpg_extension = 'jpg'

        self.current_date = date.today()
        self.current_date.strftime("%d-%m-%Y")

        self.logo = 'app_logo.jpg'
        self.centralwidget.setWindowIcon(QtGui.QIcon(self.logo))

        self.cBoxList.setChecked(True)
        self.cBoxCount.setChecked(True)
        self.cBoxTiff.setChecked(True)
        self.btnCount.setDisabled(True)
        self.exportResults.setDisabled(True)

        self.cBoxTiff.stateChanged.connect(self.uncheck_another_cBox)
        self.cBoxJpg.stateChanged.connect(self.uncheck_another_cBox)

        self.lineEdit.textChanged.connect(self.unlock_btn_count)

        self.btnBrowse.clicked.connect(self.browse_dir)
        self.btnCount.clicked.connect(self.when_btnCount_clicked)
        self.menuFile.triggered.connect(self.export_to_file)
        self.menuAbout.triggered.connect(self.show_about_IzzyCounter)
        self.second_window = Ui_AboutWindow(self)

        self.menuFile.triggered.connect(
            lambda: self.show_popup(f"Your results was successfully exported to folder '{self.report_dir}' in your images folder"))

    def when_btnCount_clicked(self):
        self.clear_widgets_after_clicked()
        self.check_file_extention(self.tiff_extension, self.jpg_extension)
        self.check_is_lineEdit_empty()
        self.is_manual_path_typing_correct()
        self.boxes_not_checked()
        if self.dir_path_ok:
            self.find_all_ones_from_dir()
            self.make_singles_and_set_list()
            self.counting_progress()
            self.display_count_result()
            self.display_item_lists()
            self.allow_export_results_after_count()

    def display_count_result(self):
        if self.cBoxCount.isChecked():
            self.count_result = str(len(self.singles_long))
            self.labelResult.setText(self.count_result)

    def display_item_lists(self):
        if self.cBoxList.isChecked():
            self.list_display(self.singles_long, self.listWidgetSingles)
            self.list_display(self.sets_long, self.listWidgetSets)

    def show_about_IzzyCounter(self):
        self.second_window.show()

    def unlock_btn_count(self):
        if len(self.lineEdit.text()) > 0:
            self.btnCount.setDisabled(False)

    def browse_dir(self):
        self.directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        self.lineEdit.setText(f'{self.directory}')

    def clear_widgets_after_clicked(self):
        self.progressBar.setValue(0)
        self.labelResult.clear()
        self.listWidgetSingles.clear()
        self.listWidgetSets.clear()

    def is_manual_path_typing_correct(self):
        self.directory = str(self.lineEdit.text())
        self.dir_path_ok = os.path.isdir(self.directory)
        if self.lineEdit.text():
            if not self.dir_path_ok:
                self.show_popup('Path does not exist! Please type or choose correct path!')

    def check_is_lineEdit_empty(self):
        if not self.lineEdit.text():
            self.show_popup('Please choose directory path!')

    def boxes_not_checked(self):
        if not self.cBoxCount.isChecked() and not self.cBoxList.isChecked():
            self.show_popup('Please choose one of the following display options')

    def allow_export_results_after_count(self):
        if self.listWidgetSingles.count() > 0 or len(self.labelResult.text()) > 0:
            self.exportResults.setDisabled(False)

    def uncheck_another_cBox(self, state):
        if state == Qt.Checked:
            if self.sender() == self.cBoxTiff:
                self.cBoxJpg.setChecked(False)
            else:
                self.cBoxTiff.setChecked(False)

    def check_file_extention(self, ext_1, ext_2):
        if self.cBoxTiff.isChecked():
            self.file_ext = ext_1
        else:
            self.file_ext = ext_2

    def show_popup(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()

    def find_all_ones_from_dir(self):
        self.ones_all = []
        self.regex_search = f'.*\(0?1\)\.{self.file_ext}?$'
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

    def export_to_file(self):
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = IzzyCounterWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
