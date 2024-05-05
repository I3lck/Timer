import sys
import time
from Model.Player import SoundPlayer
from datetime import datetime, timedelta

from GUI.qt_ui.simple_timer import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QListWidgetItem, QMainWindow, \
    QAction, QInputDialog, QWidget, QLCDNumber, QLineEdit, QPushButton
from PySide2.QtCore import Signal, Slot, QTimer, Qt, QTime
from PySide2.QtGui import Qt, QKeySequence, QPixmap, QIcon, QIntValidator, QValidator
import PySide2



class ValidatorTime(QIntValidator):
    def validate(self, arg__1: str, arg__2: int) -> QValidator.State:
        print(f'Validate len... len = {len(arg__1)}')
        if len(arg__1) == 0 or len(arg__1) < 2:

            return QIntValidator.Intermediate
        return super().validate(arg__1, arg__2)



class ValidatorMinAndSec(ValidatorTime):

    def fixup(self, input:str) -> str:
        if len(input) == 0:
            return '00'
        elif len(input) < 2:
            return f'0{input}'
        elif int(input) > 59:
            return '59'

class ValidatorHour(ValidatorTime):

    def fixup(self, input:str) -> str:
        if len(input) == 0:
            return '00'
        if len(input) < 2:
            return f'0{input}'








class Time:
    def __init__(self,
                 hours: int,
                 minutes: int,
                 seconds: int):

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __sub__(self, other):
        hours = self.hours
        minutes = self.minutes

        seconds = self.decrement(self.seconds)
        if seconds == 59:
            minutes = self.decrement(self.minutes)
            if minutes == 59:
                hours = self.decrement(self.hours)
                if hours - 1 >= -1:
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                    return self
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        return self

    def __str__(self):
        return f'{self.hours:0>2}:{self.minutes:0>2}:{self.seconds:0>2}'

    def __eq__(self, other):
        return True if self.hours == self.minutes == self.seconds == other else False

    def getHours(self):
        return f'{self.hours:0>2}'

    def getSeconds(self):
        return f'{self.seconds:0>2}'

    def getMinutes(self):
        return f'{self.minutes:0>2}'



    def decrement(self, value: int):
        value -= 1
        if value == -1:
            return 59
        else:
            return value

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnPause.hide()
        self.ui.widget.hide()




        self.ui.leH.setValidator(ValidatorHour(0, 99))
        self.ui.leM.setValidator(ValidatorMinAndSec(0, 59))
        self.ui.leS.setValidator(ValidatorMinAndSec(0, 59))


        self.ui.leH.editingFinished.connect(self.parseTimeFromLE)
        self.ui.leM.editingFinished.connect(self.parseTimeFromLE)
        self.ui.leS.editingFinished.connect(self.parseTimeFromLE)
        self.ui.btnStart.clicked.connect(self.startTimer_)
        self.ui.btnStop.clicked.connect(self.stopTimer)
        self.ui.btnPause.clicked.connect(self.pauseTimer)
        self.ui.btnConf.clicked.connect(self.showMenu)




        self.timer = QTimer(self)
        self.timer.timeout.connect(self.countdown)
        self.timer.setInterval(1000)

        self.time = Time(hours=0,
                         minutes=0,
                         seconds=0
                         )
        # self.showTime()

        self.sound_player = SoundPlayer()
        self.sound_player.set_sound('CAKEBOY, IROH - НЕРВЫ.mp3')









    def setTimer(self, hours: int, minutes: int, seconds: int):
        self.time = Time(hours=hours,
                         minutes=minutes,
                         seconds=seconds
                         )
        self.showTime()

    def showTime(self):
        self.ui.leH.setText(self.time.getHours())
        self.ui.leM.setText(self.time.getMinutes())
        self.ui.leS.setText(self.time.getSeconds())


    def resetTimer(self):
        self.setTimer(self.hours, self.minutes, self.seconds)

    def startTimer_(self):
        if not self.timer.isActive():
            self.timer.start()
            self.blockInputInterface()
            self.ui.btnStart.hide()
            self.ui.btnPause.show()



    def endTimer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.unblockInputInterface()
            self.sound_player.play()

    def pauseTimer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.btnPause.hide()
            self.ui.btnStart.show()
            self.unblockInputInterface()



    def stopTimer(self):
        self.resetTimer()
        self.timer.stop()
        self.ui.btnPause.hide()
        self.ui.btnStart.show()
        self.unblockInputInterface()
        self.sound_player.stop()



    def parseTimeFromLE(self):
        self.hours = self.convertValue(self.ui.leH.text())
        self.minutes = self.convertValue(self.ui.leM.text())
        self.seconds = self.convertValue(self.ui.leS.text())
        self.setTimer(self.hours, self.minutes, self.seconds)





    def blockInputInterface(self):
        self.ui.leH.setEnabled(False)
        self.ui.leM.setEnabled(False)
        self.ui.leS.setEnabled(False)

    def unblockInputInterface(self):
        self.ui.leH.setEnabled(True)
        self.ui.leM.setEnabled(True)
        self.ui.leS.setEnabled(True)



    def convertValue(self, value):
        return int(value) if value else 0


    def countdown(self):
        self.time -= 1
        self.showTime()
        if self.time == 0:
            self.endTimer()

    def showMenu(self):
        print('showMenu')
        if self.ui.btnConf.isChecked():
            self.ui.widget.show()
            self.setFixedWidth(439 + 160 - 20)
            # self.resize(439, 155)


        else:
            self.ui.widget.hide()
            # self.resize(439, 155)
            self.setFixedWidth(439- 20)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    sys.exit(app.exec_())
    # t = Time('0', '0', '02')
    # print()
