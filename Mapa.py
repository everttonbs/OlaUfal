import pygame, sys, os, time
from pygame.locals import *

class Mapa:

    posMapaX = 0
    posMapaY = 0

    mapa_file = os.path.join("Imagem", "mapa.png")
    mapa_surface = pygame.image.load(mapa_file)
    mapa_surface.set_colorkey((0, 0xFF, 0xFF))


    def blit(self):
        screen = pygame.display.get_surface()
        screen.blit(self.mapa_surface, (self.posMapaX, self.posMapaY))




