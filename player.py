import pygame
from pygame import locals as const
from constantes import *

import controles

class PlayerInfo():

    def __init__(self, playerId, pos, name="Deltix", color=BLACK):
        self.id = playerId
        self.pos = pos
        self.name = name
        self.color = color

        self.connected = True

    def modify(self,name,color):
        pass

    def __str__ (self):
        return "Joueur '{}':{} en {} -> {}".format(self.name,self.id,self.pos,self.color)

class Player():

    def __init__(self,playerInfo=None,ecran=None):
        self.info = playerInfo
        self.ecran = ecran

    def __str__ (self):
        return str(self.info)

    def render(self):
        # self.ecran.blit(self.image, self.pos)
        pygame.draw.circle(self.ecran,self.info.color,self.info.pos,5)

    def update(self):
        self.vect = controles.movement()
        self.info.pos[0] = self.info.pos[0] + self.vect[0]*PLAYER_SPEED
        self.info.pos[1] = self.info.pos[1] + self.vect[1]*PLAYER_SPEED
        return self.vect != [0,0]

class Players():

    def __init__(self):
        self.list = {}

    def __str__ (self):
        string = ""
        for info in self.list.values():
            string += str(info)
        return string

    def modify(self,playerInfo):
        # Si l'attribut connecté est vrai alors on update sinon on supprime
        if playerInfo.connected :
            self.list[playerInfo.id].info = playerInfo
        else :
            self.list.pop(playerInfo.id)

    def add(self,playerInfo,ecran):
        player = Player(playerInfo,ecran)
        self.list[playerInfo.id] = player

# ------

    def render(self):
        for idPlayer, player in self.list.items():
            player.render()

