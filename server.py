import socket
from _thread import *
import pickle

from player import Player
from constantes import *

class Server:
    def __init__(self): 
        self.connected = set()
        self.clientCount = 0
        self.players = []
        self.preparation()
        self.run()

    def preparation(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((SERVER_IP, SERVER_PORT))
        except socket.error as e:
            str(e)
        self.socket.listen(SERVER_NUMBER_MAX_CONNEXION)
        print("En attente de connexions, SERVEUR Started")

    def run(self):

        while True:
            conn, addr = self.socket.accept()
            print("Connected to :", addr)

            self.players[self.clientCount] = Player(self.clientCount)
            start_new_thread(threaded_client, (conn, self.clientCount))
            self.clientCount += 1

    def threaded_client(self,conn,playerId):
        conn.send(str.encode(str(playerId)))

        while True:
            try:
                data = conn.recv(4096).decode()
                player = self.players[playerId]

                if not data:
                    break
                else:
                    # Si on envoie pas get alors on a envoyé le perso (modifié)
                    if data != "get":
                        players[playerId] = data

                    conn.sendall(pickle.dumps(player))
            except :
                break

        print("Connexion perdue")
        try:
            del self.players[playerId]
            print("Fermeture d'un client", playerId)
        except:
            pass
        self.clientCount -= 1
        conn.close()