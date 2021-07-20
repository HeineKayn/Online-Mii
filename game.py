import pygame
from pygame import locals as const
from constantes import *

class Game:
    def __init__(self, ecran, clock, network, player):
        self.ecran = ecran
        self.clock = clock
        self.continuer = True
        self.bg = pygame.image.load(BG_TEXTURE)

        self.network = network
        self.player = player
    
    def prepare(self):
        pygame.key.set_repeat(1, 0)
        self.continuer = True
    
    def update_screen(self):
        self.ecran.blit(self.bg, (0, 0))

    def update_game(self):
        pass
    
    def process_event(self, event: pygame.event):

        # Click Gauche
        # if event.type == const.MOUSEBUTTONUP and event.button == 1:
        #     self.projectiles.destroy(event.pos)

        # Déplacement
        # -- if keydown and event.key is in (liste touches possible)
        # il se passe quoi si 2 touches mm temps ?
        if event.type == const.KEYDOWN and event.key == const.K_a:
            self.player.move(event.pos)
            self.network.send(self.player)

        if event.type == const.QUIT:
            self.continuer = False
    
    def start(self):
        self.prepare()
        
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)
            
            self.update_screen()
            self.update_game()

            pygame.display.flip()
            self.clock.tick(60)