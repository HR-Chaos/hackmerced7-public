#HackMerced7
#Ravikiran Madichetty
#Raivat Alwar

import sys
import hostlayout
import variables
import studentpov
import socket
#import RKM_MAIN_Window
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window2(QMainWindow):
    #time = 15 #just commented
    #size = 3 #just commented
    variables.GlobalVar.time = 15
    variables.GlobalVar.size = 3

    # Window Size
    def __init__(self):
        super().__init__()
        self.title = "Jumblo"
        self.top = 600
        self.left = 600
        self.width = 600
        self.height = 500
        self.main2()

    def main2(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        server_ad = socket.gethostbyname(socket.gethostname())
        # Text on window
        self.code = QLabel('\tGame Code:' + server_ad, self)
        self.code.adjustSize()
        self.code.move(-30, 90)

        server_address = ""
        self.code = QLabel(server_address, self)
        self.code.adjustSize()
        self.code.move(150, 90)

        # self.fillcode = QLineEdit(self)
        # self.fillcode.move(152, 85)
        # self.fillcode.resize(280, 40)

        #Letter Range
        self.range = QLabel('\tSelect range of letters from 3 to 26:', self)
        self.range.adjustSize()
        self.range.move(-30, 130)

        self.range = QLabel('random', self)
        self.range.adjustSize()
        self.range.move(202, 130)

        # self.fillcode = QLineEdit(self)
        # self.fillcode.textEdited.connect(self.getRange)
        # self.fillcode.move(232, 125)

        self.IncorrectCodeLabel = QLabel("\tIncorrect Code Label", self)
        self.IncorrectCodeLabel.setGeometry(QRect(40, 248, 111, 61))
        self.IncorrectCodeLabel.setObjectName("IncorrectCodeLabel")
        self.IncorrectCodeLabel.setText("")

        #Timer
        self.timer = QLabel('\tChoose a timer preset:', self)
        self.timer.adjustSize()
        self.timer.move(-30, 170)

        self.button_timer1 = QPushButton('15 Seconds', self)
        self.button_timer1.clicked.connect(self.setTime1)
        self.button_timer1.move(152, 165)

        # self.button_timer2 = QPushButton('30 Seconds', self)
        # self.button_timer2.clicked.connect(self.setTime2)
        # self.button_timer2.move(252, 165)

        # self.button_timer3 = QPushButton('60 Seconds', self)
        # self.button_timer3.clicked.connect(self.setTime3)
        # self.button_timer3.move(352, 165)

        # self.button_timer4 = QPushButton('90 Seconds', self)
        # self.button_timer4.clicked.connect(self.setTime4)
        # self.button_timer4.move(452, 165)

        self.TimeChosen = QLabel("Time Chosen: ", self)
        self.TimeChosen.move(400,20)
        self.TimeChosen.setObjectName("TimeChosen")
        self.TimeChosen.setText("Time Chosen: 15 seconds")
        self.TimeChosen.adjustSize()


# Just added
        self.letChosen = QLabel("Amount of Letters Chosen: ", self)
        self.letChosen.move(350,40)
        self.letChosen.setObjectName("letChosen")
        self.letChosen.setText("Amount of Letters Chosen: 3 letters")
        self.letChosen.adjustSize()

        #Join game
        self.button_joinGame = QPushButton('Start Game', self)
        self.button_joinGame.clicked.connect(self.join)
        self.button_joinGame.move(150, 205)

    def join(self):
        #if(self.fillcode.text().isdecimal()):
          #  variables.GlobalVar.size = self.fillcode.text()
           # if (int(variables.GlobalVar.size) > 2) and (int(variables.GlobalVar.size) < 27):
                #self.IncorrectCodeLabel.setText("")
        self.host = studentpov.Window3()
                # variables.GlobalVar.setSize(self, int(self.fillcode.text()))
                # self.host.set_size(int(self.fillcode.text()))
        self.host.show()
        self.hide()
            #else:
             #   self.IncorrectCodeLabel.setText("Please input a valid range of letters: [3,26]")
              #  self.IncorrectCodeLabel.adjustSize()

    def getRange(self):
        if(self.fillcode.text().isdecimal()):
            self.IncorrectCodeLabel.setText("Incorrect range of letters inputted. Please try again")
            if (int(self.fillcode.text()) < 3) or (int(self.fillcode.text()) > 26):
                self.IncorrectCodeLabel.setText("Incorrect range of letters inputted. Please try again")
                self.IncorrectCodeLabel.adjustSize()

            else:
                variables.GlobalVar.size = self.fillcode.text()
                self.printLet() # Just added
                self.IncorrectCodeLabel.setText("")
                print(variables.GlobalVar.size)
            
    def setTime1(self):
        variables.GlobalVar.time = 15
        self.printTime()
        
    def setTime2(self):
        variables.GlobalVar.time = 30
        self.printTime()
        
    def setTime3(self):
        variables.GlobalVar.time = 60
        self.printTime()
        
    def setTime4(self):
        variables.GlobalVar.time = 90
        self.printTime()
    
# Just added

    def printLet(self):
        phrase = "Amount of Letters Chosen: " + str(variables.GlobalVar.size) + " letters"
        self.letChosen.setText(phrase)
        self.letChosen.adjustSize()
        #print("time:",self.time)

    def printTime(self):
        phrase = "Time Chosen: " + str(variables.GlobalVar.time) + " seconds"
        self.TimeChosen.setText(phrase)
        self.TimeChosen.adjustSize()
        print("time:",variables.GlobalVar.time)

app = QApplication(sys.argv)

#window = Window2()
#window.show()

#app.exec()