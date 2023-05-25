# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_weather.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.textEdit_info = QTextEdit(Form)
        self.textEdit_info.setObjectName(u"textEdit_info")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.textEdit_info)

        self.doubleSpinBox_lat = QDoubleSpinBox(Form)
        self.doubleSpinBox_lat.setObjectName(u"doubleSpinBox_lat")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_lat)

        self.doubleSpinBox_lon = QDoubleSpinBox(Form)
        self.doubleSpinBox_lon.setObjectName(u"doubleSpinBox_lon")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_lon)

        self.doubleSpinBox_sleep = QDoubleSpinBox(Form)
        self.doubleSpinBox_sleep.setObjectName(u"doubleSpinBox_sleep")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_sleep)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)

        self.pushButton_stop = QPushButton(Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.gridLayout.addWidget(self.pushButton_stop, 1, 1, 1, 1)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.gridLayout.addWidget(self.pushButton_start, 1, 0, 1, 1)

        self.label_message = QLabel(Form)
        self.label_message.setObjectName(u"label_message")

        self.gridLayout.addWidget(self.label_message, 2, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Weather Information", None))
        self.label.setText(QCoreApplication.translate("Form", u"Latitude", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Longitude", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Time delay", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"Stop Thread", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"Start Thread", None))
        self.label_message.setText("")
    # retranslateUi