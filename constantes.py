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

LIGHT_GRAY 	= (200, 200, 200)

COLOR_LIST = [RED,GREEN,BLUE,YELLOW,MAGENTA,CYAN,BLACK]

# --- PLAYER --- 

PLAYER_FONT_SIZE = 28 
PLAYER_FONT_COLOR = WHITE
PLAYER_NAME_MAX_LEN = 21

# --- MENU ---

SELECTOR_SIZE = (500,200)
ARROW_TEXTURE = "ressources/textures/arrow.png"
ARROW_SIZE    = (100,60)
SELECTOR_TEXT_SIZE = 30

CONFIRM_SIZE  	 = (140,80)
CONFIRM_TEXTURE  = "ressources/textures/confirm.png"

INPUT_SIZE    	 = (300,80)
INPUT_TEXTURE 	 = "ressources/textures/input.png"
INPUT_TEXT_SIZE  = 34
INPUT_TEXT_COLOR = WHITE
INPUT_TEXT_COLOR_UNFOCUS = LIGHT_GRAY
INPUT_PADDING    = 20

# --- CONTROLES ---

PLAYER_SPEED = 5

HAUT 	= const.K_z
GAUCHE 	= const.K_q
BAS 	= const.K_s
DROITE 	= const.K_d

CONTROLE_LIST = [HAUT, GAUCHE, BAS, DROITE]

