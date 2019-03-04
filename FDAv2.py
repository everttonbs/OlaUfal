import pygame, sys, os, time
from pygame.locals import *
from DialogManager import *
from DialogUI import *

class Fda:
    def __init__(self):
        # Instanciando o controlador de diálogo
        self.dialog_manager = DialogManager()
        node = DialogNode('HelloWorld! By BG!', 0)
        self.dialog_manager.add_node( node, set_current=True )

        # Instanciando o UI de diálogo
        self.dialog_ui = DialogUI()
        self.dialog_ui.create_choices(['1 - Descrição', '2 - Area atuação', '3 - Fotos'])
        self.dialog_ui.create_text("Tendência nacional dos cursos jurídicos é o interesse crescente em concursos públicos.\
Por essa razão, o projeto pedagógico do curso privilegiou a formação em Direito público.\
Outra vertente do curso de Direito da UFAL é a ênfase em conteúdos que capacitem o \
profissional a atuar em vários espaços de exercício de cidadania, de movimentos populares e \
de organizações não governamentais, em demanda crescente de serviços jurídicos próprios.")

    def input(self, keys):
        if keys[pygame.K_1]:
            self.dialog_ui.set_option(0)
        elif keys[pygame.K_2]:
            self.dialog_ui.set_option(1)
        elif keys[pygame.K_3]:
            self.dialog_ui.set_option(2)

    def update(self):
        self.dialog_ui.update()

    def draw(self):
        self.dialog_ui.draw()
