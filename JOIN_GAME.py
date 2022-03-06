#HackMerced7
#Ritesh Patro
#Raivat Alwar

import sys
import variables
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class join1(QMainWindow):
    username = ""
    accessCode = "7uiB"

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

        # Text on window
        self.c1 = QLabel('\tEnter Game Code:', self)
        self.c1.adjustSize()
        self.c1.move(-30, 90)

        self.c_1= QLineEdit(self)
        self.c_1.move(140, 85)

        self.c2 = QLabel('\tUsername:', self)
        self.c2.adjustSize()
        self.c2.move(-30, 140)

        self.c_2 = QLineEdit(self)
        self.c_2.move(140, 135)

        # self.button_join1 = QPushButton('Back', self)
        # self.button_join1.move(350, 205)
        # self.button_join1.clicked.connect(self.goBack)

        self.IncorrectCodeLabel = QLabel("\tIncorrect Code Label", self)
        self.IncorrectCodeLabel.setGeometry(QRect(40, 248, 111, 61))
        self.IncorrectCodeLabel.setObjectName("IncorrectCodeLabel")
        self.IncorrectCodeLabel.setText("")

        self.button_join2 = QPushButton('Join Game', self)
        self.button_join2.move(150, 205)
        self.button_join2.clicked.connect(self.ifClicked)

    # def goBack(self):
    #     print("i am going back")
        
    
    def ifClicked(self):
        #print error message to window if user inputs wrong access code
        if self.c_1.text() != self.accessCode:
            self.IncorrectCodeLabel.setText("Incorrect code entered; Please try again")
            self.IncorrectCodeLabel.adjustSize()

        #save username & prepare to go to game window if user inputs right access code
        else:
            username = self.c_2.text()
            print("Success")

app = QApplication(sys.argv)
# window = join1()
# window.show()

# app.exec()