import pygame
from pygame import locals as const
from constantes import *

class Player():

    def __init__(self, playerId):
    	self.playerId = playerId
    	self.connected = False