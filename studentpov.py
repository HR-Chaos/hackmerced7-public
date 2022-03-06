#HackMerced7
#Ravikiran Madichetty


import sys
import variables
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
from wordLogic import *
import random


#Teachers POV// Leaderboards
class Window3(QMainWindow):
    t = 15
    key = ""
    size = int(random.uniform(3,26))
    list_of_words = []
    #key_size = 10
    # print("global: ", str(variables.GlobalVar.size))
    #size = variables.GlobalVar.getSize
    key = keyGenerator(size)
    #key = keyGenerator(int(variables.GlobalVar.getSize()))

    def __init__(self):
        super().__init__()
        self.title = "Jumblo"
        self.top = 600
        self.left = 600
        self.width = 600
        self.height = 500
        self.main3()

    def set_size(self, sizeIn):
        self.size = sizeIn
        self.key = keyGenerator(int(self.size))

    def main3(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.list = QLabel('\tLetter List: ', self)
        self.list.setFont(QFont('Helvetica', 10))
        self.list.adjustSize()
        self.list.move(-47, 50)

        self.temp = QLabel(self.key, self)
        self.temp.adjustSize()
        self.temp.move(120, 53)

        self.timer = QLabel('Timer:',self)
        self.timer.adjustSize()
        self.timer.move(400,20)

        self.word = QLabel('\tEnter Word: ', self)
        self.word.adjustSize()
        self.word.move(-30, 90)

        self.word1 = QLineEdit(self)
        self.word1.move(120, 85)

        self.button_word_1 = QPushButton('Enter', self)
        self.button_word_1.move(222, 85)
        self.button_word_1.clicked.connect(self.ifClicked)


    def ifClicked(self):
        wrd = self.word1.text()
        if(wrd == "END"):
            print("You got ", len(self.list_of_words), " points!")
            self.close()
        elif check(self.key, wrd):
            if findWordM("dictionary.txt",wrd):
                self.list_of_words.append(wrd)
        print(self.list_of_words)

# define the countdown func.
    def countdown(self):
        while self.t:
            mins, secs = divmod(self.t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer)
            time.sleep(1)
            self.t -= 1
            print('Fire in the hole!!')

app = QApplication(sys.argv)

# window = Window3()
# window.show()
# window.countdown()

# app.exec()

'''
def initUI(self):
    # ...
    self.text_box = QtWidgets.QTextEdit(self)
    self.text_box.installEventFilter(self)
    # ...

def eventFilter(self, obj, event):
    if event.type() == QtCore.QEvent.KeyPress and obj is self.text_box:
        if event.key() == QtCore.Qt.Key_Return and self.text_box.hasFocus():
            print('Enter pressed')
    return super().eventFilter(obj, event)
'''