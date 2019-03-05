import pygame, sys, os, time
from pygame.locals import *

class DialogUI:
    def __init__(self):
        # Configurações da tela
        self.screen_surface = pygame.display.get_surface()
        self.screen_size = self.screen_surface.get_rect().size
        print('Tamanho da tela: {}'.format(self.screen_size))
        pygame.font.init()
        # Configurações de cores e fonte
        self.fg_color = (50, 50, 50)
        self.bg_color = (255, 255, 255)
        self.text_window_color = (245, 245, 245)
        self.choice_window_color = (245, 245, 245)
        self.font_size = 20
        self.font_obj = pygame.font.Font('freesansbold.ttf', self.font_size)
        # Inicialização das janelas
        self.create_text_window()
        self.create_choice_window()
        self.create_cursor()

    def create_text_window(self):
        # Inicializando configurações da janela de texto
        self.text_window_margin_x = 0.05    # Margens relativas ao tamanho da tela
        self.text_window_margin_y = 0.05
        self.text_window_height = 0.4       # Altura relativa à altura da tela
        self.text_window_height = int(self.screen_size[1] * self.text_window_height)
        self.text_window_width = int(self.screen_size[0] * (1 - 2 * self.text_window_margin_x ) )
        # Definindo surface e rect da janela de texto
        self.text_window_surface = pygame.Surface( (self.text_window_width, self.text_window_height) )
        self.text_window_surface.fill(self.text_window_color)
        self.text_window_rect = self.text_window_surface.get_rect()
        self.text_window_rect.center = self.screen_surface.get_rect().center
        self.text_window_rect.bottom = int(self.screen_size[1] * (1 - self.text_window_margin_y) )

    def create_choice_window(self):
        # Inicializando configurações da janela de texto
        self.choice_window_margin_x = 0.05    # Margens relativas ao tamanho da tela
        self.choice_window_margin_y = 0.01
        self.choice_window_height = 0.25       # Altura relativa à altura da tela
        self.choice_window_height = int(self.screen_size[1] * self.choice_window_height)
        self.choice_window_width = int(self.screen_size[0] * (1 - 2 * self.choice_window_margin_x ) )
        # Definindo surface e rect da janela de texto
        self.choice_window_surface = pygame.Surface( (self.choice_window_width, self.choice_window_height) )
        self.choice_window_surface.fill(self.choice_window_color)
        self.choice_window_rect = self.choice_window_surface.get_rect()
        self.choice_window_rect.center = self.screen_surface.get_rect().center
        self.choice_window_rect.bottom = int( self.text_window_rect.top - self.screen_size[1] * self.choice_window_margin_y)
        # Escondendo janela de opções por padrão
        self.show_choice_window = True
        self.choices = []
        self.padding = (60, 5)
        rendered = self.font_obj.render(' ', 10, self.fg_color)
        self.font_w, self.font_h = rendered.get_size()

    def create_cursor(self):
        # Carregando a imagem do cursor
        self.cursor_image = pygame.image.load("Imagem/hand.png").convert_alpha()
        self.cursor_offset= (5, -13)

    def create_choices(self, choices):
        self.choices = choices
        self.current_choice = 0


    def create_text(self, text):
        self.text = text

    ####################################################################

    def draw_options(self):
        for index, choice in enumerate(self.choices):
            rendered = self.font_obj.render(choice, 10, self.fg_color)
            self.choice_window_surface.blit(rendered, (self.padding[0], (self.padding[1] + self.font_h)  * (index + 1)))

    def draw_choice_window(self):
        self.choice_window_surface.fill(self.choice_window_color)
        self.draw_options()
        self.draw_cursor()
        self.screen_surface.blit(self.choice_window_surface, self.choice_window_rect)

    def draw_text(self):
        # Separa a string numa lsita de caracteres
        chars = self.text.split()
        # Define as coordenadas iniciais do texto
        coord_xy = (10, 10)
        x, y = coord_xy[0], coord_xy[1]

        for schar in chars:
            char = schar + ' '
            rendered = self.font_obj.render(char, 10, self.fg_color)
            font_w, font_h = rendered.get_size()

            if ( x + font_w >= self.text_window_rect.width):
                x = coord_xy[0]
                y += font_h

                if (char == ' '):
                    x -= font_w

            self.text_window_surface.blit(rendered, (x, y))
            x += font_w


    def draw_text_window(self):
        self.text_window_surface.fill(self.text_window_color)
        self.draw_text()
        self.screen_surface.blit(self.text_window_surface, self.text_window_rect)

    def draw_cursor(self):
        self.choice_window_surface.blit(self.cursor_image, (self.cursor_offset[0], (self.padding[1] + self.font_h)  * (self.current_choice + 1) + self.cursor_offset[1]))

    def draw(self):
        # Fill screen with BG color
        self.screen_surface.fill(self.bg_color)

        # Draw options
        if (self.show_choice_window):
            self.draw_choice_window()

        # Draw text
        self.draw_text_window()

##################################################################
    def set_option(self, index):
        self.current_choice = index

    def update(self, selection_index):
        # Cuide de animações
        pass
