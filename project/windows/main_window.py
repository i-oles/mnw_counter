from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os

from project.ui.ui_main_window import Ui_MainWindow
from project.core.file_exporter import FileExporter, REPORT_DIR_NAME
from project.core.mnw_provider import MNWProvider

LOGO_FILENAME = "app_logo.png"
RESOURCES_PATH = "resources"
APP_NAME = "MNW Provider"
TIFF_EXT = "tiff"
JPG_EXT = "jpg"

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.signatures_sets = []
        self.signatures_single = []
        self.setupUi(self)
        self.center_on_screen()
        self.init_ui()
        self.setup_connections()

    def center_on_screen(self) -> None:
        geometry = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        geometry.moveCenter(center)
        self.move(geometry.topLeft())

    def init_ui(self) -> None:
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(os.path.join(RESOURCES_PATH, LOGO_FILENAME)))

        self.cBoxList.setChecked(True)
        self.cBoxCount.setChecked(True)
        self.cBoxTiff.setChecked(True)
        self.btnCount.setDisabled(True)
        self.exportResults.setDisabled(True)

    def setup_connections(self) -> None:
        self.cBoxTiff.stateChanged.connect(self.uncheck_other_ext)
        self.cBoxJpg.stateChanged.connect(self.uncheck_other_ext)
        self.lineEdit.textChanged.connect(lambda: self.btnCount.setDisabled(len(self.lineEdit.text()) == 0))
        self.btnBrowse.clicked.connect(self.browse_folder)
        self.btnCount.clicked.connect(self.on_count_clicked)
        self.exportResults.triggered.connect(self.export_results)

    def uncheck_other_ext(self, state: int) -> None:
        if state == Qt.Checked:
            if self.sender() == self.cBoxTiff:
                self.cBoxJpg.setChecked(False)
            else:
                self.cBoxTiff.setChecked(False)

    def browse_folder(self) -> None:
        directory = QFileDialog.getExistingDirectory(self, "Choose Directory")
        if directory:
            self.lineEdit.setText(directory)

    def on_count_clicked(self) -> None:
        self.progressBar.setValue(0)
        self.labelResult.clear()
        self.listWidgetSingles.clear()
        self.listWidgetSets.clear()

        directory = self.lineEdit.text()
        if not os.path.isdir(directory):
            return self.show_message("Invalid directory path.")

        if not (self.cBoxTiff.isChecked() or self.cBoxJpg.isChecked()):
            return self.show_message("Please select a file extension.")

        if not (self.cBoxList.isChecked() or self.cBoxCount.isChecked()):
            return self.show_message("Please select a display option.")

        file_ext = TIFF_EXT if self.cBoxTiff.isChecked() else JPG_EXT
        provider = MNWProvider(directory, file_ext)
        self.signatures_single, self.signatures_sets = provider.provide_objects_lists()

        for i in range(101):
            self.progressBar.setValue(i)

        if self.cBoxCount.isChecked():
            self.labelResult.setText(str(len(self.signatures_single)))

        if self.cBoxList.isChecked():
            self.listWidgetSingles.addItems(self.signatures_single)
            self.listWidgetSets.addItems(self.signatures_sets)

        self.exportResults.setDisabled(False)

    def export_results(self) -> None:
        exporter = FileExporter(
            self.lineEdit.text(),
            self.labelResult.text(),
            self.signatures_single,
            self.signatures_sets
        )
        exporter.generate_report()
        self.show_message(f"Results exported to '{REPORT_DIR_NAME}'.")

    def show_message(self, text: str) -> None:
        QMessageBox.information(self, "Info", text)
