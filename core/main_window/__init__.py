# -*- coding: utf-8 -*-

from typing import Sequence
from core.nc import DEFAULT_NC_SYNTAX
from core.trapezoid import graph_chart
from core.QtModules import (
    Qt,
    pyqtSlot,
    QStandardPaths,
    QMainWindow,
    QFileDialog,
    QFileInfo,
    QDoubleSpinBox,
    QChart,
    QChartView,
    QLineSeries,
    QPainter,
)
from .math_table import MathTableWidget
from .text_edtor import NCEditor
from .Ui_main import Ui_MainWindow

__all__ = ['MainWindow']


def str_between(s: str, front: str, back: str) -> str:
    """Get from parenthesis."""
    return s[(s.find(front) + 1):s.find(back)]


def _spinbox(value: float) -> QDoubleSpinBox:
    s = QDoubleSpinBox()
    s.setMaximum(10000)
    s.setValue(value)
    return s


class MainWindow(QMainWindow, Ui_MainWindow):

    """Main window of the program."""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.nc_editor = NCEditor(self)
        self.nc_code_layout.addWidget(self.nc_editor)
        self.parameter_table = MathTableWidget([
            r"$a$",
            r"$b$",
            r"$\zeta$",
            r"$\omega_n$",
        ], 15, self)
        self.parameter_table.verticalHeader().hide()
        self.parameter_table.setRowCount(1)
        self.parameter_table.setFixedHeight(60)
        self.parameter_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.parameter_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i, v in enumerate([1., 20., 0.707, 1000.]):
            self.parameter_table.setCellWidget(0, i, _spinbox(v))
        self.nc_code_layout.insertWidget(1, self.parameter_table)

        self.env = ""
        self.file_name = ""
        self.set_locate(QStandardPaths.writableLocation(QStandardPaths.DesktopLocation))

        # Default RE compiler.
        self.re_compiler.setPlaceholderText(DEFAULT_NC_SYNTAX)

        # Chart widgets.
        self.charts = [QChart() for _ in range(6)]
        for chart, layout in zip(self.charts, [self.s_layout, self.v_layout, self.a_layout] * 2):
            chart.setTheme(QChart.ChartThemeBlueIcy)
            view = QChartView(chart)
            view.setRenderHint(QPainter.Antialiasing)
            layout.addWidget(view)

    def output_to(self, format_name: str, format_choose: Sequence[str]) -> str:
        """Simple to support multiple format."""
        file_name, suffix = QFileDialog.getSaveFileName(
            self,
            f"Save to {format_name}...",
            self.env + '/Untitled',
            ';;'.join(format_choose)
        )
        if file_name:
            suffix = str_between(suffix, '(', ')').split('*')[-1]
            print(f"Format: {suffix}")
            if QFileInfo(file_name).completeSuffix() != suffix[1:]:
                file_name += suffix
        return file_name

    def input_from(self, format_name: str, format_choose: Sequence[str]) -> str:
        """Get file name(s)."""
        file_name_s, suffix = QFileDialog.getOpenFileName(
            self,
            f"Open {format_name} file...",
            self.env,
            ';;'.join(format_choose)
        )
        if file_name_s:
            suffix = str_between(suffix, '(', ')').split('*')[-1]
            print(f"Format: {suffix}")
            self.set_locate(QFileInfo(file_name_s).absolutePath())
            self.set_file_name(file_name_s)
        return file_name_s

    def set_locate(self, locate: str):
        """Set environment variables."""
        if locate == self.env:
            # If no changed.
            return
        self.env = locate
        print(f"~Set workplace to: [\"{self.env}\"]")

    def set_file_name(self, new_name: str):
        """Set default file name."""
        self.file_name = new_name

    def dragEnterEvent(self, event):
        """Drag file in to our window."""
        mime_data = event.mimeData()
        if not mime_data.hasUrls():
            return
        for url in mime_data.urls():
            suffix = QFileInfo(url.toLocalFile()).completeSuffix()
            if suffix in {'nc', 'g'}:
                event.acceptProposedAction()

    def dropEvent(self, event):
        """Drop file in to our window."""
        file_name = event.mimeData().urls()[-1].toLocalFile()
        self.__load_nc_code(file_name)
        event.acceptProposedAction()

    @pyqtSlot(name='on_nc_load_button_clicked')
    def __load_nc_code(self, file_name: str = ""):
        if not file_name:
            file_name = self.input_from("NC code", [
                "Numerical Control programming language (*.nc)",
                "Preparatory code (*.g)",
            ])
            if not file_name:
                return

        self.nc_file_path.setText(file_name)
        with open(file_name, 'r', encoding='utf-8') as f:
            self.nc_editor.setText(f.read())

    @pyqtSlot(name='on_nc_save_button_clicked')
    def __save_nc_code(self):
        """Save current NC code."""
        if self.nc_file_path.text() != self.file_name or not self.file_name:
            file_name = self.output_to("NC code", [
                "Numerical control programming language (*.nc)",
                "Preparatory code (*.g)",
            ])
            if not file_name:
                return

            self.file_name = file_name

        with open(self.file_name, 'w', encoding='utf-8') as f:
            f.write(self.nc_editor.text())

    @pyqtSlot(name='on_nc_compile_clicked')
    def __nc_compile(self):
        """Compile NC code."""
        self.__clear_charts()

        lines = []
        for name in [
            "Position",
            "Velocity",
            "Accelerate",
            "XY Position (mm)",
            "XY Velocity (mm/s)",
            "XY Accelerate (mm/s^2)",
        ]:
            line = QLineSeries()
            line.setName(name)
            lines.append(line)

        i = 0.
        syntax = self.re_compiler.text() or self.re_compiler.placeholderText()
        for tp in graph_chart(self.nc_editor.text(), syntax):
            for s, v, a, (sx, sy), (vx, vy), (ax, ay) in tp.iter(tp.s, tp.v, tp.a, tp.s_xy, tp.v_xy, tp.a_xy):
                lines[0].append(i, s)
                lines[1].append(i, v)
                lines[2].append(i, a)
                lines[3].append(sx, sy)
                lines[4].append(vx, vy)
                lines[5].append(ax, ay)
                i += tp.t_s
        for line, chart in zip(lines, self.charts):
            chart.addSeries(line)
        self.__reset_axis()

    def __clear_charts(self):
        """Clear all charts."""
        for chart in self.charts:
            chart.removeAllSeries()
            for axis in chart.axes():
                chart.removeAxis(axis)

    def __reset_axis(self):
        """Reset all axis of charts."""
        for chart, x_axis, y_axis in zip(
            self.charts,
            ["Time (s)"] * 3 + ["X"] * 3,
            ["Position (mm)", "Velocity (mm/s)", "Accelerate (mm/s^2)"] + ["Y"] * 3,
        ):
            chart.createDefaultAxes()
            chart.axisX().setTitleText(x_axis)
            chart.axisY().setTitleText(y_axis)
