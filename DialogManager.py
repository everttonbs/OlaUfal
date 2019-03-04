from DialogNode import *

class DialogManager:

    def __init__(self):
        self.node_dictionary = {}
        self.current_node = None

    def add_node(self, node, set_current=False):
        self.node_dictionary[node.id] = node
        if( set_current ):
            self.current_node = node

    def next_node(self, node_id):
        # Checa se o próximo nó existe nas ramificações do atual
        if node_id in self.current_node.node_pointers:
            self.current_node = node_dictionary[node_id]
            # Se existir, atualize o current e retorne true
            return true
        # Caso contrário, retorne falso
        return false

    def get_options(self):
        return current_node.node_labels

    def get_text(self):
        return current_node.text

    def get_type(self):
        return current_node.type
