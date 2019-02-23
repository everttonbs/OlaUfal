
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
        #(larguraTela, alturaTela)).fill(fundoBranco)

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

        if(personagem.posX >= 110 and personagem.posX <= 130 and personagem.posY >= 205 and personagem.posY <= 225):
            print("FDA")
            fda.blit()
        #elif (personagem.posX == 220 and personagem.posY == 335):
        elif(personagem.posX >= 208 and personagem.posX <= 228 and personagem.posY >= 325 and personagem.posY <= 345):
            print("Famed")
            famed.blit()

        #elif (personagem.posX == 360 and personagem.posY == 255):
        elif(personagem.posX >= 350 and personagem.posX <= 370 and personagem.posY >= 249 and personagem.posY <= 269):
            print("Biblioteconomia")
            biblioteconomia.blit()

        #elif(personagem.posX == 320 and personagem.posY == 285):
        elif (personagem.posX >= 312 and personagem.posX <= 332 and personagem.posY >= 279 and personagem.posY <= 299):
            print("Saude")
            saude.blit()

        elif (personagem.posX >= 320 and personagem.posX <= 340 and personagem.posY >= 405 and personagem.posY <= 425):
        #elif (personagem.posX == 330 and personagem.posY == 405):
            print("ICBS")
            icbs.blit()
        elif (personagem.posX >= 432 and personagem.posX <= 452 and personagem.posY >= 233 and personagem.posY <= 248):
        #elif (personagem.posX == 440 and personagem.posY == 235):
            print("Cedu")
            cedu.blit()

        elif (personagem.posX >= 432 and personagem.posX <= 452 and personagem.posY >= 311 and personagem.posY <= 331):
        #elif (personagem.posX == 440 and personagem.posY == 315):
            print("Psicologia")
            psicologia.blit()

        elif (personagem.posX >= 446 and personagem.posX <= 466 and personagem.posY >= 205 and personagem.posY <= 220):
        #elif (personagem.posX == 460 and personagem.posY == 205):
            print("IM")
            im.blit()

        elif (personagem.posX >= 500 and personagem.posX <= 520 and personagem.posY >= 239 and personagem.posY <= 254):
        #elif (personagem.posX == 510 and personagem.posY == 245):
            print("FEAC")
            feac.blit()

        elif (personagem.posX >= 528 and personagem.posX <= 548 and personagem.posY >= 195 and personagem.posY <= 215):
        #elif (personagem.posX == 540 and personagem.posY == 195):
            print("Social")
            servSocial.blit()

        elif (personagem.posX >= 562 and personagem.posX <= 582 and personagem.posY >= 307 and personagem.posY <= 322):
        #elif (personagem.posX == 570 and personagem.posY == 305):
            print("Letras")
            letras.blit()

        elif (personagem.posX >= 594 and personagem.posX <= 614 and personagem.posY >= 245 and personagem.posY <= 260):
        #elif (personagem.posX == 600 and personagem.posY == 245):
            print("ICHICA")
            ichica.blit()
        elif (personagem.posX >= 576 and personagem.posX <= 596 and personagem.posY >= 65 and personagem.posY <= 80):
        #elif (personagem.posX == 580 and personagem.posY == 65):
            print("CTEC")
            ctec.blit()

        elif (personagem.posX >= 558 and personagem.posX <= 585 and personagem.posY >= -1 and personagem.posY <= -1):
        #elif (personagem.posX == 570 and personagem.posY == -5):
            print("Arquitetura")
            arquitetura.blit()

        elif (personagem.posX >= 502 and personagem.posX <= 522 and personagem.posY >= 123 and personagem.posY <= 138):
        #elif (personagem.posX == 510 and personagem.posY == 135):
            print("IQB")
            iqb.blit()

        elif (personagem.posX >= 474 and personagem.posX <= 494 and personagem.posY >= 43 and personagem.posY <= 58):
        #elif (personagem.posX == 480 and personagem.posY == 45):
            print("COS")
            cos.blit()
        elif (personagem.posX >= 418 and personagem.posX <= 438 and personagem.posY >= 151 and personagem.posY <= 166):
        #elif (personagem.posX == 410 and personagem.posY == 155):
            print("IF")
            fisica.blit()

        elif (personagem.posX >= 380 and personagem.posX <= 400 and personagem.posY >= 55 and personagem.posY <= 70):
        #elif (personagem.posX == 390 and personagem.posY == 55):
            print("IC")
            ic.blit()

        elif (personagem.posX >= 388 and personagem.posX <= 408 and personagem.posY >= 129 and personagem.posY <= 144):
        #elif (personagem.posX == 380 and personagem.posY == 125):
            print("ICAT")
            icat.blit()

        elif (personagem.posX >= 360 and personagem.posX <= 380 and personagem.posY >= 153 and personagem.posY <= 168):
        #elif (personagem.posX == 370 and personagem.posY == 155):
            print("Geografia")
            geografia.blit()

        elif (personagem.posX >= 212 and personagem.posX <= 232 and personagem.posY >= 97 and personagem.posY <= 112):
        #elif (personagem.posX == 220 and personagem.posY == 95):
            print("Ed. Fis")
            edFisica.blit()

        else:
            pass



        pygame.display.flip()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    pygame.quit()
