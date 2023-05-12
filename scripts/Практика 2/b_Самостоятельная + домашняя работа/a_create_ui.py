from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # TODO Вызовите метод для инициализации интерфейса
        self.initUi()

    def initUi(self) -> None:
        """
        Инициализация интерфейса

        :return: None
        """

        # TODO Создайте виджет QLabel с текстом "Логин"
        labelLogin = QtWidgets.QLabel("Логин")
        # TODO Создайте виджет QLabel с текстом "Регистрация"
        labelRegistration = QtWidgets.QLabel("Регистрация")

        # TODO создайте виджет QLineEdit
        self.lineEditLogin = QtWidgets.QLineEdit()

        # TODO добавьте placeholderText "Введите логин" с помощью метода .setPlaceholderText()
        self.lineEditLogin.setPlaceholderText("Введите логин")

        # TODO создайте виджет QLineEdit
        self.lineEditPassword = QtWidgets.QLineEdit()
        # TODO добавьте placeholderText "Введите пароль"
        self.lineEditPassword.setPlaceholderText("Введите пароль")

        # TODO установите ограничение видимости вводимых знаков с помощью метода .setEchoMode()
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.NoEcho)

        # TODO создайте виджет QPushButton
        self.pushButtonLogin = QtWidgets.QPushButton()

        # TODO установите текст "Войти" с помощью метода setText()
        self.pushButtonLogin.setText("Войти")

        # TODO создайте виджет QPushButton
        self.pushButtonRegistration = QtWidgets.QPushButton()
        # TODO установите текст "Регистрация" с помощью метода setText()
        self.pushButtonRegistration.setText("Регистрация")

        # TODO Создайте QHBoxLayout
        layoutLogin = QtWidgets.QHBoxLayout()
        # TODO с помощью метода .addWidget() добавьте labelLogin
        layoutLogin.addWidget(labelLogin)
        # TODO с помощью метода .addWidget() добавьте self.lineEditLogin
        layoutLogin.addWidget(self.lineEditLogin)

        # TODO Создайте QHBoxLayout
        layoutPassword = QtWidgets.QHBoxLayout()
        # TODO с помощью метода .addWidget() добавьте labelRegistration
        layoutPassword.addWidget(labelRegistration)
        # TODO с помощью метода .addWidget() добавьте self.lineEditPassword
        layoutPassword .addWidget(self.lineEditPassword)

        # TODO Создайте QHBoxLayout
        layoutButtons = QtWidgets.QHBoxLayout()
        # TODO с помощью метода .addWidget() добавьте self.pushButtonLogin
        layoutButtons.addWidget(self.pushButtonLogin)
        # TODO с помощью метода .addWidget() добавьте self.pushButtonRegistration
        layoutButtons.addWidget(self.pushButtonRegistration)

        # TODO Создайте QVBoxLayout
        layoutMain = QtWidgets.QVBoxLayout()
        # TODO с помощью метода .addLayout() добавьте layoutLogin
        layoutMain.addLayout(layoutLogin)
        # TODO с помощью метода .addLayout() добавьте layoutPassword
        layoutMain.addLayout(layoutPassword)
        # TODO с помощью метода .addLayout() добавьте layoutButtons
        layoutMain.addLayout(layoutButtons)

        # TODO с помощью метода setLayout установите layoutMain на основной виджет
        self.setLayout(layoutMain)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
