import sys, psutil, os, random
from psutil._common import bytes2human
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QColor, QFont, QPainter
from PySide6 import QtWidgets
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice


class MainSlice(QPieSlice):
    def __init__(self, breakdown_series, parent=None):
        super().__init__(parent)

        self.breakdown_series = breakdown_series
        self.name = None

        self.percentageChanged.connect(self.update_label)

    def get_breakdown_series(self):
        return self.breakdown_series

    def set_name(self, name):
        self.name = name

    def name(self):
        return self.name

    @Slot()
    def update_label(self):
        # p = self.percentage() * 100
        self.setLabel(f"{self.name}")


class DonutBreakdownChart(QChart):
    def __init__(self, parent=None):
        super().__init__(QChart.ChartTypeCartesian, parent, Qt.WindowFlags())
        self.main_series = QPieSeries()
        self.main_series.setPieSize(0.7)
        self.addSeries(self.main_series)

    def add_breakdown_series(self, breakdown_series, color):
        font = QFont("Arial", 8)

        # add breakdown series as a slice to center pie
        main_slice = MainSlice(breakdown_series)
        main_slice.set_name(breakdown_series.name())
        main_slice.setValue(breakdown_series.sum())
        self.main_series.append(main_slice)

        # customize the slice
        main_slice.setBrush(color)
        main_slice.setLabelVisible()
        main_slice.setLabelColor(Qt.white)
        main_slice.setLabelPosition(QPieSlice.LabelInsideNormal)

        # position and customize the breakdown series
        breakdown_series.setPieSize(0.7)
        breakdown_series.setHoleSize(0.6)
        breakdown_series.setLabelsVisible()

        for pie_slice in breakdown_series.slices():
            color = QColor(color).lighter(115)
            pie_slice.setBrush(color)
            pie_slice.setLabelFont(font)

        # add the series to the chart
        self.addSeries(breakdown_series)

        # recalculate breakdown donut segments
        self.recalculate_angles()


    def recalculate_angles(self):
        angle = 0
        slices = self.main_series.slices()
        for pie_slice in slices:
            breakdown_series = pie_slice.get_breakdown_series()
            breakdown_series.setPieStartAngle(angle)
            angle += pie_slice.percentage() * 360.0  # full pie is 360.0
            breakdown_series.setPieEndAngle(angle)


class DiskCalculate(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.color = [Qt.red, Qt.darkGreen, Qt.darkBlue, Qt.darkCyan, Qt.darkMagenta, Qt.darkYellow]
        self.DiskCalculateDiskTotal()

    def initUi(self) -> None:
        layout = QtWidgets.QVBoxLayout()
        self.donut_breakdown = DonutBreakdownChart()
        self.donut_breakdown.setAnimationOptions(QChart.AllAnimations)
        self.donut_breakdown.legend().hide()
        self.chart_view = QChartView(self.donut_breakdown)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        layout.addWidget(self.chart_view)
        self.setLayout(layout)

    def DiskCalculateDiskTotal(self):
        for part in psutil.disk_partitions(all=False):
            if os.name == 'nt':
                if 'cdrom' in part.opts or part.fstype == '':
                    continue

            usage = psutil.disk_usage(part.mountpoint)

            series = QPieSeries()
            series.setName(part.device)
            series.append(f"Free {bytes2human(usage.used)}", float(bytes2human(usage.used)[:-1]))
            series.append(f"Used {bytes2human(usage.free)}", float(bytes2human(usage.free)[:-1]))

            self.donut_breakdown.add_breakdown_series(series, random.choice(self.color))


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = DiskCalculate()
    available_geometry = window.screen().availableGeometry()
    size = available_geometry.height() * 0.6
    window.resize(size, size * 0.8)
    window.show()

    sys.exit(app.exec())