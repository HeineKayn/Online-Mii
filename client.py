import pygame
from network import Network
import pickle

from pygame import locals as const
from constantes import *

from menu import Menu
from game import Game

def main():

    pygame.init()
    pygame.font.init()

    pygame.display.set_icon(pygame.image.load(CLIENT_ICON))
    pygame.display.set_caption(CLIENT_CAPTION)

    clock = pygame.time.Clock()
    ecran = pygame.display.set_mode(SCREEN_SIZE)

    # Partie Multijoueur 
    network = Network()
    try : 
        player  = network.send("get")
    except :
        print("Echec de connexion au serveur")
        exit()

    # Interfaces
    menu = Menu(ecran,clock,player)
    menu.start()

    jeu = Game(ecran,clock,player)
    jeu.start()

    pygame.quit()

if __name__ == '__client__':
    main()