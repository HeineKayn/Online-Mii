import pygame
from pygame import locals as const

from constantes import *
import time

class Input:
    def __init__(self, ecran, pos, text="Pseudo..."):
        self.ecran = ecran
        self.pos = pos
        self.text = text

        self.text_color = INPUT_TEXT_COLOR_UNFOCUS
        self.focus = False

        self.image = pygame.image.load(INPUT_TEXTURE)
        self.image = pygame.transform.scale(self.image,INPUT_SIZE)
        self.hitbox = self.image.get_rect()

        self.hitbox.center = self.pos
        self.pos = (self.pos[0] - self.hitbox.width/2, self.pos[1] - self.hitbox.height/2)
        
        self.font = pygame.font.SysFont(None, INPUT_TEXT_SIZE)
        self.text_image = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.midleft = self.hitbox.midleft
        self.text_rect.x += INPUT_PADDING

        self.cursor = pygame.rect.Rect(self.text_rect.topright, (3, self.text_rect.height))
        self.cursor.topleft = self.text_rect.topright

    def update(self):
        if self.focus :
            self.text_color = INPUT_TEXT_COLOR
        else :
            self.text_color = INPUT_TEXT_COLOR_UNFOCUS

        self.text_image = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.midleft = self.hitbox.midleft
        self.text_rect.x += INPUT_PADDING
        self.cursor.topleft = self.text_rect.topright

    def process_key(self,event):
        if self.focus : 
            if event.key == const.K_BACKSPACE:
                if len(self.text)>0:
                    self.text = self.text[:-1]
            else:
                if len(self.text)==0:
                    self.text = self.text.capitalize()
                self.text += event.unicode
            self.update()

    def collide(self,pos):
        self.focus = self.hitbox.collidepoint(pos)
        self.update()
        return self.focus

    def render(self):
        self.ecran.blit(self.image, self.hitbox)
        self.ecran.blit(self.text_image, self.text_rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(self.ecran, self.text_color, self.cursor)

        # pygame.draw.rect(self.ecran,GREEN,self.hitbox,1)