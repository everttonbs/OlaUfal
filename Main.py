
import pygame, sys, os, time

from pygame.locals import *

from Personagem import *
from Mapa import *
from Reitoria import *
from Arquitetura import *
from Biblioteconomia import *
from CEDU import *
from COS import *
from CTEC import *
from EdFis import *
from Famed import *
from FDA import *
from FEAC import *
from Geografia import *
from IC import *
from ICAT import *
from ICBS import *
from ICHICA import *
from Fisica import *
from IM import *
from IQB import *
from Letras import *
from Psicologia import *
from Saude import *
from ServSocial import *
pygame.FULLSCREEN

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

    personagem = Personagem()
    Mapa = Mapa()
    arquitetura = Arquitetura()
    biblioteconomia = Biblioteconomia()
    cedu = Cedu()
    cos = Cos()
    ctec = Ctec()
    edFisica = EdFisica()
    famed = Famed()
    fda = Fda()
    feac = Feac()
    fisica = Fisica()
    geografia = Geografia()
    ic = IC()
    icat = Icat()
    icbs = Icbs()
    ichica = Ichica()
    im = IM()
    iqb = IQB()
    letras = Letras()
    psicologia = Psicologia()
    saude = Saude()
    servSocial = ServSocial()

    # Tela de fundo sera branca
    janela = pygame.display.set_mode(
        (larguraTela, alturaTela), FULLSCREEN).fill(fundoBranco)

    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0xFF, 0xFF, 0xFF))

    FPS = 60
    FPSCLOCK = pygame.time.Clock()

    pygame.mixer.music.load('Musica/music.ogg')
    pygame.mixer.music.play()



    # Loop do jogo
    while execJogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execJogo = False

        keys = pygame.key.get_pressed()
        personagem.move(keys)

        # Atualiza a tela
        screen.blit(background, (0, 0))
        # Personagem aparece na tela

        #Verifica se a musica ainda esta tocando
        if (pygame.mixer.music.get_busy()):
            pass
        else:
            pygame.mixer.music.play()

        Mapa.blit()
        personagem.blit()

    # Encontra a posicao do personagem
    # personagem.posXY();
    #Blocos de cursos

        if (personagem.posX == 120 and personagem.posY == 215):
            print("FDA")
            fda.blit()
        elif (personagem.posX == 220 and personagem.posY == 335):
            print("Famed")
            famed.blit()

        elif (personagem.posX == 360 and personagem.posY == 255):
            print("Biblioteconomia")
            biblioteconomia.blit()

        elif (personagem.posX == 320 and personagem.posY == 285):
            print("Saude")
            saude.blit()

        elif (personagem.posX == 330 and personagem.posY == 405):
            print("ICBS")
            icbs.blit()

        elif (personagem.posX == 440 and personagem.posY == 235):
            print("Cedu")
            cedu.blit()

        elif (personagem.posX == 440 and personagem.posY == 315):
            print("Psicologia")
            psicologia.blit()

        elif (personagem.posX == 460 and personagem.posY == 205):
            print("IM")
            im.blit()

        elif (personagem.posX == 510 and personagem.posY == 245):
            print("FEAC")
            feac.blit()

        elif (personagem.posX == 540 and personagem.posY == 195):
            print("Social")
            servSocial.blit()

        elif (personagem.posX == 570 and personagem.posY == 305):
            print("Letras")
            letras.blit()

        elif (personagem.posX == 600 and personagem.posY == 245):
            print("ICHICA")
            ichica.blit()

        elif (personagem.posX == 580 and personagem.posY == 65):
            print("CTEC")
            ctec.blit()

        elif (personagem.posX == 570 and personagem.posY == -5):
            print("Arquitetura")
            arquitetura.blit()

        elif (personagem.posX == 510 and personagem.posY == 135):
            print("IQB")
            iqb.blit()

        elif (personagem.posX == 480 and personagem.posY == 45):
            print("COS")
            cos.blit()

        elif (personagem.posX == 410 and personagem.posY == 155):
            print("IF")
            fisica.blit()

        elif (personagem.posX == 390 and personagem.posY == 55):
            print("IC")
            ic.blit()

        elif (personagem.posX == 380 and personagem.posY == 125):
            print("ICAT")
            icat.blit()

        elif (personagem.posX == 370 and personagem.posY == 155):
            print("Geografia")
            geografia.blit()

        elif (personagem.posX == 220 and personagem.posY == 95):
            print("Ed. Fis")
            edFisica.blit()

        else:
            pass



        pygame.display.flip()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    pygame.quit()
