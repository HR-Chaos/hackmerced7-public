import socket
from _thread import *
import sys
from player import Player
import pickle
from wordLogic import *


# use socket and threading for connections on a port
server = ""     # this will be a string
port = 5555     # this will be a number (int?)  5555 is a random, typically open, port

# set up a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ipv4 connection needed and sock_stream is how the server string is received

# bind server and port to socket
# try catch (except) to check if port is available
# set address of server
server = socket.gethostbyname(socket.gethostname())
try:
    s.bind((server, port))      # double perenthesis as it is one parameter
except socket.error as e:
    str(e)

# colors
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
# INIT players in server
players = [Player("Lard", 0), Player("Bart", 0)]

# open up port; argument optional, leaving blank will allow unlimited connections
max_number_players = 10
s.listen(max_number_players)
print("Server started... Waiting for connection")
key = keyGenerator(10)


# define a threaded function
def threaded_client(conn, player):       # pass in a var called conn that is just the connection
    print(key)
    conn.send(pickle.dumps(players[player]))  # want to send init position of player
    reply = "reply"
    input("SaySomething")
    while True:
        try:
            data = pickle.loads(conn.recv(2048*4))  # if any errors occur or something is being truanced, increase size of bits (2048*2)
            players[player] = data      # Data has to be encoded when sent
            print(players[player].score)

            if not data:        # if we don't get data, client may have left
                print("disconnected")
                break   # failsafe to not get into a loop
            else:
                print("Received: ", data.score, data.username)
                print("Sending: ", key)

            conn.sendall(pickle.dumps(key))     # encode string into a bytes object
        except:
            break
    print("Lost Connection")
    conn.close()


# keep track of how many players connected
number_players = 0
# while loop continuously looks for connections
while True:
    conn, adr = s.accept()
    print("Connected to: ", adr)

    # starts a new thread that will run in the background
    start_new_thread(threaded_client, (conn, number_players))
    number_players += 1
