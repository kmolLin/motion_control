# -*- coding: utf-8 -*-

"""This module contain all the Qt objects we needed.

Customized class will define below.
"""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import Tuple
from PyQt5.QtCore import (
    pyqtSignal,
    pyqtSlot,
    QCoreApplication,
    QDir,
    QFileInfo,
    QLineF,
    QModelIndex,
    QMutex,
    QMutexLocker,
    QObject,
    QPoint,
    QPointF,
    QRect,
    QRectF,
    QSettings,
    QSize,
    QSizeF,
    QStandardPaths,
    QThread,
    QTimer,
    QUrl,
    Qt,
)
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QAction,
    QApplication,
    QCheckBox,
    QColorDialog,
    QComboBox,
    QDial,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFileDialog,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QHeaderView,
    QInputDialog,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMessageBox,
    QProgressDialog,
    QPushButton,
    QScrollBar,
    QShortcut,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QSplashScreen,
    QStyle,
    QStyleOptionHeader,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QTableWidgetSelectionRange,
    QTextEdit,
    QToolTip,
    QUndoCommand,
    QUndoStack,
    QUndoView,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtGui import (
    QBrush,
    QColor,
    QCursor,
    QDesktopServices,
    QFont,
    QFontMetrics,
    QIcon,
    QImage,
    QKeySequence,
    QPainter,
    QPainterPath,
    QPen,
    QPixmap,
    QPolygonF,
    QTextCursor,
)
from PyQt5.QtChart import (
    QCategoryAxis,
    QChart,
    QChartView,
    QLegend,
    QLineSeries,
    QScatterSeries,
    QValueAxis,
)
from PyQt5.Qsci import QsciScintilla, QSCINTILLA_VERSION_STR
from PyQt5.QtCore import qVersion, PYQT_VERSION_STR

__all__ = [
    'pyqtSignal',
    'pyqtSlot',
    'qt_image_format',
    'qVersion',
    'PYQT_VERSION_STR',
    'QAbstractItemView',
    'QAction',
    'QApplication',
    'QBrush',
    'QCategoryAxis',
    'QChart',
    'QChartView',
    'QCheckBox',
    'QColor',
    'QColorDialog',
    'QComboBox',
    'QCoreApplication',
    'QCursor',
    'QDesktopServices',
    'QDial',
    'QDialog',
    'QDialogButtonBox',
    'QDir',
    'QDoubleSpinBox',
    'QFileDialog',
    'QFileInfo',
    'QFont',
    'QFontMetrics',
    'QGraphicsScene',
    'QGraphicsView',
    'QHBoxLayout',
    'QHeaderView',
    'QIcon',
    'QImage',
    'QInputDialog',
    'QKeySequence',
    'QLabel',
    'QLegend',
    'QLineEdit',
    'QLineF',
    'QLineSeries',
    'QListWidget',
    'QListWidgetItem',
    'QMainWindow',
    'QMenu',
    'QMessageBox',
    'QModelIndex',
    'QMutex',
    'QMutexLocker',
    'QObject',
    'QPainter',
    'QPainterPath',
    'QPen',
    'QPixmap',
    'QPoint',
    'QPointF',
    'QPolygonF',
    'QProgressDialog',
    'QPushButton',
    'QRect',
    'QRectF',
    'QSpacerItem',
    'QScatterSeries',
    'QScrollBar',
    'QSettings',
    'QShortcut',
    'QSize',
    'QSizeF',
    'QSizePolicy',
    'QSpinBox',
    'QSplashScreen',
    'QStandardPaths',
    'QStyle',
    'QStyleOptionHeader',
    'QTabWidget',
    'QTableWidget',
    'QTableWidgetItem',
    'QTableWidgetSelectionRange',
    'QTextCursor',
    'QTextEdit',
    'QThread',
    'QTimer',
    'QToolTip',
    'QUndoCommand',
    'QUndoStack',
    'QUndoView',
    'QUrl',
    'QValueAxis',
    'QVBoxLayout',
    'QWidget',
    'Qt',
    'QsciScintilla',
    'QSCINTILLA_VERSION_STR',
]


qt_image_format: Tuple[str, ...] = (
    "Portable Network Graphics (*.png)",
    "Joint Photographic Experts Group (*.jpg)",
    "Bitmap Image file (*.bmp)",
    "Business Process Model (*.bpm)",
    "Tagged Image File Format (*.tiff)",
    "Windows Icon (*.ico)",
    "Wireless Application Protocol Bitmap (*.wbmp)",
    "X Bitmap (*.xbm)",
    "X Pixmap (*.xpm)",
)
