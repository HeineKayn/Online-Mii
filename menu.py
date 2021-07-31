import pygame
import pickle
from pygame import locals as const

from player import *
from constantes import *

from selector import *
from input import *
from button import *

class Menu():

    def __init__(self, ecran, clock):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)

        self.player = Player(PlayerInfo(0,[WIDTH//2,HEIGHT//2 - 100]),self.ecran)
        self.init_hud()

    def init_hud(self):
        hud_pos = [WIDTH//2,HEIGHT//2 + 20]
        margin  = 100

        self.selectors = Selectors(self.ecran)
        self.selectors.add("color",COLOR_LIST,hud_pos)
        self.input = Input(self.ecran,[hud_pos[0],hud_pos[1]+margin])
        self.confirm = Button(self.ecran,[hud_pos[0],hud_pos[1]+margin*2])

    def render(self):
        self.ecran.blit(self.bg, (0, 0))
        self.player.render()
        self.selectors.render()
        self.input.render()
        self.confirm.render()

    def process_event(self):
        for event in pygame.event.get():

            # Si clique sur fermer
            if event.type == const.QUIT :
                exit()

            # Si clique gauche
            if event.type == const.MOUSEBUTTONUP and event.button == 1:

                if self.confirm.collide(event.pos) :
                    self.modify_player_info()
                    self.continuer = 0

                else :
                    self.selectors.collide(event.pos)
                    self.input.collide(event.pos)
                    self.modify_player_info()
                    self.player.update_color()

            if event.type == const.KEYDOWN:
                self.input.process_key(event)
                self.modify_player_info()
                self.player.update_name(True) # on force l'update de l'affichage du nom

    def start(self):
        while self.continuer:
            self.process_event()
            self.render()
            pygame.display.flip()    
            self.clock.tick(60)

    ###### Interface

    def modify_player_info(self):
        self.player.info.color = self.selectors.list["color"].get_selected()
        self.player.info.name  = self.input.text

    def get_player_info(self):
        return self.player.info