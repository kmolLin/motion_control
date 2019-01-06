# -*- coding: utf-8 -*-

from typing import Sequence
from pylab import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from core.QtModules import (
    Qt,
    QAbstractItemView,
    QRect,
    QImage,
    QPixmap,
    QCursor,
    QTableWidget,
    QHeaderView,
    QStyleOptionHeader,
    QStyle,
)


def _math_tex_to_qpixmap(math_tex: str, fs: int):
    # set up a mpl figure instance
    fig = Figure()
    fig.patch.set_facecolor('none')
    fig.set_canvas(FigureCanvasAgg(fig))
    renderer = fig.canvas.get_renderer()

    # plot the math_tex expression
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.patch.set_facecolor('none')
    t = ax.text(0, 0, math_tex, ha='left', va='bottom', fontsize=fs)

    # fit figure size to text artist
    f_width, f_height = fig.get_size_inches()
    fig_bbox = fig.get_window_extent(renderer)
    text_bbox = t.get_window_extent(renderer)
    tight_fwidth = text_bbox.width * f_width / fig_bbox.width
    tight_fheight = text_bbox.height * f_height / fig_bbox.height
    fig.set_size_inches(tight_fwidth, tight_fheight)

    # convert mpl figure to QPixmap
    buf, size = fig.canvas.print_to_buffer()

    return QPixmap(QImage.rgbSwapped(QImage(buf, size[0], size[1], QImage.Format_ARGB32)))


class MathTableWidget(QTableWidget):

    def __init__(self, header_labels: Sequence[str], font_size: int, parent=None):
        super(MathTableWidget, self).__init__(parent)
        self.setColumnCount(len(header_labels))
        self.setHorizontalHeader(_MathHeader(header_labels, font_size, self))
        self.verticalHeader().setStretchLastSection(True)
        self.setHorizontalHeaderLabels(header_labels)
        self.setAlternatingRowColors(True)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)


class _MathHeader(QHeaderView):

    def __init__(self, header_labels: Sequence[str], font_size: int, parent):
        super(_MathHeader, self).__init__(Qt.Horizontal, parent)
        self.setSectionsClickable(True)
        self.setStretchLastSection(True)
        self.setSectionResizeMode(QHeaderView.Stretch)
        self.pixmaps = []
        index = 0
        for label in header_labels:
            self.pixmaps.append(_math_tex_to_qpixmap(label, font_size))
            index += 1

    def paintSection(self, painter, rect, logical_index):
        if not rect.isValid():
            return

        opt = QStyleOptionHeader()
        self.initStyleOption(opt)
        opt.rect = rect
        opt.section = logical_index
        opt.text = ""

        mouse_pos = self.mapFromGlobal(QCursor.pos())
        if rect.contains(mouse_pos):
            opt.state |= QStyle.State_MouseOver

        painter.save()
        self.style().drawControl(QStyle.CE_Header, opt, painter, self)
        painter.restore()

        pixmap = self.pixmaps[logical_index]

        xpix = (rect.width() - pixmap.size().width()) / 2. + rect.x()
        ypix = (rect.height() - pixmap.size().height()) / 2.

        rect = QRect(xpix, ypix, pixmap.size().width(), pixmap.size().height())
        painter.drawPixmap(rect, pixmap)

    def sizeHint(self):
        base_size = QHeaderView.sizeHint(self)

        base_height = base_size.height()
        if len(self.pixmaps):
            for pixmap in self.pixmaps:
                base_height = max(pixmap.height() + 8, base_height)
        base_size.setHeight(base_height)

        self.parentWidget().repaint()

        return base_size
