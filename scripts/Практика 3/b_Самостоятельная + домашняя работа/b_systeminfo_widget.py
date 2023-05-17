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
from PySide6 import QtWidgets, QtCore
import a_threads

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.delaySystemInfoSpinBox = QtWidgets.QSpinBox()
        self.cpuProgressBar = QtWidgets.QProgressBar()
        self.ramProgressBar = QtWidgets.QProgressBar()
        self.cpuProgressBar.setMinimum(0)
        self.cpuProgressBar.setMaximum(100)
        self.cpuProgressBar.setMinimum(0)
        self.ramProgressBar.setMaximum(100)

        layout_system_monitor_h = QtWidgets.QHBoxLayout()
        layout_system_monitor_h.addWidget(QtWidgets.QLabel("Задержка обновления"))
        layout_system_monitor_h.addWidget(self.delaySystemInfoSpinBox)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_system_monitor_h)
        layout.addWidget(QtWidgets.QLabel("CPU"))
        layout.addWidget(self.cpuProgressBar)
        layout.addWidget(QtWidgets.QLabel("RAM"))
        layout.addWidget(self.ramProgressBar)

        self.setLayout(layout)

        self.system_info = a_threads.SystemInfo()
        self.system_info.systemInfoReceived.connect(self.onSystemInfoView)
        self.system_info.start()

        self.delaySystemInfoSpinBox.valueChanged.connect(self.onDelayLineEditChanged)

    def onSystemInfoView(self, value):
        self.cpuProgressBar.setValue(value[0])
        self.ramProgressBar.setValue(value[1])

    def onDelayLineEditChanged(self):
        self.system_info.setDelay(int(self.delaySystemInfoSpinBox.text()))



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()