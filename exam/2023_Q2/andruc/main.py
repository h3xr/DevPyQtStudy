from PySide6 import QtWidgets, QtCore
from utils.cpu_ram_chart import ChartViewCPURAM
from utils.processes_table_view import ProcessesTable
from utils.total_info import TotalInfoFirstTab
from utils.ping_whois_info import PingAndWHOISTab
from utils.disk_usage import DiskCalculate

class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt)
            painter.restore()

class VerticalTabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar())
        self.setTabPosition(QtWidgets.QTabWidget.West)





class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        tabs = VerticalTabWidget()

        # Tab 1
        self.tab_num1 = QtWidgets.QWidget()
        self.verticalLayout_tab_num1 = QtWidgets.QVBoxLayout(self.tab_num1)
        self.verticalLayout_tab_num1.addWidget(TotalInfoFirstTab())
        self.verticalLayout_tab_num1.addWidget(QtWidgets.QSplitter(QtCore.Qt.Vertical))
        tabs.addTab(self.tab_num1, "About System")

        # Tab 2
        self.tab_num2 = QtWidgets.QWidget()
        self.verticalLayout_tab_num2 = QtWidgets.QVBoxLayout(self.tab_num2)
        self.verticalLayout_tab_num2.addWidget(ChartViewCPURAM())
        self.verticalLayout_tab_num2.addWidget(ProcessesTable())
        tabs.addTab(self.tab_num2, "System load")

        # Tab 3
        self.tab_num3 = QtWidgets.QWidget()
        self.verticalLayout_tab_num3 = QtWidgets.QVBoxLayout(self.tab_num3)
        self.verticalLayout_tab_num3.addWidget(DiskCalculate())
        tabs.addTab(self.tab_num3, "Disk Usage")

        # Tab 4
        self.tab_num4 = QtWidgets.QWidget()
        self.verticalLayout_tab_num4 = QtWidgets.QVBoxLayout(self.tab_num4)
        self.verticalLayout_tab_num4.addWidget(PingAndWHOISTab())
        tabs.addTab(self.tab_num4, "PING && WHOIS")

        self.setCentralWidget(tabs)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = Window()

    window.resize(800, 600)
    window.setMaximumWidth(800)
    window.setMaximumHeight(600)
    screen_width = QtWidgets.QApplication.screenAt(window.pos()).size().width()
    screen_height = QtWidgets.QApplication.screenAt(window.pos()).size().height()
    window.move(int(screen_width / 2 - window.width() / 2), int(screen_height / 2 - window.height() / 2))
    window.setWindowTitle("System Monitor App")
    window.show()
    app.exec()