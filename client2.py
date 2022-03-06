import pygame
from network import Network
from player import Player
import time
from wordLogic import *


'''
This part checks the file to see what the server number is
'''
server = "none"
with open("address.txt", 'r') as inFile:
    server = inFile.read()
inFile.close()


# main function that runs continuously
def find_word(word):
    return findWordM("dictionary.txt", word)


def main():
    run = True
    clock = pygame.time.Clock()
    user_name = input("What is your name? ")
    n = Network(server)
    # get players
    p = n.get_p()
    key = n.send(p)
    print(key)

    timer = 10
    t0 = time.time()
    user_input = []
    i = 0

    p = Player(user_name, 0)
    #split dictionary
    while time.time() - t0 < timer:
        inp = input("Enter something: ")
        if check(key, inp):
            if find_word(inp):
                user_input.append(inp)
                p.score += 1
    print(user_name)
    print(user_input)
    n.send(p)


main()