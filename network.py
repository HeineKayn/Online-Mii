import socket
import pickle

from constantes import *

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER_IP
        self.port = SERVER_PORT
        self.addr = (self.server, self.port)

        self.playerId = int(self.connect())
        print("Connecté, id = ",self.playerId)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(pickle.dumps(data))
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

    def ask(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

