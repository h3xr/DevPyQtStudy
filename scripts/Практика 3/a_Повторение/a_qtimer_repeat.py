"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore
import time as time_

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initTimers()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.labelTime = QtWidgets.QLabel()
        self.labelTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox = QtWidgets.QSpinBox()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.labelTime)
        layout.addWidget(self.spinBox)
        layout.addWidget(QtWidgets.QPlainTextEdit())

        self.setLayout(layout)
        self.value = 0
        self.showTime()

    def initTimers(self) -> None:
        """
        Инициализация таймеров

        :return: None
        """

        self.timeTimer = QtCore.QTimer()
        self.timeTimer.setInterval(1000)
        self.timeTimer.start()

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.timeTimer.timeout.connect(self.showTime)
        self.spinBox.valueChanged.connect(self.changeTimeout)

    def showTime(self) -> None:
        """
        Слот для отображения в labelTime текущего времени

        :return: None
        """

        time = QtCore.QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.labelTime.setText(timeDisplay)
        time_.sleep(3)
        # self.value += 1
        # self.labelTime.setText(str(self.value))

    def changeTimeout(self, value) -> None:
        self.timeTimer.setInterval(value * 10)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
