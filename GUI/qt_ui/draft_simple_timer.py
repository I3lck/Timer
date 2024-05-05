# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simple_timer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(264, 188)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.display = QLCDNumber(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setSmallDecimalPoint(False)
        self.display.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout.addWidget(self.display)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lnHours = QLineEdit(self.centralwidget)
        self.lnHours.setObjectName(u"lnHours")
        self.lnHours.setMaxLength(2)

        self.horizontalLayout_2.addWidget(self.lnHours)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lnMinutes = QLineEdit(self.centralwidget)
        self.lnMinutes.setObjectName(u"lnMinutes")
        self.lnMinutes.setMaxLength(2)

        self.horizontalLayout_2.addWidget(self.lnMinutes)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lnSeconds = QLineEdit(self.centralwidget)
        self.lnSeconds.setObjectName(u"lnSeconds")
        self.lnSeconds.setMaxLength(2)

        self.horizontalLayout_2.addWidget(self.lnSeconds)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnPause = QPushButton(self.centralwidget)
        self.btnPause.setObjectName(u"btnPause")

        self.horizontalLayout.addWidget(self.btnPause)

        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout.addWidget(self.btnStop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnPause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

