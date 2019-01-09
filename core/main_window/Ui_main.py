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
        self.main_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setObjectName("main_splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_splitter)
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
        self.nc_code_layout.addLayout(self.file_option_layout)
        self.compiler_layout = QtWidgets.QHBoxLayout()
        self.compiler_layout.setObjectName("compiler_layout")
        self.re_compiler = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.re_compiler.setObjectName("re_compiler")
        self.compiler_layout.addWidget(self.re_compiler)
        self.nc_compile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/merge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nc_compile.setIcon(icon3)
        self.nc_compile.setObjectName("nc_compile")
        self.compiler_layout.addWidget(self.nc_compile)
        self.nc_code_layout.addLayout(self.compiler_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.trapezoid_option = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.trapezoid_option.setObjectName("trapezoid_option")
        self.horizontalLayout.addWidget(self.trapezoid_option)
        self.s_shape_option = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.s_shape_option.setChecked(True)
        self.s_shape_option.setObjectName("s_shape_option")
        self.horizontalLayout.addWidget(self.s_shape_option)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nc_code_layout.addLayout(self.horizontalLayout)
        self.chart_tab_widget = QtWidgets.QTabWidget(self.main_splitter)
        self.chart_tab_widget.setObjectName("chart_tab_widget")
        self.s_tab = QtWidgets.QWidget()
        self.s_tab.setObjectName("s_tab")
        self.s_layout = QtWidgets.QVBoxLayout(self.s_tab)
        self.s_layout.setObjectName("s_layout")
        self.chart_tab_widget.addTab(self.s_tab, "")
        self.v_tab = QtWidgets.QWidget()
        self.v_tab.setObjectName("v_tab")
        self.v_layout = QtWidgets.QVBoxLayout(self.v_tab)
        self.v_layout.setObjectName("v_layout")
        self.chart_tab_widget.addTab(self.v_tab, "")
        self.a_tab = QtWidgets.QWidget()
        self.a_tab.setObjectName("a_tab")
        self.a_layout = QtWidgets.QVBoxLayout(self.a_tab)
        self.a_layout.setObjectName("a_layout")
        self.chart_tab_widget.addTab(self.a_tab, "")
        self.jerk_tab = QtWidgets.QWidget()
        self.jerk_tab.setObjectName("jerk_tab")
        self.j_layout = QtWidgets.QVBoxLayout(self.jerk_tab)
        self.j_layout.setObjectName("j_layout")
        self.chart_tab_widget.addTab(self.jerk_tab, "")
        self.verticalLayout.addWidget(self.main_splitter)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Motion Control Simulator"))
        self.nc_load_button.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.nc_save_button.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.trapezoid_option.setText(_translate("MainWindow", "Trapezoid planning"))
        self.s_shape_option.setText(_translate("MainWindow", "S Shape planning"))
        self.chart_tab_widget.setTabText(self.chart_tab_widget.indexOf(self.s_tab), _translate("MainWindow", "Position"))
        self.chart_tab_widget.setTabText(self.chart_tab_widget.indexOf(self.v_tab), _translate("MainWindow", "Velocity"))
        self.chart_tab_widget.setTabText(self.chart_tab_widget.indexOf(self.a_tab), _translate("MainWindow", "Accelerate"))
        self.chart_tab_widget.setTabText(self.chart_tab_widget.indexOf(self.jerk_tab), _translate("MainWindow", "Jerk"))

import icons_rc
