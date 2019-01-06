# -*- coding: utf-8 -*-

from sys import exit
from .QtModules import QApplication
from .main_window import MainWindow


def main():
    app = QApplication([])
    run = MainWindow()
    run.show()
    exit(app.exec())
