# -*- coding: utf-8 -*-

from core.QtModules import QMainWindow
from .Ui_main import Ui_MainWindow

__all__ = ['MainWindow']


class MainWindow(QMainWindow, Ui_MainWindow):

    """Main window of the program."""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
