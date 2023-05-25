"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QtCore.QSettings("MyDataCard")

        self.initUI()
        self.loadData()
        self.initSignals()

    def initUI(self):
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.plainTextEdit)
        self.setLayout(layout)

    def loadData(self):
        self.plainTextEdit.setPlainText(self.settings.value("Text", ""))

    def initSignals(self):
        pass

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue("Text", self.plainTextEdit.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

