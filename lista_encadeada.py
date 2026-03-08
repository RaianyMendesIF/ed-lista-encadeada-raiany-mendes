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
    def insert_beginning(self, elem):
        pointer = self.head
        self.head = Node(elem)
        self.head.next = pointer
    
    # Inserir elemento no final da lista
    def insert_end(self, elem):
        pointer = self.head
        if pointer:
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)




## Teste

lista = LinkList()

lista.append(3)
lista.append(5)
lista.append(6)

# print("Tamanho da lista:", len(lista))
# print("Item de index 2 da lista", lista[2])
# lista[2] = 10
# print("Novo Item de index 2 da lista", lista[2])

lista.insert_beginning(20)
lista.insert_end(10)

for i in lista:
    print(i)
