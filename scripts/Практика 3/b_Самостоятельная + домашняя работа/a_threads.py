"""
Модуль в котором содержаться потоки Qt
"""

import time
import requests
import psutil
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных
        self.delay = None

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            # TODO то устанавливайте значение 1
            self.delay = 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            cpu_value = psutil.cpu_percent()
            # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            ram_value = psutil.virtual_memory().percent

            # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            sys_info = [cpu_value, ram_value]
            self.systemInfoReceived.emit(sys_info)
            # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay
            time.sleep(self.delay)

    def setDelay(self, delay) -> None:
        self.delay = delay


class WeatherHandler(QtCore.QThread):
    # TODO Пропишите сигналы, которые считаете нужными
    started_signal = QtCore.Signal()
    finished_signal = QtCore.Signal()
    result_signal = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = False

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def setStop(self, stop) -> None:
        self.__status = stop

    def run(self) -> None:
        # TODO настройте метод для корректной работы
        self.started_signal.emit()

        while not self.__status:
            # TODO Примерный код ниже
            response = requests.get(self.__api_url)
            data = response.json()
            self.result_signal.emit(data)

            time.sleep(self.__delay)
            self.finished_signal.emit()
