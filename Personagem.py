import pygame, sys, os, time
from pygame.locals import *
from SpriteManager import SpriteManager

class Personagem:
    def __init__(self):
        self.posX = 0
        self.posY = 205

        # Classe auxiliar para divisao da folha de sprites
        sprite_manager = SpriteManager('Imagem/sprite_character.png', 576, 385, 12, 8)
        # Numero de sprites presentes em cada acao
        self.frames_per_action = 3
        # Dicionario das acoes possiveis
        self.sprites = {}
        self.sprites['down']  = sprite_manager.cells[0: 0+self.frames_per_action]
        self.sprites['left']  = sprite_manager.cells[12: 12+self.frames_per_action]
        self.sprites['right'] = sprite_manager.cells[24: 24+self.frames_per_action]
        self.sprites['up']    = sprite_manager.cells[36: 36+self.frames_per_action]
        # Definindo imagem atual
        self.current_action = 'down'
        self.current_frame = 0

    def blit(self):
        self.personagem_surface = self.sprites[self.current_action][self.current_frame]
        # Desenhando
        screen = pygame.display.get_surface()
        screen.blit(self.personagem_surface, (self.posX, self.posY))

    def move(self):
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.updateAction('up')
            if self.posY > 0:
                self.posY += -10
        if key[pygame.K_DOWN]:
            self.updateAction('down')
            if self.posY < 510:
                self.posY += 10
        if key[pygame.K_LEFT]:
            self.updateAction('left')
            self.current_action = 'left'
            if self.posX > 0:
                self.posX += -10
        if key[pygame.K_RIGHT]:
            self.updateAction('right')
            self.current_action = 'right'
            if self.posX < 916:
                self.posX += 10

        if key[pygame.K_ESCAPE]:
            exit()

        print(self.posX)
        print(self.posY)

    def updateAction(self, new_action):
        if new_action != self.current_action:
            self.current_action = new_action
            self.current_frame = 0
        else:
            self.current_frame = (self.current_frame + 1) % self.frames_per_action
