import pygame, sys, os, time
from pygame.locals import *

class Reitoria:

    posReitoriaX = 0
    posReitoriaY = 0

    mapaReitoria_file = os.path.join("Imagem", "Reitoria2.png")
    mapaReitoria_surface = pygame.image.load(mapaReitoria_file)
    mapaReitoria_surface.set_colorkey((0, 0xFF, 0xFF))

    def blit(self):
        screen = pygame.display.get_surface();
        screen.blit(self.mapaReitoria_surface, (self.posReitoriaX, self.posReitoriaY))
