import pygame, sys, os, time
from pygame.locals import *

class Personagem:
    posX = 0
    posY = 205

    personagem_file = os.path.join("Imagem", "alien22.bmp")
    personagem_surface = pygame.image.load(personagem_file)
    personagem_surface.set_colorkey((0, 0xFF, 0xFF))

    def blit(self):
        screen = pygame.display.get_surface()
        screen.blit(self.personagem_surface, (self.posX, self.posY))

    def move(self):
        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if self.posY > 0:
                self.posY += -10
        if key[pygame.K_DOWN]:
            if self.posY < 510:
                self.posY += 10
        if key[pygame.K_LEFT]:
            if self.posX > 0:
                self.posX += -10
        if key[pygame.K_RIGHT]:
            if self.posX < 916:
                self.posX += 10

        print(self.posX);
        print(self.posY);



