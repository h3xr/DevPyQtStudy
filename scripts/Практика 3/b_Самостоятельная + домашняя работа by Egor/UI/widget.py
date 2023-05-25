# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLCDNumber,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Demo_Form(object):
    def setupUi(self, Demo_Form):
        if not Demo_Form.objectName():
            Demo_Form.setObjectName(u"Demo_Form")
        Demo_Form.resize(546, 345)
        self.gridLayout = QGridLayout(Demo_Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_stop = QPushButton(Demo_Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.gridLayout.addWidget(self.pushButton_stop, 3, 4, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Demo_Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.progressBar_cpu = QProgressBar(Demo_Form)
        self.progressBar_cpu.setObjectName(u"progressBar_cpu")
        self.progressBar_cpu.setValue(0)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.progressBar_cpu)

        self.label_3 = QLabel(Demo_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.progressBar_ram = QProgressBar(Demo_Form)
        self.progressBar_ram.setObjectName(u"progressBar_ram")
        self.progressBar_ram.setValue(0)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.progressBar_ram)

        self.textEdit_text = QTextEdit(Demo_Form)
        self.textEdit_text.setObjectName(u"textEdit_text")

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.textEdit_text)

        self.label = QLabel(Demo_Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label)

        self.lcdNumber = QLCDNumber(Demo_Form)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lcdNumber)


        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 5)

        self.pushButton_start = QPushButton(Demo_Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.gridLayout.addWidget(self.pushButton_start, 3, 3, 1, 1)


        self.retranslateUi(Demo_Form)

        QMetaObject.connectSlotsByName(Demo_Form)
    # setupUi

    def retranslateUi(self, Demo_Form):
        Demo_Form.setWindowTitle(QCoreApplication.translate("Demo_Form", u"System Information", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Demo_Form", u"Stop Thread", None))
        self.label_2.setText(QCoreApplication.translate("Demo_Form", u"CPU", None))
        self.label_3.setText(QCoreApplication.translate("Demo_Form", u"RAM", None))
        self.label.setText(QCoreApplication.translate("Demo_Form", u"Time delay", None))
        self.pushButton_start.setText(QCoreApplication.translate("Demo_Form", u"Start Thread", None))
    # retranslateUi