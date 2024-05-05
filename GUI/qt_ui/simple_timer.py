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

import resourse_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(599, 218)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(100, 218))
        MainWindow.setMaximumSize(QSize(599, 16777215))
        icon = QIcon()
        icon.addFile(u":/act/icons/clock.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QLineEdit:focus { background: white }\n"
"QLineEdit[enabled=\"true\"] {  color:  black }\n"
"QLineEdit {background: rgb(240, 240, 240);\n"
"border: 0px solid gray;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leH = QLineEdit(self.centralwidget)
        self.leH.setObjectName(u"leH")
        self.leH.setEnabled(True)
        self.leH.setMinimumSize(QSize(100, 140))
        self.leH.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(45)
        font.setKerning(False)
        self.leH.setFont(font)
        self.leH.setAutoFillBackground(False)
        self.leH.setStyleSheet(u"")
        self.leH.setMaxLength(2)
        self.leH.setAlignment(Qt.AlignCenter)
        self.leH.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.leH)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(40)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.leM = QLineEdit(self.centralwidget)
        self.leM.setObjectName(u"leM")
        self.leM.setEnabled(True)
        self.leM.setMinimumSize(QSize(100, 140))
        self.leM.setMaximumSize(QSize(100, 16777215))
        self.leM.setFont(font)
        self.leM.setMaxLength(2)
        self.leM.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.leM)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.leS = QLineEdit(self.centralwidget)
        self.leS.setObjectName(u"leS")
        self.leS.setEnabled(True)
        self.leS.setMinimumSize(QSize(100, 140))
        self.leS.setMaximumSize(QSize(100, 16777215))
        self.leS.setFont(font)
        self.leS.setMaxLength(2)
        self.leS.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.leS)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btnPause = QPushButton(self.centralwidget)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setMinimumSize(QSize(45, 45))
        self.btnPause.setMaximumSize(QSize(45, 45))
        icon1 = QIcon()
        icon1.addFile(u":/act/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPause.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.btnPause)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(45, 45))
        self.btnStart.setMaximumSize(QSize(45, 45))
        icon2 = QIcon()
        icon2.addFile(u":/act/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStart.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.btnStart)

        self.btnStop = QPushButton(self.centralwidget)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setMinimumSize(QSize(45, 45))
        self.btnStop.setMaximumSize(QSize(45, 45))
        icon3 = QIcon()
        icon3.addFile(u":/act/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStop.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.btnStop)

        self.btnConf = QPushButton(self.centralwidget)
        self.btnConf.setObjectName(u"btnConf")
        self.btnConf.setMinimumSize(QSize(45, 45))
        self.btnConf.setMaximumSize(QSize(45, 45))
        icon4 = QIcon()
        icon4.addFile(u":/act/icons/conf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnConf.setIcon(icon4)
        self.btnConf.setCheckable(True)

        self.verticalLayout_4.addWidget(self.btnConf)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_2.addWidget(self.label)

        self.cbSoundList = QComboBox(self.widget)
        self.cbSoundList.setObjectName(u"cbSoundList")

        self.horizontalLayout_2.addWidget(self.cbSoundList)

        self.btnPlaySound = QPushButton(self.widget)
        self.btnPlaySound.setObjectName(u"btnPlaySound")
        self.btnPlaySound.setMinimumSize(QSize(20, 0))
        self.btnPlaySound.setMaximumSize(QSize(20, 20))
        icon5 = QIcon()
        icon5.addFile(u":/act/icons/note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPlaySound.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.btnPlaySound)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.leH.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.leM.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.leS.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.btnPause.setText("")
        self.btnStart.setText("")
        self.btnStop.setText("")
        self.btnConf.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0443\u043a:", None))
        self.btnPlaySound.setText("")
    # retranslateUi

