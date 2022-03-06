#HackMerced7
#Ravikiran Madichetty
#Raivat Alwar

import sys
import RKM_MAKE_GAME_SCREEN
import JOIN_GAME
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window1(QMainWindow):
    #Window Size
    def __init__(self):
        super().__init__()
        self.title = "Jumblo"
        self.top = 600
        self.left = 600
        self.width = 600
        self.height = 500
        self.main1()

    def main1(self):
        # Text on window
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.label01 = QLabel('Welcome to Jumblo', self)
        self.label01.adjustSize()
        self.label01.move(50,50)

        self.label2 = QLabel('How to Play:', self)
        self.label2.adjustSize()
        self.label2.move(50, 70)

        self.label02 = QLabel('\t1. You are given a list of random letters and are supposed to make as many \n\t    words as possible in the given time frame.', self)
        self.label02.adjustSize()
        self.label02.move(50, 90)

        self.label03 = QLabel('\t2. The letters can be repeatable and used multiple times in the same word.', self)
        self.label03.adjustSize()
        self.label03.move(50, 125)

        self.label04 = QLabel('\t3. The words must be at least 3 letters long.', self)
        self.label04.adjustSize()
        self.label04.move(50, 145)

        #Make a Game Button
        self.button = QPushButton('Make a Game', self)
        self.button.clicked.connect(self.showMakeGame)
        self.button.move(150, 200)

        #Join Game Button
        # self.button = QPushButton('Join Game', self)
        # self.button.clicked.connect(self.showJoinGame)
        # self.button.move(350, 200)
    
    def showMakeGame(self, checked):
        self.w = RKM_MAKE_GAME_SCREEN.Window2()
        self.w.show()
        window.hide()
    
    # def showJoinGame(self, checked):
    #     self.w = JOIN_GAME.join1()
    #     self.w.show()
    #     window.hide()

app = QApplication(sys.argv)

window = Window1()
window.show()

app.exec()