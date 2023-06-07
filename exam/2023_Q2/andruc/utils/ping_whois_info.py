import socket, validators, platform, requests
from PySide6 import QtCore, QtWidgets


class GetWhois(QtCore.QThread):
    started_signal = QtCore.Signal()
    finished_signal = QtCore.Signal()
    result_signal = QtCore.Signal(dict)

    def __init__(self, host, parent=None):
        super().__init__(parent)

        self.host = f"http://ipwho.is/{host}"
        self.__status = False

    def run(self) -> None:
        self.started_signal.emit()
        while not self.__status:
            response = requests.get(self.host)
            whois_info = response.json()
            self.result_signal.emit(whois_info)
            if response.status_code:
                self.setStop(True)
            self.finished_signal.emit()

    def setStop(self, stop) -> None:
        self.__status = stop

class PingAndWHOISTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ip = None
        self.process = None
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:

        self.labelHost = QtWidgets.QLabel()
        self.labelHost.setText("Host: ")

        self.lineEditHost = QtWidgets.QLineEdit()
        self.lineEditHost.setPlaceholderText("Example: 8.8.8.8")

        self.buttonPing = QtWidgets.QPushButton()
        self.buttonPing.setText("PING")

        self.buttonWHOIS = QtWidgets.QPushButton()
        self.buttonWHOIS.setText("WHOIS")

        self.infoBox = QtWidgets.QPlainTextEdit()
        self.infoBox.setReadOnly(True)

        layout_h = QtWidgets.QHBoxLayout()
        layout_h.addWidget(self.labelHost)
        layout_h.addWidget(self.lineEditHost)
        layout_h.addWidget(self.buttonPing)
        layout_h.addWidget(self.buttonWHOIS)

        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_h)
        layout.addWidget(self.infoBox)

        self.setLayout(layout)

    def initSignals(self) -> None:
        self.buttonPing.clicked.connect(self.onButtonPingClicked)
        self.buttonWHOIS.clicked.connect(self.onButtonWHOISClicked)

    def onButtonPingClicked(self):
        if self.lineEditHost.text() and self.buttonPing.text() == "PING":
            self.ip = self.hostCheck(self.lineEditHost.text())
            if self.ip:
                self.infoBox.clear()
                if self.process is None:
                    self.buttonPing.setText("STOP")
                    self.buttonWHOIS.setEnabled(False)
                    self.lineEditHost.setEnabled(False)

                    self.process = QtCore.QProcess()
                    self.process.readyReadStandardOutput.connect(self.handleOutput)
                    self.process.readyReadStandardError.connect(self.handleError)
                    self.process.finished.connect(self.processFinished)
                    self.process.start("ping", [f"{self.ip}"])

        elif self.buttonPing.text() == "STOP":
            self.process = 1
            self.buttonWHOIS.setEnabled(True)
            self.lineEditHost.setEnabled(True)
            self.buttonPing.setText("PING")

        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Host empty! Fill the form!")
            msg.exec()

    def handleError(self) -> None:
        data = self.process.readAllStandardError()
        if platform.os.name == 'posix':
            stdout = bytes(data).decode("utf8")
            self.infoBox.appendPlainText(stdout.rstrip('\n'))
        elif platform.os.name == 'nt':
            stdout = bytes(data).decode('cp866')
            self.infoBox.appendPlainText(stdout.rstrip('\r\n'))

    def handleOutput(self) -> None:
        data = self.process.readAllStandardOutput()
        # stdout = bytes(data).decode("utf8")
        # stdout = bytes(data).decode('cp866')

        if platform.os.name == 'posix':
            stdout = bytes(data).decode("utf8")
            self.infoBox.appendPlainText(stdout.rstrip('\n'))
        elif platform.os.name == 'nt':
            stdout = bytes(data).decode('cp866')
            self.infoBox.appendPlainText(stdout.rstrip('\r\n'))

        # print(sys.getdefaultencoding())
        # print(repr(stdout))

    def processFinished(self) -> None:
        self.process = None

    def onButtonWHOISClicked(self):
        if self.lineEditHost.text():
            self.ip = self.hostCheck(self.lineEditHost.text())
            if self.ip:
                self.whois_info_get = GetWhois(self.ip)
                self.whois_info_get.started_signal.connect(self.onWHOISStarted)
                self.whois_info_get.result_signal.connect(self.onWHOISResult)
                self.whois_info_get.start()
                self.whois_info_get.exit()
                self.whois_info_get.finished_signal.connect(self.onWHOISStop)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Host empty! Fill the form!")
            msg.exec()

    def hostCheck(self, host):
        try:
            validators.url(host)
            return socket.gethostbyname(host)
        except socket.gaierror as e:
            msg = QtWidgets.QMessageBox()
            msg.setText("Invalid hostname!")
            msg.exec()

    def onWHOISStarted(self):
        self.buttonPing.setEnabled(False)
        self.buttonWHOIS.setEnabled(False)
        self.lineEditHost.setEnabled(False)

    def onWHOISStop(self):
        self.buttonPing.setEnabled(True)
        self.buttonWHOIS.setEnabled(True)
        self.lineEditHost.setEnabled(True)

    def onWHOISResult(self, data):
        self.infoBox.clear()
        log = self.infoBox.appendPlainText

        log(f"IP: {data['ip']}")
        log(f"Type: {data['type']}")
        log(f"Continent: {data['continent']}")
        log(f"Country: {data['country']}")
        log(f"Region: {data['region']}")
        log(f"City: {data['city']}")
        log(f"Latitude: {data['latitude']}")
        log(f"Longitude: {data['longitude']}")
        log(f"ASN: {data['connection']['asn']}")
        log(f"Organization: {data['connection']['org']}")
        log(f"ISP: {data['connection']['isp']}")
        log(f"Domain: {data['connection']['domain']}")
        log(f"Current time: {data['timezone']['current_time']}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = PingAndWHOISTab()
    window.show()

    app.exec()
