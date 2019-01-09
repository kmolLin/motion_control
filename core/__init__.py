# -*- coding: utf-8 -*-

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from sys import exit
from .QtModules import (
    qVersion,
    QSCINTILLA_VERSION_STR,
    QApplication,
)
from .main_window import MainWindow


def main():
    print(f"Qt Version: {qVersion()}")
    print(f"QScintilla Version: {QSCINTILLA_VERSION_STR}")
    app = QApplication([])
    run = MainWindow()
    run.show()
    exit(app.exec())
