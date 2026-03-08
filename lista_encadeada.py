class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkList:

    def __init__(self):
        self.head = None
        self._size = 0

    # Adicionar item na lisat
    def append(self, elem):
        if self.head:                   
            pointer = self.head         
            while(pointer.next):        
                pointer = pointer.next
            pointer.next = Node(elem)   
        else:
            self.head = Node(elem)      
        self._size = self._size + 1
    
    # Retornar o tamanho da lista
    def __len__(self):
        return self._size
    
    # Mostrar um item da lista
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range") 

    # Editar um item da lista   
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range") 

    # Inserir elemento no início da lista
    def insert_beginning(elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")   
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range") 






""" insert_beginning(value) — inserir elemento no início da lista
insert_end(value) — inserir elemento no final da lista
remove(value) — remover um elemento da lista
search(value) — buscar um elemento na lista
print_list() — imprimir os elementos da lista
size() — retornar o tamanho da lista
is_empty() — verificar se a lista está vazia """
