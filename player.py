import pygame
from pygame import locals as const
from constantes import *

from random import randint
from math import floor

import controles

class PlayerInfo():

    def __init__(self, playerId, pos=[randint(0,WIDTH),randint(0,HEIGHT)], name="", color=BLACK):
        self.id = playerId
        self.pos = pos
        self.name = name
        self.color = color
        self.vect = [0,0]

        self.connected = True

    def modify(self,name,color):
        pass

    def __str__ (self):
        return "Joueur '{}':{} en {} -> {}".format(self.name,self.id,self.pos,self.color)

class Player():

    def __init__(self,playerInfo=None,ecran=None):
        self.info = playerInfo
        self.ecran = ecran

        self.old_pos = None
        self.state = PLAYER_IDLE
        self.old_state = PLAYER_IDLE
        self.anim_count = 0
        # self.anim_lock  = False
        self.init_sprites()

        self.text_image = None
        self.font = pygame.font.SysFont(None,PLAYER_FONT_SIZE)
        self.decalage_pseudo = 50
        self.update_name(True)

    def __str__ (self):
        return str(self.info)

    def random_pos(self):
        self.info.pos = [randint(0,WIDTH),randint(0,HEIGHT)]

    def update_color(self,init=False):
        for i,sublist in self.sprites.items() :
            for j,image in enumerate(sublist) : 
                new_img = pygame.PixelArray(image)

                # Si c'est à l'init, le sprite de base est forcément noir
                if init :
                    new_img.replace(BLACK, self.info.color)
                # Sinon ça pouvait être n'importe quelle couleur avant
                else :
                    for color in COLOR_LIST :
                        new_img.replace(color, self.info.color)

                # CHANGEMENT DE TAILLE
                new_img = new_img.surface
                new_img = pygame.transform.scale(new_img,[30,60]) 
                self.sprites[i][j] = new_img

    def init_sprites(self):
        self.sprites = {}
        self.sprites[PLAYER_IDLE]     = [pygame.image.load(ANIMATION_TEXTURE_IDLE)]
        self.sprites[PLAYER_FORWARD]  = self.sprites[PLAYER_IDLE] + [pygame.image.load(ANIMATION_TEXTURE_FORWARD.format(1)),pygame.image.load(ANIMATION_TEXTURE_FORWARD.format(2))]
        self.sprites[PLAYER_BACKWARD] = self.sprites[PLAYER_IDLE] + [pygame.image.load(ANIMATION_TEXTURE_BACKWARD.format(1)),pygame.image.load(ANIMATION_TEXTURE_BACKWARD.format(2))]
        self.sprites[PLAYER_LATERALE] = self.sprites[PLAYER_IDLE] + [pygame.image.load(ANIMATION_TEXTURE_LATERALE.format(1)),pygame.image.load(ANIMATION_TEXTURE_LATERALE.format(2))]
        self.sprites[PLAYER_IDLE]     = [pygame.image.load(ANIMATION_TEXTURE_IDLE)] * 3
        
        self.update_color(init=True)
        self.current_sprite = self.sprites[PLAYER_IDLE]

    # AFFICHAGE
    def render_pseudo(self):
        if self.text_image : 
            self.ecran.blit(self.text_image, self.text_rect)

    def play_animation(self):
        self.current_sprite = self.sprites[self.state][floor(self.anim_count)]
        self.anim_count += ANIMATION_FRAMERATE 

        if floor(self.anim_count) >= len(self.sprites[self.state]) :
            self.anim_count = 0

        self.old_state = self.state
        self.rec_sprite = self.current_sprite.get_rect()
        self.pos_sprite = [self.info.pos[0] - self.rec_sprite.width//2, self.info.pos[1] - self.rec_sprite.height//2]
        self.rec_sprite.topleft = self.pos_sprite

        self.ecran.blit(self.current_sprite, self.pos_sprite)

    def reset_animation(self):
        self.current_sprite = self.sprites[PLAYER_IDLE][0]
        self.anim_count = 0

    def animate(self):
        if self.old_state != self.state :
            self.reset_animation()
            
        self.play_animation()

        # pygame.draw.rect(self.ecran,RED,self.rec_sprite,1)

    def render(self):
        # pygame.draw.circle(self.ecran,self.info.color,self.info.pos,5)
        self.animate()
        self.render_pseudo()     

    # MISE à JOUR

    def update_state(self):
        if self.info.vect == [0,0] : 
            self.state = PLAYER_IDLE

        else : 
            if self.info.vect[1] > 0 : 
                self.state = PLAYER_FORWARD

            elif self.info.vect[1] < 0 :
                self.state = PLAYER_BACKWARD

            else :
                self.state = PLAYER_LATERALE

    def update_name(self,force=False):
        if self.old_pos or force:
            if self.info.name :
                if self.old_pos != self.info.pos or force :
                    self.text_image = self.font.render(self.info.name, True, PLAYER_FONT_COLOR)
                    self.text_rect  = self.text_image.get_rect()
                    self.text_rect  = [self.info.pos[0] - self.text_rect.width//2,self.info.pos[1] - self.text_rect.height//2 - self.decalage_pseudo]
        self.old_pos = self.info.pos

    # SEULEMENT POUR JOUEUR PRINCIPALE

    def update(self):
        self.info.vect = controles.movement()
        self.info.pos[0] = self.info.pos[0] + self.info.vect[0]*PLAYER_SPEED
        self.info.pos[1] = self.info.pos[1] + self.info.vect[1]*PLAYER_SPEED
        return self.info.vect != [0,0]

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

    def update(self):
        for idPlayer, player in self.list.items():
            player.update_name()
            player.update_state()
