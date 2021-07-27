import pygame
from _thread import *
import pickle

from pygame import locals as const
from constantes import *

from network import Network
from menu import Menu
from game import Game
from player import *

class Client:

    def initialize(self):
        pygame.init()
        pygame.font.init()

        # pygame.display.set_icon(pygame.image.load(CLIENT_ICON))
        pygame.display.set_caption(CLIENT_CAPTION)

        self.clock = pygame.time.Clock()
        self.ecran = pygame.display.set_mode(SCREEN_SIZE)
        self.players = Players()

    def threaded_server(self,network):
        while True:
            try:
                # Réception des infos du joueur 
                playerInfo = network.receive()
                print("Recu : ",playerInfo)

                if not playerInfo:
                    break
                else:
                    # Si on reçoit un truc c'est les infos d'un joueur qui a été update ou ajouté
                    if playerInfo.id in self.players.list:
                        self.players.modify(playerInfo)
                    else:
                        self.players.add(playerInfo,self.ecran)
            except :
                break
        print("Connexion terminée")

    def connect(self):
        self.network = Network()
        start_new_thread(client.threaded_server,(self.network,))

        try : 
            return self.network.ask("get")
        except Exception as e:
            print("Echec de connexion au serveur : ",e)
            exit()

    def run(self):
        
        # Creation du personnage
        menu = Menu(self.ecran,self.clock)
        menu.start()
        created_info = menu.get_player_info()

        # Connexion au serveur
        self.playerInfo = self.connect()

        # On modifie les infos reçues et on renvoie
        created_info.id  = self.playerInfo.id
        created_info.pos = self.playerInfo.pos
        self.playerInfo  = created_info
        self.network.send(self.playerInfo)

        # On rajoute à la liste des joueurs présents
        self.players.add(self.playerInfo,self.ecran)
        print(self.players)

        # Lancement du jeu
        jeu = Game(self.ecran,self.clock,self.network,self.players)
        jeu.start()

        pygame.quit()

###########

client = Client()
client.initialize()
# start_new_thread(client.threaded_server,(client.network,))
client.run()