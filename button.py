import pygame
from pygame import locals as const

from constantes import *

class Button:
    def __init__(self, ecran, pos):
        self.ecran = ecran
        self.pos = pos

        self.image = pygame.image.load(CONFIRM_TEXTURE)
        self.image = pygame.transform.scale(self.image,CONFIRM_SIZE)
        self.hitbox = self.image.get_rect()

        self.hitbox.center = self.pos
        self.pos = (self.pos[0] - self.hitbox.width/2, self.pos[1] - self.hitbox.height/2)

    def collide(self,pos):
        return self.hitbox.collidepoint(pos)

    def render(self):
        self.ecran.blit(self.image, self.pos)
        # pygame.draw.rect(self.ecran,GREEN,self.hitbox,1)