"""
Модуль в котором содержаться потоки Qt
"""

import time
import requests
import psutil
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None, delay=None):
        super().__init__(parent)
        self.delay = delay  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных
        self.running = True

    def run(self):
        self.runLoop()
        self.stop()

    def stop(self):
         self.running = False

    def runLoop(self):              # TODO переопределить метод run
        if self.delay == 0:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        count = 0
        while self.running and count < 20:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            data = [cpu_value, ram_value]
            self.systemInfoReceived.emit(data)  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            print(data)

            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay

            count += 1

        print("Поток завершен")


class WeatherHandler(QtCore.QThread):
    weatherInfoReceived = QtCore.Signal(dict)  # TODO Пропишите сигналы, которые считаете нужными

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)
        self.lat = lat
        self.lon = lon

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

        self.running = True

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта
        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self):
        self.runLoop()
        self.stop()

    def stop(self):
        self.running = False

    def runLoop(self):
        if self.__delay == 0:
            self.__delay = 10

        count = 0
        while self.running and count < 20:
            response = requests.get(self.__api_url)
            data = response.json()
            self.weatherInfoReceived.emit(data)
            print(f"Status Code: {response.status_code}")
            time.sleep(self.__delay)

            count += 1

        print("Поток завершен")
