                                            #lista simple
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class lsitaSimple:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = Nodo(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
                                            #Lista circular
class listacircular:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = Nodo(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        last_node = self.head
        while last_node.next != self.head:
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = self.head
