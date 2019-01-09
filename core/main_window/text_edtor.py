# -*- coding: utf-8 -*-

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import Tuple
import re
from platform import system
from core.QtModules import (
    Qt,
    pyqtSlot,
    QColor,
    QFont,
    QFontMetrics,
    QsciScintilla,
)


class NCEditor(QsciScintilla):

    """NC code editor."""

    def __init__(self, parent):
        super(NCEditor, self).__init__(parent)

        # Set the default font.
        if system() == "Windows":
            font_name = "Courier New"
        else:
            font_name = "Mono"
        self.font = QFont(font_name)
        self.font.setFixedPitch(True)
        self.font.setPointSize(14)
        self.setFont(self.font)
        self.setMarginsFont(self.font)
        self.setUtf8(True)

        # Margin 0 is used for line numbers.
        font_metrics = QFontMetrics(self.font)
        self.setMarginsFont(self.font)
        self.setMarginWidth(0, font_metrics.width("0000") + 4)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#cccccc"))

        # Current line visible with special background color.
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#ffe4e4"))

        # Don't want to see the horizontal scrollbar at all.
        self.setWrapMode(QsciScintilla.WrapWord)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Keyword indicator [1]
        self.indicatorDefine(QsciScintilla.BoxIndicator, 1)
        self.cursorPositionChanged.connect(self.__catch_word)

    @pyqtSlot(int, int)
    def __catch_word(self, line: int, index: int):
        """Catch and indicate current word."""
        self.__clear_indicator_all(1)
        pos = self.positionFromLineIndex(line, index)
        _, _, word = self.__word_at_pos(pos)
        word = r'\b' + word + r'\b'
        for m in re.finditer(word.encode('utf-8'), self.text().encode('utf-8'), re.IGNORECASE):
            self.fillIndicatorRange(
                *self.lineIndexFromPosition(m.start()),
                *self.lineIndexFromPosition(m.end()),
                1
            )

    def __word_at_pos(self, pos: int) -> Tuple[int, int, str]:
        """Return pos of current word."""
        return (
            self.SendScintilla(QsciScintilla.SCI_WORDSTARTPOSITION, pos, True),
            self.SendScintilla(QsciScintilla.SCI_WORDENDPOSITION, pos, True),
            self.wordAtLineIndex(*self.getCursorPosition())
        )

    def __clear_indicator_all(self, indicator: int):
        """Clear all indicators."""
        self.clearIndicatorRange(0, 0, *self.lineIndexFromPosition(self.length()), indicator)
