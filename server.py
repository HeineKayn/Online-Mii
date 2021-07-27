import socket
from _thread import *
import pickle
from random import randint

from player import *
from constantes import *

class Server:
    def __init__(self): 
        self.connected = set()
        self.clientCount = 0
        self.playerInfos = {}
        self.conns       = {}

    ###### Serveur

    def preparation(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((SERVER_IP, SERVER_PORT))
        except socket.error as e:
            str(e)
        self.socket.listen(SERVER_NUMBER_MAX_CONNEXION)
        print("En attente de connexions, SERVEUR Started")

    # ---- 

    def run(self):

        while True:
            conn, addr = self.socket.accept()
            self.conns[self.clientCount] = conn
            print("Connected to :", addr)

            start_pos = [randint(0,WIDTH),randint(0,HEIGHT)]
            self.playerInfos[self.clientCount] = PlayerInfo(self.clientCount,start_pos)

            start_new_thread(self.threaded_client, (conn, self.clientCount))
            self.clientCount += 1

    ####### Chaque clients

    def threaded_client(self,conn,playerId):

        # A l'établissement de la connexion, on envoie le numéro du joueur
        conn.send(str.encode(str(playerId)))

        # On lui envoie les infos sur tous les autres joueurs
        for i, playerInfo in self.playerInfos.items():
            conn.sendall(pickle.dumps(playerInfo))

        while True:
            try:
                # Réception des infos du joueur 
                data = pickle.loads(conn.recv(4096))

                if not data:
                    break
                else:
                    # --- PAS UTILE POUR L'INSTANT
                    # Si on envoie un chiffre, alors on renvoie les infos du joueur correspondant
                    if isinstance(data,int):
                        conn.sendall(pickle.dumps(self.playerInfos[data]))

                    # Si on envoie "get" ça renvoie nos propres infos
                    if data == "get":
                        conn.sendall(pickle.dumps(self.playerInfos[playerId]))

                    # Si on recoit des données c'est qu'on veut modifier le joueur qui l'a envoyé
                    else :
                        self.playerInfos[playerId] = data

                        # On envoie à tous le monde le joueur qui à été modifié
                        for i, playerInfo in self.playerInfos.items():
                            self.conns[i].sendall(pickle.dumps(self.playerInfos[playerId]))

            except :
                break

        print("Connexion perdue")
        try:
            # On lui mets l'attribut disant qu'il a déco
            self.playerInfos[playerId].connected = False

            # Puis on envoie l'info à tout le monde
            for i, playerInfo in self.playerInfos.items():
                if i != playerId :
                    self.conns[i].sendall(pickle.dumps(self.playerInfos[playerId]))

            # Puis on le supprime de la liste du serveur
            del self.playerInfos[playerId]
            del self.conns[playerId]
            print("Fermeture d'un client", playerId)
        except:
            pass
        self.clientCount -= 1
        conn.close()

####### INSTANCIATION

server = Server()
server.preparation()
server.run()