from DialogNode import *
from DialogUI import *

class DialogManager:

    def __init__(self):
        self.node_dictionary = {}
        self.current_node = None
        self.selection_index = 0;

    def add_node(self, node, set_current=False):
        self.node_dictionary[node.id] = node
        if( set_current ):
            self.current_node = node

    def next_node(self, selection_index):
        self.selection_index = selection_index
        next_node_id = self.current_node.node_pointers[self.selection_index]

        # Checa se o próximo nó existe nas ramificações do atual
        if next_node_id in self.current_node.node_pointers:
            self.current_node = self.node_dictionary[next_node_id]
            self.selection_index = 0
            # Se existir, atualize o current e retorne true
            return True
        # Caso contrário, retorne falso
        return False

    def get_options(self):
        return self.current_node.node_labels

    def get_text(self):
        return self.current_node.text

    def get_type(self):
        return self.current_node.type

    def get_selection(self):
        return self.selection_index

    def update_selection(self, selection_index):
        if self.current_node.check_pointer(selection_index) != -1:
            self.selection_index = selection_index

    def input(self, keys):
        if (self.get_type() == NODE_TYPE.MULTIPLE_CHOICE):
            if keys[pygame.K_1]:
                self.update_selection(0)
            elif keys[pygame.K_2]:
                self.update_selection(1)
            elif keys[pygame.K_3]:
                self.update_selection(2)
            elif keys[pygame.K_4]:
                self.update_selection(3)
            elif keys[pygame.K_5]:
                self.update_selection(4)
