"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtGui, QtCore
from time import ctime

from ui.c_signals_events import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initSignals()



    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)

    def onPushButtonGetDataClicked(self) -> None:
        self.ui.plainTextEdit.setPlainText(time.ctime())
        self.ui.plainTextEdit.appendPlainText("Количество мониторов: " +
                                              str(len(QtWidgets.QApplication.screens())))
        self.ui.plainTextEdit.appendPlainText("Название текущего окна: " +
                                              self.window().windowTitle())

        self.ui.plainTextEdit.appendPlainText("Ширина текущего окна: " +
                                              str(self.window().frameGeometry().width()))
        self.ui.plainTextEdit.appendPlainText("Высота текущего окна: " +
                                              str(self.window().frameGeometry().height()))


        l# QtCore.QSize.width()

        print()



    # * Разрешение экрана
    # * На каком экране окно находится
    # * Размеры окна



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
