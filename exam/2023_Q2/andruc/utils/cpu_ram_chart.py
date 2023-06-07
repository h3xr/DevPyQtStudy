from PySide6 import QtCore, QtWidgets, QtCharts, QtGui
import time, psutil


class SystemInfoCPURAM(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self) -> None:
        while True:
            cpu_value = psutil.cpu_percent()
            ram_value = psutil.virtual_memory().percent
            sys_info = [cpu_value, ram_value]
            self.systemInfoReceived.emit(sys_info)
            time.sleep(0.1)

class ChartViewCPURAM(QtCharts.QChartView, QtCharts.QChart):
    def __init__(self, *args, **kwargs):
        super(ChartViewCPURAM, self).__init__(*args, **kwargs)
        self.resize(700, 200)
        self.setRenderHint(QtGui.QPainter.Antialiasing)  # Anti-aliasing
        self.chart_init()

        self.system_info = SystemInfoCPURAM()
        self.system_info.systemInfoReceived.connect(self.drawLine)
        self.system_info.start()

    def chart_init(self):
        self.chart = QtCharts.QChart()
        self.series_cpu = QtCharts.QSplineSeries()
        self.series_ram = QtCharts.QSplineSeries()

        self.chart.setTitle("CPU | RAM Usage Graph")
        #self.series.setName("CPU Usage Graph")
        self.series_cpu.setColor(QtCore.Qt.red)
        self.series_ram.setColor(QtCore.Qt.blue)
        self.series_cpu.setName("CPU Usage")
        self.series_ram.setName("RAM Usage")

        self.chart.addSeries(self.series_cpu)
        self.chart.addSeries(self.series_ram)

        # Set Legend
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        # Declare and initialize X axis, Y axis
        self.dtaxisX = QtCharts.QDateTimeAxis()
        self.vl_cpu_axisY = QtCharts.QValueAxis()
        self.vl_ram_axisY = QtCharts.QValueAxis()
        self.vl_cpu_axisY.setLinePenColor(QtGui.QColor(QtCore.Qt.red))
        self.vl_ram_axisY.setLinePenColor(QtGui.QColor(QtCore.Qt.blue))

        # Set the coordinate axis display range
        self.vl_cpu_axisY.setMin(0)
        self.vl_cpu_axisY.setMax(100)
        self.vl_cpu_axisY.setLabelFormat("%d")

        self.vl_ram_axisY.setMin(0)
        self.vl_ram_axisY.setMax(100)
        self.vl_ram_axisY.setLabelFormat("%d")

        # Set X-axis time style
        self.dtaxisX.setFormat("hh:mm:ss")

        # Set the grid points on the coordinate axis
        self.dtaxisX.setTickCount(1)
        self.vl_cpu_axisY.setTickCount(5)
        self.vl_ram_axisY.setTickCount(5)

        # Set the axis name
        self.vl_cpu_axisY.setTitleText("CPU | RAM Usage %")

        # Set the grid not to display
        self.vl_cpu_axisY.setGridLineVisible(True)

        # Add the coordinate axis to the chart
        self.chart.addAxis(self.dtaxisX, QtCore.Qt.AlignBottom)
        self.chart.addAxis(self.vl_cpu_axisY, QtCore.Qt.AlignLeft)
        self.chart.addAxis(self.vl_ram_axisY, QtCore.Qt.AlignRight)

        # Associate the curve to the coordinate axis
        self.series_cpu.attachAxis(self.dtaxisX)
        self.series_cpu.attachAxis(self.vl_cpu_axisY)

        self.series_ram.attachAxis(self.dtaxisX)
        self.series_ram.attachAxis(self.vl_ram_axisY)

        self.setChart(self.chart)

    def drawLine(self, value):
        # Get the current time
        cur_time = QtCore.QDateTime.currentDateTime()
        # Update X coordinate
        self.dtaxisX.setMin(QtCore.QDateTime.currentDateTime().addSecs(-60))
        self.dtaxisX.setMax(QtCore.QDateTime.currentDateTime().addSecs(0))

        # When the point on the curve exceeds the range of the X axis, remove the oldest point
        if self.series_cpu.count() > 600:
            self.series_cpu.removePoints(0, self.series_cpu.count() - 600)
            self.series_ram.removePoints(0, self.series_ram.count() - 600)

        # Add data to the end of the curve
        # print(cur_time.toMSecsSinceEpoch())

        # Error
        # Python int too large to convert to C long
        # Need to convert into float(cur_time.toMSecsSinceEpoch())

        self.series_cpu.append(float(cur_time.toMSecsSinceEpoch()), value[0])
        self.series_ram.append(float(cur_time.toMSecsSinceEpoch()), value[1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    view = ChartViewCPURAM()
    view.show()
    app.exec()