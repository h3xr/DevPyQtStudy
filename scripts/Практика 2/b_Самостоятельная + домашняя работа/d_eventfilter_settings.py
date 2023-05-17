"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from ui.d_eventfilter_settings import Ui_Form

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.initSignals()
        self.ui.dial.installEventFilter(self)

        self.ui.comboBox.addItem("dec")
        self.ui.comboBox.addItem("oct")
        self.ui.comboBox.addItem("hex")
        self.ui.comboBox.addItem("bin")

        self.settings = QtCore.QSettings("MyDialApp")
        self.loadData()

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent):
        if event.type() == QtCore.QEvent.Type.KeyPress:
            key = event.key()
            if key == 43:
                self.ui.dial.setValue(self.ui.dial.value() + 1)
            elif key == 45:
                self.ui.dial.setValue(self.ui.dial.value() - 1)
            print(self.ui.dial.value())
        return super(Window, self).eventFilter(watched, event)

    def initSignals(self):
        self.ui.dial.valueChanged.connect(self.onDialValueChanged)
        self.ui.horizontalSlider.valueChanged.connect(self.onHorizontalSliderValueChanged)
        self.ui.comboBox.currentTextChanged.connect(self.onComboBoxChanged)

    def onDialValueChanged(self):
        self.ui.horizontalSlider.setValue(self.ui.dial.value())
        self.ui.lcdNumber.setDecMode()
        self.ui.lcdNumber.display(self.ui.dial.value())

    def onHorizontalSliderValueChanged(self):
        self.ui.dial.setValue(self.ui.horizontalSlider.value())
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())

    def onComboBoxChanged(self):
        if self.ui.comboBox.currentText() == "dec":
            self.ui.lcdNumber.setDecMode()
        elif self.ui.comboBox.currentText() == "oct":
            self.ui.lcdNumber.setOctMode()
        elif self.ui.comboBox.currentText() == "hex":
            self.ui.lcdNumber.setHexMode()
        elif self.ui.comboBox.currentText() == "bin":
            self.ui.lcdNumber.setBinMode()

    def loadData(self):
        self.ui.lcdNumber.display(self.settings.value("LCDValue", ""))
        self.ui.comboBox.setCurrentText(self.settings.value("Mode", ""))

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue("LCDValue", self.ui.lcdNumber.value())
        self.settings.setValue("Mode", self.ui.comboBox.currentText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
