import pygame
import pickle
from pygame import locals as const

from player import *
from constantes import *

class Game:
    def __init__(self, ecran, clock, network, players):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)

        self.network = network
        self.players = players
        self.main_player = self.players.list[self.network.playerId]
    
    def prepare(self):
        pygame.key.set_repeat(1, 0)
        self.continuer = True
    
    def update_screen(self):
        self.ecran.blit(self.bg, (0, 0))
        self.players.render() 

    def update_game(self):
        has_changed = self.main_player.update()

        if has_changed :
            self.network.send(self.main_player.info)
    
    def process_event(self, event: pygame.event):

        # Click Gauche
        # if event.type == const.MOUSEBUTTONUP and event.button == 1:
        #     self.projectiles.destroy(event.pos)

        # Le déplacement se fait directement dans Player

        if event.type == const.QUIT:
            self.continuer = False
    
    def start(self):
        self.prepare()

        # On spawn le joueur
        self.network.send(self.main_player.info)
        
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.update_screen()
            self.update_game()

            pygame.display.flip()
            self.clock.tick(60)