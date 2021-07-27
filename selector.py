import pygame
from pygame import locals as const

from constantes import *

class Selectors:
    def __init__(self, ecran):
        self.ecran = ecran
        self.list  = {}

    def add(self, valName, values, pos):
        self.list[valName] = Selector(self.ecran,valName,values,pos,SELECTOR_SIZE)

    def collide(self,pos):
        isCollide = False
        for selector in self.list.values() :
            isCollide |= selector.collide(pos)
        return isCollide

    def render(self):
        for selector in self.list.values() :
            selector.render()

class Selector:
    def __init__(self, ecran, valName, values, pos, size):
        self.ecran = ecran
        self.values = values
        self.pos = pos
        self.size = size
        self.valName = valName

        self.selectedIndex = 0
        self.previous = Arrow(self,0)
        self.next     = Arrow(self,1)
        self.disp     = Display(self)

    # Vérifie si on a cliqué sur une des fléches
    def collide(self,pos):
        return self.previous.collide(pos) or self.next.collide(pos)

    def render(self):
        self.previous.render()
        self.next.render()
        self.disp.render()

    def get_selected(self):
        return self.values[self.selectedIndex]

class Display:
    def __init__(self,selector):
        self.selector = selector

    def render(self):
        font = pygame.font.SysFont(None,SELECTOR_TEXT_SIZE) 
        text = font.render(self.selector.valName.capitalize(), 1, (255,255,255))
        self.selector.ecran.blit(text, (self.selector.pos[0] - text.get_width()/2, self.selector.pos[1] - text.get_height()/2))

class Arrow:
    def __init__(self,selector,typeArrow):
        self.selector = selector
        self.type     = typeArrow

        self.image = pygame.image.load(ARROW_TEXTURE)
        self.image = pygame.transform.scale(self.image,ARROW_SIZE)
        self.hitbox = self.image.get_rect()

        # Flèche de gauche (Previous)
        if self.type == 0 :
            self.image = pygame.transform.rotate(self.image, 180) # On la fait tourner à 180
            self.hitbox.midleft = [self.selector.pos[0] - self.selector.size[0]//2, self.selector.pos[1]] 
        else:
            self.hitbox.midright = [self.selector.pos[0] + self.selector.size[0]//2, self.selector.pos[1]]  

        self.pos = self.hitbox.topleft
        
    # Vérifie si on a cliqué dessus
    def collide(self,pos):
        isCollide = self.hitbox.collidepoint(pos)
        maxval = len(self.selector.values) - 1

        if isCollide :

            # Flèche de gauche (Previous)
            if self.type == 0 :
                if self.selector.selectedIndex <= 0 :
                    self.selector.selectedIndex = maxval
                else :
                    self.selector.selectedIndex -= 1

            # Flèche de droite (Next)
            else:
                if self.selector.selectedIndex >= maxval:
                    self.selector.selectedIndex = 0
                else :
                    self.selector.selectedIndex += 1

        return isCollide

    def render(self):
        self.selector.ecran.blit(self.image, self.pos)
        # pygame.draw.rect(self.selector.ecran,GREEN,self.hitbox,1)