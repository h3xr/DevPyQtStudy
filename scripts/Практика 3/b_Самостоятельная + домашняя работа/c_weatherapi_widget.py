"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets, QtCore
import a_threads

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.latLineEdit = QtWidgets.QLineEdit()  # Широта
        self.lonLineEdit = QtWidgets.QLineEdit()  # Долгота
        self.delaySpinBox = QtWidgets.QSpinBox()
        self.infoBox = QtWidgets.QPlainTextEdit()
        self.getInfoButton = QtWidgets.QPushButton()
        self.getInfoButton.setText("Получить данные")
        self.delaySpinBox.setValue(10)

        layout_v1 = QtWidgets.QVBoxLayout()
        layout_v1.addWidget(QtWidgets.QLabel("Широта: "))
        layout_v1.addWidget(QtWidgets.QLabel("Долгота: "))

        layout_v2 = QtWidgets.QVBoxLayout()
        layout_v2.addWidget(self.latLineEdit)
        layout_v2.addWidget(self.lonLineEdit)

        layout_h1 = QtWidgets.QHBoxLayout()
        layout_h1.addLayout(layout_v1)
        layout_h1.addLayout(layout_v2)

        layout_h2 = QtWidgets.QHBoxLayout()
        layout_h2.addWidget(QtWidgets.QLabel("Интервал получения данных: "))
        layout_h2.addWidget(self.delaySpinBox)

        layout_v3 = QtWidgets.QVBoxLayout()
        layout_v3.addWidget(QtWidgets.QLabel("Полученные данные: "))
        layout_v3.addWidget(self.infoBox)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_h1)
        layout.addLayout(layout_h2)
        layout.addLayout(layout_v3)
        layout.addWidget(self.getInfoButton)

        self.setLayout(layout)

        self.getInfoButton.clicked.connect(self.onButtonGetInfoClicked)

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