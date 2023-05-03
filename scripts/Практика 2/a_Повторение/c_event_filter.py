"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

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
        self.lable = QtWidgets.QLabel("Текст")
        self.lable.installEventFilter(self)
        self.lable.setTextFormat(QtCore.Qt.RichText)
        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()

        layout1.addWidget(self.lineEditInput)
        layout1.addWidget(self.lineEditMirror)
        layout2.addLayout(layout1)
        layout2.addWidget(self.pushButtonMirror)
        layout2.addWidget(self.lable)
        self.pushButtonMirror.installEventFilter(self)

        self.setLayout(layout2)
        self.initSignals()

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.pushButtonMirror and event.type() == QtCore.QEvent.Type.Enter:
            self.lineEditMirror.setText("1st Form")
        if watched == self.lable and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.lable.setText('<span style=" color:#ff0000;">Красивый </span><span style=" color:#0000ff;">текст</span>')

        return super(Window, self).eventFilter(watched, event)

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
