import pygame
import pickle
from pygame import locals as const

from player import *
from constantes import *

class Menu():

    def __init__(self, ecran, clock, network, players):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)

        self.network = network
        self.players = players

        self.player = self.players.list[self.network.playerId]
        self.player.info.name = "Deltix"
        self.player.info.color = BLUE
        self.players.list[self.network.playerId] = self.player

    def render(self):
        self.ecran.blit(self.bg, (0, 0))
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Appuyer sur une touche", 1, (255,0,0), True)
        self.ecran.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

    def process_event(self):
        for event in pygame.event.get():
            if event.type == const.QUIT :
                exit()
            if event.type == const.KEYDOWN:
                self.continuer = 0

    def start(self):
        while self.continuer:
            self.process_event()
            self.render()
            pygame.display.flip()    
            self.clock.tick(60)