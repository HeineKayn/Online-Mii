import pygame
from pygame import locals as const
from constantes import *

def movement():
	vect = [0,0]
	pressed = pygame.key.get_pressed()

	if pressed[DROITE]  :
		vect[0] += 1 

	if pressed[BAS]  :
		vect[1] += 1 

	if pressed[GAUCHE] :
		vect[0] -= 1

	if pressed[HAUT] :
		vect[1] -= 1

	return vect