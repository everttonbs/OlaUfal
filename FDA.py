import pygame, sys, os, time
from pygame.locals import *
from DialogManager import *

class Fda:
    def __init__(self):
        # Instanciando o controlador de diálogo
        self.dialog_manager = DialogManager()

        welcome_node = DialogNode('Olá. Que tal escolher um dos itens acima?', 0)
        welcome_node.add_choice(1, '1 - Descrição')
        welcome_node.add_choice(2, '2 - Área de Atuação')
        welcome_node.add_choice(3, '3 - Fotos')

        # Definindo os nós
        description_text = "Tendência nacional dos cursos jurídicos é o interesse crescente em concursos públicos. \
        Por essa razão, o projeto pedagógico do curso privilegiou a formação em Direito público. \
        Outra vertente do curso de Direito da UFAL é a ênfase em conteúdos que capacitem o \
        profissional a atuar em vários espaços de exercício de cidadania, de movimentos populares e \
        de organizações não governamentais, em demanda crescente de serviços jurídicos próprios."
        description_node = DialogNode(description_text, 1)
        description_node.make_linear(0)

        workarea_text = "Tendência nacional dos cursos jurídicos é o interesse crescente em concursos públicos.\
        Por essa razão, o projeto pedagógico do curso privilegiou a formação em Direito público.\
        Outra vertente do curso de Direito da UFAL é a ênfase em conteúdos que capacitem o \
        profissional a atuar em vários espaços de exercício de cidadania, de movimentos populares e \
        de organizações não governamentais, em demanda crescente de serviços jurídicos próprios."
        workarea_node = DialogNode(workarea_text, 2)
        workarea_node.make_linear(0)

        photos_text = "No futuro, você poderá ver algumas fotos sobre o bloco neste mesmo local."
        photos_node = DialogNode(photos_text, 3)
        photos_node.make_linear(0)

        # Cadastrando os nós no manager
        self.dialog_manager.add_node(welcome_node, set_current=True)
        self.dialog_manager.add_node(description_node)
        self.dialog_manager.add_node(workarea_node)
        self.dialog_manager.add_node(photos_node)

        # Instanciando o UI de diálogo
        self.dialog_ui = DialogUI()
        self.dialog_ui.create_choices( self.dialog_manager.get_options() )
        self.dialog_ui.create_text( self.dialog_manager.get_text() )

    def input(self, keys, events):
        self.dialog_manager.input(keys)

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.dialog_manager.next_node(self.dialog_manager.selection_index)
                    self.dialog_ui.create_choices( self.dialog_manager.get_options() )
                    self.dialog_ui.create_text( self.dialog_manager.get_text() )

    def update(self):
        if(self.dialog_manager.get_type() == NODE_TYPE.MULTIPLE_CHOICE):
            self.dialog_ui.show_choice_window = True
            self.dialog_ui.set_option( self.dialog_manager.selection_index )
        else:
            self.dialog_ui.show_choice_window = False

    def draw(self):
        self.dialog_ui.draw()
