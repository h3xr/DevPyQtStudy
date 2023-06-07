from PySide6 import QtCore, QtGui, QtWidgets
import psutil, time


class ProcessesTableThread(QtCore.QThread):
    processesTableSignal = QtCore.Signal(list)
    sortTableSignal = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.sort_row = 0
        self.sort_type = None
        self.sort_row_dict = {0: 'pid', 1: 'name', 2: 'status', 3: 'cpu_percent', 4: 'memory_percent'}

    def run(self) -> None:
        while True:
            self.listOfProcessNames = list()
            # Iterate over all running processes
            for proc in psutil.process_iter():
                # Get process detail as dictionary
                self.pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'status', 'memory_percent'])
                self.listOfProcessNames.append(self.pInfoDict)
            self.sortStart()
            self.processesTableSignal.emit(self.listOfProcessNames)
            time.sleep(1)

    def setSortRow(self, sort_row) -> None:
        self.sort_row = sort_row
        if self.sort_type is None or self.sort_type == 1:
            self.sort_type = 2
        else:
            self.sort_type = 1

        self.sortStart()
        self.processesTableSignal.emit(self.listOfProcessNames)

    def sortStart(self):
        if self.sort_type == 1 or self.sort_type is None:
            self.listOfProcessNames.sort(key=lambda element: element[self.sort_row_dict[self.sort_row]])
        elif self.sort_type == 2:
            self.listOfProcessNames.sort(key=lambda element: element[self.sort_row_dict[self.sort_row]], reverse=True)

class ProcessesTable(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initTableModel()
        self.initUi()

    def initUi(self) -> None:
        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.tableModel)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableView.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.tableView.verticalHeader().setVisible(False)

        # Read Only
        self.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tableView)

        self.setLayout(layout)

        self.processes_table = ProcessesTableThread()
        self.processes_table.sortTableSignal.connect(self.onHeaderClickedSort)
        self.processes_table.processesTableSignal.connect(self.drawTable)

        self.processes_table.start()

        #self.tableView.setSortingEnabled(False)
        self.tableView.horizontalHeader().sectionClicked.connect(self.onHeaderClickedSort)

    def onHeaderClickedSort(self, logicalIndex):
        self.processes_table.setSortRow(logicalIndex)

    def initTableModel(self) -> None:
        self.tableModel = QtGui.QStandardItemModel()
        self.tableModel.setHorizontalHeaderLabels(['PID', 'NAME', 'STATUS', 'CPU USAGE %', 'RAM USAGE %'])

    def drawTable(self, value):
        self.tableModel.removeRows(0, self.tableModel.rowCount())
        for pr in value:
            item1 = QtGui.QStandardItem(str(pr['pid']))
            item1.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item2 = QtGui.QStandardItem(str(pr['name']))
            item3 = QtGui.QStandardItem(str(pr['status']))
            item3.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item4 = QtGui.QStandardItem(str(pr['cpu_percent']))
            item4.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            item5 = QtGui.QStandardItem(str(round(pr['memory_percent'], 1)))
            item5.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

            self.tableModel.appendRow([item1, item2, item3, item4, item5])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = ProcessesTable()
    window.show()

    app.exec()