import pygame

class Player():
    def __init__(self):
        self.username = ""
        self.score = 0

    def __init__(self, username):
        self.username = username
        self.score = 0

    def __init__(self, username, score):
        self.username = username
        self.score = score