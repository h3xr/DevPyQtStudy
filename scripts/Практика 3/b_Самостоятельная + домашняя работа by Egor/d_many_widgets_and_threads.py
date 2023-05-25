"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""

from PySide6 import QtWidgets, QtGui, QtCore
from b_systeminfo_widget import SystemInfoWindow
from c_weatherapi_widget import WeatherInfo

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.app1 = SystemInfoWindow(self.centralwidget)
        self.app2 = WeatherInfo(self.centralwidget)
        self.horizontalLayout.addWidget(self.app1)
        self.horizontalLayout.addWidget(self.app2)
        self.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    main_window = MainWindow()
    main_window.show()

    app.exec()
