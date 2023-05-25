"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads
Создавать форму можно как в ручную, так и с помощью программы Designer
Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""

from PySide6 import QtWidgets
from UI.widget_weather import Ui_Form
from a_threads import WeatherHandler
import time


class WeatherInfo(QtWidgets.QWidget, Ui_Form, WeatherHandler):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initSignals()

        self.doubleSpinBox_lat.setRange(-100, 100)
        self.doubleSpinBox_lon.setRange(-100, 100)

    def initSignals(self):
        self.pushButton_start.clicked.connect(self.startThreadWeather)
        self.pushButton_stop.clicked.connect(self.stopThreadWeather)

    def startThreadWeather(self):
        self.thread_weather = WeatherHandler(self.doubleSpinBox_lat.value(), self.doubleSpinBox_lon.value())
        self.thread_weather.weatherInfoReceived.connect(self.getWeatherData)

        self.thread_weather.finished.connect(self.finishThread)

        self.pushButton_start.setEnabled(False)

        self.thread_weather.setDelay(self.doubleSpinBox_sleep.value())

        self.thread_weather.start()

    def getWeatherData(self, data: dict):
        self.textEdit_info.append(f"Updated: {time.ctime()}\n{str(data)}")

    def stopThreadWeather(self):
        self.thread_weather.stop()
        self.thread_weather.wait()

        self.pushButton_start.setEnabled(True)

    def finishThread(self):
        self.textEdit_info.setText("The thread stopped")

        self.pushButton_start.setEnabled(True)


if __name__=="__main__":
    app = QtWidgets.QApplication()
    app.setStyle('Fusion')

    weatherWindow = WeatherInfo()
    weatherWindow.show()

    app.exec()