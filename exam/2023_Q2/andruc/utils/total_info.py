import datetime, platform, psutil, cpuinfo
from PySide6 import QtWidgets, QtCore


class TotalInfoFirstTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()


    def initUi(self) -> None:
        self.labelComputerName = QtWidgets.QLabel()
        self.labelComputerName.setText("Computer Name: " + platform.node())
        self.labelOS = QtWidgets.QLabel()
        self.labelOS.setText("Operating System: " + self.platformType())
        self.labelUptime = QtWidgets.QLabel()
        self.labelUptime.setText("System Uptime: " +
                                 str(datetime.datetime.now() -
                                     datetime.datetime.fromtimestamp(psutil.boot_time()))[:8])

        self.labelProcessor = QtWidgets.QLabel()
        my_cpuinfo = cpuinfo.get_cpu_info()
        self.labelProcessor.setText("Full CPU Name: " + my_cpuinfo['brand_raw'])
        self.labelProcessorLogic = QtWidgets.QLabel()
        self.labelProcessorLogic.setText("Processor logic cores: " + str(psutil.cpu_count(logical=True)))
        self.labelProcessorPhysic = QtWidgets.QLabel()
        self.labelProcessorPhysic.setText("Processor physical cores: " + str(psutil.cpu_count(logical=False)))
        self.labelProcessorFrMin = QtWidgets.QLabel()
        self.labelProcessorFrMin.setText("Min CPU frequency: " + str(psutil.cpu_freq().min))
        self.labelProcessorFrMax = QtWidgets.QLabel()
        self.labelProcessorFrMax.setText("Max CPU frequency: " + str(psutil.cpu_freq().max))

        self.labelTotalRAM = QtWidgets.QLabel()
        self.labelTotalRAM.setText(f"Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024: .2f} GB")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.labelComputerName)
        layout.addWidget(self.labelOS)
        layout.addWidget(self.labelUptime)
        layout.addWidget(self.labelProcessor)
        layout.addWidget(self.labelProcessorLogic)
        layout.addWidget(self.labelProcessorFrMin)
        layout.addWidget(self.labelProcessorFrMax)

        layout.addWidget(self.labelTotalRAM)
        self.setLayout(layout)

    def platformType(self):
        if platform.os.name == 'nt':
            self.info = platform.win32_ver()
            self.oslabel = "Windows " + self.info[0] + "  Version: " + self.info[1]
        elif platform.os.name == 'posix':
            self.info = platform.uname()
            self.oslabel = self.info[0] + " Release: " + self.info[2] + " Version: " + self.info[3]
        return self.oslabel


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = TotalInfoFirstTab()
    window.show()

    app.exec()
