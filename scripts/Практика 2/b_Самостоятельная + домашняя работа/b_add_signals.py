import random

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        # comboBox -----------------------------------------------------------
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItem("Элемент 1")
        self.comboBox.addItem("Элемент 2")
        self.comboBox.addItems(["Элемент 3", "Элемент 4", "Элемент 5"])
        self.comboBox.insertItem(0, "")

        self.pushButtonComboBox = QtWidgets.QPushButton("Получить данные")

        layoutComboBox = QtWidgets.QHBoxLayout()
        layoutComboBox.addWidget(self.comboBox)
        layoutComboBox.addWidget(self.pushButtonComboBox)

        # lineEdit -----------------------------------------------------------
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите текст")

        self.pushButtonLineEdit = QtWidgets.QPushButton("Получить данные")

        layoutLineEdit = QtWidgets.QHBoxLayout()
        layoutLineEdit.addWidget(self.lineEdit)
        layoutLineEdit.addWidget(self.pushButtonLineEdit)

        # textEdit -----------------------------------------------------------
        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setPlaceholderText("Введите текст")

        self.pushButtonTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutTextEdit = QtWidgets.QHBoxLayout()
        layoutTextEdit.addWidget(self.textEdit)
        layoutTextEdit.addWidget(self.pushButtonTextEdit)

        # plainTextEdit ------------------------------------------------------
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlaceholderText("Введите текст")

        self.pushButtonPlainTextEdit = QtWidgets.QPushButton("Получить данные")

        layoutPlainTextEdit = QtWidgets.QHBoxLayout()
        layoutPlainTextEdit.addWidget(self.plainTextEdit)
        layoutPlainTextEdit.addWidget(self.pushButtonPlainTextEdit)

        # spinBox ------------------------------------------------------------
        self.spinBox = QtWidgets.QSpinBox()
        self.spinBox.setValue(random.randint(-50, 50))

        self.pushButtonSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutSpinBox = QtWidgets.QHBoxLayout()
        layoutSpinBox.addWidget(self.spinBox)
        layoutSpinBox.addWidget(self.pushButtonSpinBox)

        # doubleSpinBox ------------------------------------------------------
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.doubleSpinBox.setValue(random.randint(-50, 50))

        self.pushButtonDoubleSpinBox = QtWidgets.QPushButton("Получить данные")

        layoutDoubleSpinBox = QtWidgets.QHBoxLayout()
        layoutDoubleSpinBox.addWidget(self.doubleSpinBox)
        layoutDoubleSpinBox.addWidget(self.pushButtonDoubleSpinBox)

        # timeEdit -----------------------------------------------------------
        self.timeEdit = QtWidgets.QTimeEdit()
        self.timeEdit.setTime(QtCore.QTime.currentTime().addSecs(random.randint(-10000, 10000)))

        self.pushButtonTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutTimeEdit = QtWidgets.QHBoxLayout()
        layoutTimeEdit.addWidget(self.timeEdit)
        layoutTimeEdit.addWidget(self.pushButtonTimeEdit)

        # dateTimeEdit -------------------------------------------------------
        self.dateTimeEdit = QtWidgets.QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime().addDays(random.randint(-10, 10)))

        self.pushButtonDateTimeEdit = QtWidgets.QPushButton("Получить данные")

        layoutDateTimeEdit = QtWidgets.QHBoxLayout()
        layoutDateTimeEdit.addWidget(self.dateTimeEdit)
        layoutDateTimeEdit.addWidget(self.pushButtonDateTimeEdit)

        # plainTextEditLog ---------------------------------------------------
        self.plainTextEditLog = QtWidgets.QPlainTextEdit()

        self.pushButtonClearLog = QtWidgets.QPushButton("Очистить лог")

        layoutLog = QtWidgets.QHBoxLayout()
        layoutLog.addWidget(self.plainTextEditLog)
        layoutLog.addWidget(self.pushButtonClearLog)

        # main layout

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutComboBox)
        layoutMain.addLayout(layoutLineEdit)
        layoutMain.addLayout(layoutTextEdit)
        layoutMain.addLayout(layoutPlainTextEdit)
        layoutMain.addLayout(layoutSpinBox)
        layoutMain.addLayout(layoutDoubleSpinBox)
        layoutMain.addLayout(layoutTimeEdit)
        layoutMain.addLayout(layoutDateTimeEdit)
        layoutMain.addLayout(layoutLog)

        self.setLayout(layoutMain)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """
        # TODO подключить слот для вывода текста из comboBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonComboBox.clicked.connect(self.onPushButtonComboBoxClicked)
        self.pushButtonLineEdit.clicked.connect(self.onPushButtonLineEditClicked)

        # TODO подключить слот для вывода текста из textEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonTextEdit.clicked.connect(self.onPushButtonTextEditClicked)

        # TODO подключить слот для вывода текста из plainTextEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonPlainTextEdit.clicked.connect(self.onPushButtonPlainTextEditClicked)

        # TODO подключить слот для вывода значения из spinBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonSpinBox.clicked.connect(self.onPushButtonSpinBoxClicked)

        # TODO подключить слот для вывода значения из doubleSpinBox в plainTextEditLog при нажатии на кнопку
        self.pushButtonDoubleSpinBox.clicked.connect(self.onPushButtonDoubleSpinBoxClicked)

        # TODO подключить слот для вывода времени из timeEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonTimeEdit.clicked.connect(self.onPushButtonTimeEditClicked)

        # TODO подключить слот для вывода времени из dateTimeEdit в plainTextEditLog при нажатии на кнопку
        self.pushButtonDateTimeEdit.clicked.connect(self.onPushButtonDateTimeEditClicked)

        # TODO подключить слот для очистки plainTextEditLog при нажатии на кнопку
        self.pushButtonClearLog.clicked.connect(self.onPushButtonClearLogClicked)

        # TODO подключить слот для вывода текста в plainTextEditLog при изменении выбранного элемента в comboBox
        self.comboBox.currentIndexChanged.connect(self.onCurrentIndexChanged)

        # TODO подключить слот для вывода значения в plainTextEditLog при изменении значения в spinBox
        self.spinBox.valueChanged.connect(self.onSpinBoxValueChanged)

        # TODO подключить слот для вывода даты и времени в plainTextEditLog при изменении в dateTimeEdit
        self.dateTimeEdit.dateTimeChanged.connect(self.onDateTimeEditChange)

        # slots --------------------------------------------------------------
    def onPushButtonLineEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLineEdit

        :return: None
        """

        self.plainTextEditLog.setPlainText(self.lineEdit.text())

    # TODO Самостоятельная реализация слотов для сигналов
    def onPushButtonComboBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonComboBox

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.comboBox.currentText())

    def onPushButtonTextEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonTextEdit

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.textEdit.toPlainText())

    def onPushButtonPlainTextEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonPlainTextEdit

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.plainTextEdit.toPlainText())

    def onPushButtonSpinBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonSpinBox

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.spinBox.text())

    def onPushButtonDoubleSpinBoxClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonDoubleSpinBoxClicked

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.doubleSpinBox.text())

    def onPushButtonTimeEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonTimeEditClicked

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.timeEdit.text())

    def onPushButtonDateTimeEditClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonDateTimeEditClicked

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.dateTimeEdit.text())

    def onPushButtonClearLogClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonClearLogClicked

        :return: None
        """
        self.plainTextEditLog.clear()

    def onCurrentIndexChanged(self) -> None:
        """
        Обработка сигнала clicked для кнопки comboBox.currentIndexChanged

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.comboBox.currentText())

    def onSpinBoxValueChanged(self) -> None:
        """
        Обработка сигнала clicked для кнопки spinBox.currentValueChanged

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.spinBox.text())

    def onDateTimeEditChange(self) -> None:
        """
        Обработка сигнала clicked для кнопки dateTimeEditChange

        :return: None
        """
        self.plainTextEditLog.setPlainText(self.dateTimeEdit.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
