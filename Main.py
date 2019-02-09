
import pygame
import sys
import os
import time
from pygame.locals import *

from Personagem import *
from Mapa import *
from IC import *
from Reitoria import *


class Main:

    try:
        pygame.init()

    except:
        print("Erro ao inicializar o pygame")

    fundoBranco = (255, 255, 255)

    larguraTela = 916
    alturaTela = 510

    pygame.display.set_mode((larguraTela, alturaTela))

    # Titulo do jogo
    pygame.display.set_caption("OlaUfal")

    execJogo = True

    Personagem = Personagem()
    Mapa = Mapa()
    IC = IC()
    Reitoria = Reitoria()

    # Tela de fundo será branca
    janela = pygame.display.set_mode(
        (larguraTela, alturaTela)).fill(fundoBranco)

    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0xFF, 0xFF, 0xFF))

    # Loop do jogo
    while execJogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execJogo = False
            elif event.type == KEYDOWN:
                Personagem.move()

        # Atualiza a tela
        screen.blit(background, (0, 0))
        # Personagem aparece na tela

        Mapa.blit()
        Personagem.blit()

    # Encontra a posição do personagem
    # personagem.posXY();

        if (Personagem.posX == 400 and Personagem.posY == 85):
            print("IC")
            IC.blit()

        if (Personagem.posX == 130 and Personagem.posY == 245):
            print("Reitoria")
            Reitoria.blit()

        pygame.display.flip()

        pygame.display.update()

    pygame.quit()
