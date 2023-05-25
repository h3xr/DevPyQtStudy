"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import time

from PySide6 import QtWidgets, QtCore
import requests

class CheckSiteThread(QtCore.QThread):
    started_signal = QtCore.Signal()
    finished_signal = QtCore.Signal()
    status_code_signal = QtCore.Signal(int)
    result = QtCore.Signal(str)

    def __init__(self, parent=None, url="", sleep=3):
        super().__init__(parent)
        self.url = url
        self.sleep = sleep

    def run(self):
        self.started_signal.emit()
        try:
            response = requests.get(self.url)
            status_code = response.status_code
            for val in range(10):
                self.result.emit(str(val))
                time.sleep(0.3)
            time.sleep(self.sleep)
        except requests.exceptions.RequestException:
            status_code = None
        self.status_code_signal.emit(status_code)
        self.finished_signal.emit()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.urlLineEdit = QtWidgets.QLineEdit()
        self.checkButton = QtWidgets.QPushButton("Проверить url")
        self.statusLabel = QtWidgets.QLabel()
        self.textEdit = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("URL"))
        layout.addWidget(self.urlLineEdit)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.checkButton)
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)


        self.thread_site = CheckSiteThread(sleep=5)
        self.thread_site.started_signal.connect(self.onThreadStart)
        self.thread_site.finished_signal.connect(self.onThreadFinish)
        self.thread_site.status_code_signal.connect(self.onThreadStatus)
        self.thread_site.result.connect(self.textEdit.appendPlainText)

        self.checkButton.clicked.connect(self.onClick)
        # self.initSignals()

    def onThreadStart(self):
        self.checkButton.setEnabled(False)
        self.statusLabel.setText("Start")

    def onThreadFinish(self):
        self.checkButton.setEnabled(True)
        # self.statusLabel.setText("Stop")

    def onThreadStatus(self, value):
        if value is None:
            self.statusLabel.setText("Error")
        elif value == 200:
            self.statusLabel.setText("Good 200")
        else:
            self.statusLabel.setText(str(value))

    def onClick(self):
        url = self.urlLineEdit.text()
        self.thread_site.url = url
        self.thread_site.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
