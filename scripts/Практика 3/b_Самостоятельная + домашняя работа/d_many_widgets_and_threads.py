"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets, QtCore
import a_threads

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initThreads()
        self.initUi()
        self.initSignals()

    def initUi(self):
        self.delaySystemInfoSpinBox = QtWidgets.QSpinBox()
        self.delaySystemInfoSpinBox.setValue(1)
        self.cpuProgressBar = QtWidgets.QProgressBar()
        self.ramProgressBar = QtWidgets.QProgressBar()
        self.cpuProgressBar.setMinimum(0)
        self.cpuProgressBar.setMaximum(100)
        self.cpuProgressBar.setMinimum(0)
        self.ramProgressBar.setMaximum(100)

        layout_system_monitor_h = QtWidgets.QHBoxLayout()
        layout_system_monitor_h.addWidget(QtWidgets.QLabel("Интервал обновления данных: "))
        layout_system_monitor_h.addWidget(self.delaySystemInfoSpinBox)

        layout_system_monitor = QtWidgets.QVBoxLayout()
        layout_system_monitor.addLayout(layout_system_monitor_h)
        layout_system_monitor.addWidget(QtWidgets.QLabel("CPU"))
        layout_system_monitor.addWidget(self.cpuProgressBar)
        layout_system_monitor.addWidget(QtWidgets.QLabel("RAM"))
        layout_system_monitor.addWidget(self.ramProgressBar)

        self.latLineEdit = QtWidgets.QLineEdit()  # Широта
        self.lonLineEdit = QtWidgets.QLineEdit()  # Долгота
        self.delaySpinBox = QtWidgets.QSpinBox()
        self.infoBox = QtWidgets.QPlainTextEdit()
        self.getInfoButton = QtWidgets.QPushButton()
        self.getInfoButton.setText("Получить данные")
        self.delaySpinBox.setValue(10)

        layout_weather_v1 = QtWidgets.QVBoxLayout()
        layout_weather_v1.addWidget(QtWidgets.QLabel("Широта: "))
        layout_weather_v1.addWidget(QtWidgets.QLabel("Долгота: "))

        layout_weather_v2 = QtWidgets.QVBoxLayout()
        layout_weather_v2.addWidget(self.latLineEdit)
        layout_weather_v2.addWidget(self.lonLineEdit)

        layout_weather_h1 = QtWidgets.QHBoxLayout()
        layout_weather_h1.addLayout(layout_weather_v1)
        layout_weather_h1.addLayout(layout_weather_v2)

        layout_weather_h2 = QtWidgets.QHBoxLayout()
        layout_weather_h2.addWidget(QtWidgets.QLabel("Интервал получения данных: "))
        layout_weather_h2.addWidget(self.delaySpinBox)

        layout_weather_v3 = QtWidgets.QVBoxLayout()
        layout_weather_v3.addWidget(QtWidgets.QLabel("Полученные данные: "))
        layout_weather_v3.addWidget(self.infoBox)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_system_monitor)
        layout.addLayout(layout_weather_h1)
        layout.addLayout(layout_weather_h2)
        layout.addLayout(layout_weather_v3)
        layout.addWidget(self.getInfoButton)

        self.setLayout(layout)

    def initThreads(self):
        self.system_info = a_threads.SystemInfo()
        self.system_info.start()
    def initSignals(self):
        self.delaySystemInfoSpinBox.valueChanged.connect(self.onDelayLineEditChanged)
        self.system_info.systemInfoReceived.connect(self.onSystemInfoView)
        self.getInfoButton.clicked.connect(self.onButtonGetInfoClicked)

    def onSystemInfoView(self, value):
        self.cpuProgressBar.setValue(value[0])
        self.ramProgressBar.setValue(value[1])

    def onDelayLineEditChanged(self):
        self.system_info.setDelay(int(self.delaySystemInfoSpinBox.text()))

    def onButtonGetInfoClicked(self):
        if self.getInfoButton.text() == "Получить данные":
            if not self.latLineEdit.text() and not self.lonLineEdit.text():
                msg = QtWidgets.QMessageBox()
                msg.setText("Поля широты и долготы должны быть заполнены!")
                msg.exec()
            else:
                self.weatherinfo_get = a_threads.WeatherHandler(self.latLineEdit.text(), self.lonLineEdit.text())
                self.weatherinfo_get.setDelay(self.delaySpinBox.value())
                self.weatherinfo_get.started_signal.connect(self.onWeatherInfoStarted)
                self.weatherinfo_get.result_signal.connect(self.onWeatherInfoView)
                self.weatherinfo_get.start()

        elif self.getInfoButton.text() == "Остановить":
            self.weatherinfo_get.setStop(True)
            self.weatherinfo_get.exit()
            self.weatherinfo_get.finished_signal.connect(self.onWeatherInfoFinished)

    def onWeatherInfoStarted(self):
        self.latLineEdit.setEnabled(False)
        self.lonLineEdit.setEnabled(False)
        self.delaySpinBox.setEnabled(False)
        self.getInfoButton.setText("Остановить")

    def onWeatherInfoFinished(self):
        print("we are here")
        self.latLineEdit.setEnabled(True)
        self.lonLineEdit.setEnabled(True)
        self.delaySpinBox.setEnabled(True)
        self.getInfoButton.setText("Получить данные")

    def onWeatherInfoView(self, data):
        self.infoBox.appendPlainText(f"Интервал обновления: {self.delaySpinBox.value()} сек")
        self.infoBox.appendPlainText(f"Широта: {data['latitude']}")
        self.infoBox.appendPlainText(f"Долгота: {data['longitude']}")
        self.infoBox.appendPlainText(f"Время прогноза: {data['current_weather']['time']}")
        self.infoBox.appendPlainText(f"Временная зона: {data['timezone']}")
        self.infoBox.appendPlainText(f"Температура: {data['current_weather']['temperature']}")
        self.infoBox.appendPlainText(f"Скорость ветра: {data['current_weather']['windspeed']}")
        self.infoBox.appendPlainText("=" * 15)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()