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
        self.screen_width = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        self.screen_height = QtWidgets.QApplication.screenAt(self.pos()).size().height()

        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonPositionCenter)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonPositionLB)
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonPositionLT)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonPositionRB)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonPositionRT)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonPositionXY)
        self.ui.spinBoxX.valueChanged.connect(self.onSpinBoxXValue)
        self.ui.spinBoxY.valueChanged.connect(self.onSpinBoxYValue)

    def onPushButtonGetDataClicked(self) -> None:
        screens_count = QtWidgets.QApplication.screens()
        self.ui.plainTextEdit.appendPlainText("-" * 30) 
        self.ui.plainTextEdit.appendPlainText(time.ctime())
        self.ui.plainTextEdit.appendPlainText("Количество мониторов: " +
                                              str(len(screens_count)))
        self.ui.plainTextEdit.appendPlainText("Название основного окна: " +
                                              QtWidgets.QApplication.primaryScreen().name())
        for screen in screens_count:
            self.ui.plainTextEdit.appendPlainText("Разрешение экрана: " + screen.name() + ": " +
                                                  "Ширина - " + str(screen.size().width()) +
                                                  " Высота - " + str(screen.size().height()))

        self.ui.plainTextEdit.appendPlainText("Ширина текущего окна: " +
                                              str(self.window().frameGeometry().width()))
        self.ui.plainTextEdit.appendPlainText("Высота текущего окна: " +
                                              str(self.window().frameGeometry().height()))
        self.ui.plainTextEdit.appendPlainText("Окно находится на экране: " +
                                              str(QtWidgets.QApplication.screenAt(self.pos()).name()))
        self.ui.plainTextEdit.appendPlainText("Минимальные размеры окна: " +
                                              "Ширина - " + str(self.window().minimumWidth()) +
                                              " Высота - " + str(self.window().minimumHeight()))
        self.ui.plainTextEdit.appendPlainText("Текущее положение: " +
                                              "x = " + str(self.pos().x()) +
                                              " y = " + str(self.pos().y()))
        self.ui.plainTextEdit.appendPlainText("Центр приложения: " +
                                              "x = " + str(self.pos().x() + self.width()/2) +
                                              " y = " + str(self.pos().y() + self.height()/2))
        self.ui.plainTextEdit.appendPlainText("-" * 30)

    def onPushButtonPositionCenter(self):
        self.move(int(self.screen_width/2 - self.width()/2),
                  int(self.screen_height/2 - self.height()/2))

    def onPushButtonPositionLB(self):
        self.move(0, self.screen_height - self.height())

    def onPushButtonPositionLT(self):
        self.move(0, 0)

    def onPushButtonPositionRB(self):
        self.move(self.screen_width - self.width(), self.screen_height - self.height())

    def onPushButtonPositionRT(self):
        self.move(self.screen_width - self.width(), 0)

    def onPushButtonPositionXY(self):
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(time.ctime() + " - отображение окна")

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        self.ui.plainTextEdit.appendPlainText(time.ctime() + " - сворачивание окна")

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print("x = " + str(event.pos().x()) + " y = " + str(event.pos().y()))

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        print("w = " + str(event.size().width()) + " h = " + str(event.size().height()))

    def onSpinBoxXValue(self):
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def onSpinBoxYValue(self):
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
