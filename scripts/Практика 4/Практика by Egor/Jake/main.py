from PySide6 import QtWidgets

from widget import Ui_MainWindow  # Импортируем класс формы


class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.setUrl)

    def setUrl(self):
        self.ui.webEngineView.setUrl("https://" + self.ui.lineEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()