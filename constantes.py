import pygame
from pygame import locals as const

# --- CLIENT ---

SCREEN_SIZE = (WIDTH,HEIGHT) = 700,700
BG_TEXTURE = "ressources/textures/bg.png"
# CLIENT_ICON = 
CLIENT_CAPTION = "Mii simulator"

# --- SERVER ---

SERVER_IP 	= "192.168.1.17"
SERVER_PORT = 5555
SERVER_NUMBER_MAX_CONNEXION = 5

# --- COULEURS ---

RED 	= (255, 0, 0)
GREEN 	= (0, 255, 0)
BLUE 	= (0, 0, 255)
YELLOW 	= (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN 	= (0, 255, 255)
BLACK 	= (0, 0, 0)
GRAY 	= (150, 150, 150)
WHITE 	= (255, 255, 255)

# --- CONTROLES ---

PLAYER_SPEED = 5

HAUT 	= const.K_z
GAUCHE 	= const.K_q
BAS 	= const.K_s
DROITE 	= const.K_d

CONTROLE_LIST = [HAUT, GAUCHE, BAS, DROITE]