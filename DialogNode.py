
from enum import Enum

class NODE_TYPE(Enum):
    MULTIPLE_CHOICE = 0 # Quando houver multiplas ramificações. Múltiplos ponteiros e labels
    LINEAR = 1          # Quando houver uma única ramificação. Ponteiro único sem label
    END = 2             # Quando quando. Sem ponteiros.

class DialogNode:
    def __init__(self, text, id):
        self.text = text        # Texto do nó atual
        self.id = id            # Id do nó atual
        self.node_pointers = []  # Array de índices das ramificações
        self.node_labels  = []   # Array de labels das ramificações
        self.type = NODE_TYPE.END # Inicializa como nó final
        print('DialogNode init')

    def add_choice(self, pointer_id, pointer_label):
        """
        Adiciona uma opção de ramificação ao nó atual
        """
        print('DialogNode add_pointer')
        if (self.type == NODE_TYPE.LINEAR):
            self.node_pointers.clear()

        self.node_pointers.append(pointer_id)
        self.node_labels.append(pointer_label)
        self.type = NODE_TYPE.MULTIPLE_CHOICE;

    def make_linear(self, pointer_id):
        print('DialogNode make_linear')
        """
        Transforma em linear e adiciona a devida ramificação
        """
        self.node_pointers.clear()
        self.node_labels.clear()
        self.node_pointers.append(pointer_id)
        self.type = NODE_TYPE.LINEAR
