"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""
import time

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()

    def initUi(self):
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.pushButtonMirror = QtWidgets.QPushButton("Mirror")

        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()

        layout1.addWidget(self.lineEditInput)
        layout1.addWidget(self.lineEditMirror)
        layout2.addLayout(layout1)
        layout2.addWidget(self.pushButtonMirror)

        self.setLayout(layout2)
        self.initSignals()

    def event(self, event: QtCore.QEvent) -> bool:
        print(time.ctime(), event)
        return super().event(event)

    def initSignals(self):
        self.pushButtonMirror.clicked.connect(self.invertData)
        #self.lineEditInput.textChanged.connect(lambda x: self.lineEditMirror.setText(x[::-1]))

    @QtCore.Slot()
    def invertData(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
