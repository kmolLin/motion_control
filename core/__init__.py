# -*- coding: utf-8 -*-

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
