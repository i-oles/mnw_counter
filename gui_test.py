# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(365, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelListSingles = QtWidgets.QLabel(self.centralwidget)
        self.labelListSingles.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelListSingles.setObjectName("labelListSingles")
        self.gridLayout.addWidget(self.labelListSingles, 7, 0, 1, 1)
        self.cBoxList = QtWidgets.QCheckBox(self.centralwidget)
        self.cBoxList.setObjectName("cBoxList")
        self.gridLayout.addWidget(self.cBoxList, 3, 0, 1, 1)
        self.listWidgetSingles = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetSingles.setMinimumSize(QtCore.QSize(0, 200))
        self.listWidgetSingles.setObjectName("listWidgetSingles")
        self.gridLayout.addWidget(self.listWidgetSingles, 7, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)
        self.cBoxCount = QtWidgets.QCheckBox(self.centralwidget)
        self.cBoxCount.setObjectName("cBoxCount")
        self.gridLayout.addWidget(self.cBoxCount, 2, 0, 1, 1)
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.gridLayout.addWidget(self.labelResult, 6, 1, 1, 1)
        self.btnBrowse = QtWidgets.QToolButton(self.centralwidget)
        self.btnBrowse.setMinimumSize(QtCore.QSize(50, 0))
        self.btnBrowse.setMaximumSize(QtCore.QSize(50, 21))
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout.addWidget(self.btnBrowse, 1, 2, 1, 1)
        self.listWidgetSets = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetSets.setMinimumSize(QtCore.QSize(0, 160))
        self.listWidgetSets.setMaximumSize(QtCore.QSize(16777215, 160))
        self.listWidgetSets.setObjectName("listWidgetSets")
        self.gridLayout.addWidget(self.listWidgetSets, 9, 1, 1, 2)
        self.labelListSets = QtWidgets.QLabel(self.centralwidget)
        self.labelListSets.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelListSets.setObjectName("labelListSets")
        self.gridLayout.addWidget(self.labelListSets, 9, 0, 1, 1)
        self.labelChoose = QtWidgets.QLabel(self.centralwidget)
        self.labelChoose.setObjectName("labelChoose")
        self.gridLayout.addWidget(self.labelChoose, 0, 0, 1, 3)
        self.labelPhotographed = QtWidgets.QLabel(self.centralwidget)
        self.labelPhotographed.setObjectName("labelPhotographed")
        self.gridLayout.addWidget(self.labelPhotographed, 6, 0, 1, 1)
        self.btnCount = QtWidgets.QPushButton(self.centralwidget)
        self.btnCount.setMinimumSize(QtCore.QSize(0, 50))
        self.btnCount.setObjectName("btnCount")
        self.gridLayout.addWidget(self.btnCount, 4, 0, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "IzzyCounter"))
        self.labelListSingles.setText(_translate("MainWindow", "List of objects:"))
        self.cBoxList.setText(_translate("MainWindow", "display objects list"))
        self.cBoxCount.setText(_translate("MainWindow", "display counting result"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
