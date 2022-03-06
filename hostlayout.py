#HackMerced7
#Ritesh Patro
#Raivat Alwar

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import variables

class HostLayout(QMainWindow):
    #time = 0
    jumblo = ""
    leaderboardPlayers = ["sparklyunico", "Ravioli"]
    leaderboardScores = [69, 53]

    def __init__(self):
        super(HostLayout, self).__init__()
        self.setGeometry(600, 600, 600, 500)
        self.setWindowTitle("Jumblo")
        self.initUI()

    def updateLeaderboard(self):
        QLabelList = []
        for i in range(0,len(self.leaderboardScores)):
            QLabelList.append(QLabel(self))

            spaces = 50 - len(self.leaderboardPlayers[i])

            for j in range(0, spaces):
                self.leaderboardPlayers[i] = self.leaderboardPlayers[i] + " "

            QLabelList[i].setText(str(self.leaderboardPlayers[i]))
            QLabelList[i].adjustSize()
            QLabelList[i].move(300, 150 + 15 * i)
        
        QLabelList = []
        for i in range(0,len(self.leaderboardScores)):
            QLabelList.append(QLabel(self))
            QLabelList[i].setText(str(self.leaderboardScores[i]))
            QLabelList[i].adjustSize()
            QLabelList[i].move(500, 150 + 15 * i)

    def initUI(self):
        self.timerLabel = QLabel(self)
        self.timerLabel.setText("Time: " + str(variables.GlobalVar.time))
        self.timerLabel.move(450, 50)

        self.leaderboardTitleLabel = QLabel(self)
        self.leaderboardTitleLabel.setText("Leaderboard")
        self.leaderboardTitleLabel.move(400, 100)

        self.usernameTitleLabel = QLabel(self)
        self.usernameTitleLabel.setText("Username:")
        self.usernameTitleLabel.move(300, 125)

        self.scoreTitleLabel = QLabel(self)
        self.scoreTitleLabel.setText("Score:")
        self.scoreTitleLabel.move(500, 125)

        self.updateLeaderboard()

        self.jumbloLabel = QLabel(self)
        self.jumbloLabel.setText("Jumblo: " + self.jumblo)
        self.jumbloLabel.move(100, 150)

app = QApplication(sys.argv)

# def window():
    
#     app = QApplication(sys.argv)
#     win = HostLayout()
#     win.show()
#     sys.exit(app.exec_())

#window()