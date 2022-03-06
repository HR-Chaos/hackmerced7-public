import socket
import pickle   # serialize object (turn into byte: 0s and 1s)


class Network:
    def __init__(self, server):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()   # position in queue

    def get_p(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*4))
        except:
            pass


    def send(self, data):
        try:
            # user pickle.dumps to recv data, and .loads to zip data and send it
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*4))
        except socket.error as e:
            print(e)

