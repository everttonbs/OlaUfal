import pygame, sys, os, time
from pygame.locals import *

class IM:

    posX = 0
    posY = 0

    mapa_file = os.path.join("Imagem", "temporario.png")
    mapa_surface = pygame.image.load(mapa_file)
    mapa_surface.set_colorkey((0, 0xFF, 0xFF))

    def blit(self):
        screen = pygame.display.get_surface();0
        screen.blit(self.mapa_surface, (self.posX, self.posY))