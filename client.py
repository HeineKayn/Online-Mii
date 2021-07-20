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
        self.network = Network()
        self.players = Players()

    def threaded_server(self,network):
        while True:
            try:
                print("test")
                # Réception des infos du joueur 
                playerInfo = network.recv()
                print(playerInfo)

                if not playerInfo:
                    break
                else:
                    # Si on reçoit un truc c'est les infos d'un joueur qui a été update ou ajouté
                    if playerInfo.id in self.players.list:
                        self.players.modify(playerInfo)
                    else:
                        self.players.add(playerInfo)
            except:
                pass

    def run(self):
        
        try : 
            self.playerInfo  = self.network.ask("get")
        except Exception as e:
            print("Echec de connexion au serveur : ",e)
            exit()

        self.players.add(self.playerInfo)
        self.players.list[self.network.playerId].ecran = self.ecran
        print(self.players)

        # Interfaces
        menu = Menu(self.ecran,self.clock,self.network,self.players)
        menu.start()

        jeu = Game(self.ecran,self.clock,self.network,self.players)
        jeu.start()

        pygame.quit()

###########

client = Client()
client.initialize()
start_new_thread(client.threaded_server,(client.network,))
client.run()