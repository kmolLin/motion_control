# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(True)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/motor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.nc_code_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.nc_code_layout.setContentsMargins(0, 0, 0, 0)
        self.nc_code_layout.setObjectName("nc_code_layout")
        self.file_option_layout = QtWidgets.QHBoxLayout()
        self.file_option_layout.setObjectName("file_option_layout")
        self.nc_file_path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nc_file_path.setObjectName("nc_file_path")
        self.file_option_layout.addWidget(self.nc_file_path)
        self.nc_load_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/load_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nc_load_button.setIcon(icon1)
        self.nc_load_button.setObjectName("nc_load_button")
        self.file_option_layout.addWidget(self.nc_load_button)
        self.nc_save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/save_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nc_save_button.setIcon(icon2)
        self.nc_save_button.setObjectName("nc_save_button")
        self.file_option_layout.addWidget(self.nc_save_button)
        self.nc_compile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nc_compile.setIcon(icon3)
        self.nc_compile.setObjectName("nc_compile")
        self.file_option_layout.addWidget(self.nc_compile)
        self.nc_code_layout.addLayout(self.file_option_layout)
        self.chart_tab_widget = QtWidgets.QTabWidget(self.splitter)
        self.chart_tab_widget.setObjectName("chart_tab_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.chart_tab_widget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.chart_tab_widget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Motion control"))
        self.nc_load_button.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.nc_save_button.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.chart_tab_widget.setTabText(self.chart_tab_widget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.chart_tab_widget.setTabText(self.chart_tab_widget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

import icons_rc
