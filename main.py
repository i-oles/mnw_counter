from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt
from mnw_provider import MNWProvider
from file_exporter import FileExporter, REPORT_DIR_NAME
from gui import Ui_MainWindow
import os
import sys


class IzzyCounterWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(IzzyCounterWindow, self).__init__(parent)
        self.sets_long = None
        self.singles_long = None
        self.setupUi(self)
        self.center_on_screen()

        self.tiff_ext = 'tiff'
        self.jpg_ext = 'jpg'

        # default settings
        self.cBoxList.setChecked(True)
        self.cBoxCount.setChecked(True)
        self.cBoxTiff.setChecked(True)
        self.btnCount.setDisabled(True)
        self.exportResults.setDisabled(True)

        # widgets connections
        self.cBoxTiff.stateChanged.connect(self.uncheck_another_cBox)
        self.cBoxJpg.stateChanged.connect(self.uncheck_another_cBox)
        self.lineEdit.textChanged.connect(self.unlock_btn_count)
        self.btnBrowse.clicked.connect(self.set_dir_path_in_lineEdit)
        self.btnCount.clicked.connect(self.when_btnCount_clicked)
        self.menuFile.triggered.connect(self.export_to_file)
        self.menuFile.triggered.connect(
            lambda: self.show_popup(
                f"Your results was successfully exported to folder '{REPORT_DIR_NAME}' in your images folder"))

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
        self.check_file_extension(self.tiff_ext, self.jpg_ext)
        self.check_is_empty(self.lineEdit, self.show_popup, 'Please choose directory path!')
        self.is_manual_path_ok()
        if self.dir_path_ok:
            self.when_all_cBox_unchecked(self.cBoxTiff, self.cBoxJpg, self.show_popup, 'Please choose file extension!')
            if self.cBoxJpg.isChecked() or self.cBoxTiff.isChecked():
                self.when_all_cBox_unchecked(self.cBoxCount, self.cBoxList, self.show_popup,
                                             'Please choose display option!')
                if self.dir_path_ok and (self.cBoxCount.isChecked() or self.cBoxList.isChecked()):
                    provider = MNWProvider(self.directory_path, self.file_ext)
                    self.singles_long, self.sets_long = provider.provide_objects_lists()
                    self.counting_progress()
                    self.display_count_result()
                    self.display_item_lists()
                    self.allow_export_results()

    def clear_widgets_after_clicked(self):
        self.progressBar.setValue(0)
        self.labelResult.clear()
        self.listWidgetSingles.clear()
        self.listWidgetSets.clear()

    def check_file_extension(self, ext_1, ext_2):
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
