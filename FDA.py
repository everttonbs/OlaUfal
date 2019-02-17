import pygame, sys, os, time
from pygame.locals import *


class Fda:

    posX = 0
    posY = 0
    tamanho_tela = x, y = (916, 510)
    
    #Texto na tela
    pygame.font.init()
    fonte_padrao = pygame.font.get_default_font()
    a = pygame.font.SysFont('comicsansms', 18)
    b = pygame.font.SysFont(fonte_padrao, 45)
    
    
    texto_desc_curso = "    O curso de Direito com mais de 83 anos de existência, carrega o título de curso mais antigo da UFAL. \
 A Faculdade de Direito de Alagoas é também a maior unidade acadêmica da Universidade Federal de Alagoas. São, em média, \
 850 alunos matriculados em 15 turmas distribuídas nos horários diurno e noturno."
    
    texto_area_atuacao = "  Tendência nacional dos cursos jurídicos é o interesse crescente em concursos públicos.\
 Por essa razão, o projeto pedagógico do curso privilegiou a formação em Direito público.\
 Outra vertente do curso de Direito da UFAL é a ênfase em conteúdos que capacitem o \
 profissional a atuar em vários espaços de exercício de cidadania, de movimentos populares e \
 de organizações não governamentais, em demanda crescente de serviços jurídicos próprios."
    
    mapa_file = os.path.join("Imagem", "temporario.png")
    mapa_surface = pygame.image.load(mapa_file)
    mapa_surface.set_colorkey((0, 0xFF, 0xFF))


    def texto_curso(self, screen, texto):

        lista_palavras = [lista_palavras.split(' ') for lista_palavras in texto.splitlines()]
        #Texto incia nas coordenas (x, y)
        coord_xy = (0, 175)
        space = self.a.size(' ')[0]
        #Tamanho da tela, necessario para o texto nao ultrapassar
        max_x, max_y = (916, 510)
        x, y = coord_xy
        for palavras in lista_palavras:
            for letras in palavras:
                l_surface = self.a.render(letras, 0, (255, 255, 255))                
                letras_x, letra_y = l_surface.get_size()

                if ((x + letras_x) >= max_x):
                    x = coord_xy[0]
                    y += letra_y
                
                screen.blit(l_surface, (x, y))
                x += letras_x + space

            x = coord_xy[0]
            y += letra_y     

    def blit(self):
        screen = pygame.display.get_surface()
        screen.blit(self.mapa_surface, (self.posX, self.posY))

        tela_inicial = self.b.render("  [ 1 - Descrição ]     [ 2 - Area atuação ]     [ 3 - Fotos ]", 1, (255, 255, 255))
        screen.blit(tela_inicial, (0, 175))
        #self.texto_curso(screen, self.texto_desc_curso)          
        #self.texto_curso(screen, self.texto_area_atuacao)             
        key = pygame.key.get_pressed()

        if key[pygame.K_1]:
            screen.blit(self.mapa_surface, (self.posX, self.posY))
            self.texto_curso(screen, self.texto_desc_curso)

        if(key[pygame.K_2]):
            screen.blit(self.mapa_surface, (self.posX, self.posY))
            self.texto_curso(screen, self.texto_area_atuacao)



         


        