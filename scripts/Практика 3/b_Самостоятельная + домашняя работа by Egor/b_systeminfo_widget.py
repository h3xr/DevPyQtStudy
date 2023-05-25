"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads
Создавать форму можно как в ручную, так и с помощью программы Designer
Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets
from PySide6 import QtGui
from UI.widget import Ui_Demo_Form
from a_threads import SystemInfo


class SystemInfoWindow(QtWidgets.QWidget, Ui_Demo_Form, SystemInfo):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initSignals()

        self.counter = 0

        self.lcdNumber.setSmallDecimalPoint(10)
        self.lcdNumber.setFocus()

    def initSignals(self):
        self.pushButton_start.clicked.connect(self.startThread)
        self.pushButton_stop.clicked.connect(self.stopThread)

    def startThread(self):
        self.thread_system = SystemInfo()
        self.thread_system.systemInfoReceived.connect(self.setProgressBarValue)

        self.thread_system.finished.connect(self.finishThread)

        self.pushButton_start.setEnabled(False)
        self.textEdit_text.setText("The thread is running...")

        self.thread_system.delay = self.lcdNumber.value()

        self.thread_system.start()

    def setProgressBarValue(self, data):
        self.progressBar_cpu.setValue(data[0])
        self.progressBar_ram.setValue(data[1])

    def stopThread(self):
        self.thread_system.stop()
        self.thread_system.wait()

        self.pushButton_start.setEnabled(True)

    def finishThread(self):
        self.textEdit_text.setText("The thread stopped")

        self.pushButton_start.setEnabled(True)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if event.key() == QtGui.Qt.Key_Plus:
            self.counter += 0.1
            self.lcdNumber.display(self.counter)
        elif event.key() == QtGui.Qt.Key_Minus:
            self.counter -= 0.1
            self.lcdNumber.display(self.counter)


if __name__=="__main__":
    app = QtWidgets.QApplication()
    app.setStyle('Fusion')

    window = SystemInfoWindow()
    window.show()

    app.exec()