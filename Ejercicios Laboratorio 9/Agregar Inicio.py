                                        #Lista simple
class Node:
    class LinkedList:
        def init(self):
            self.head = None
    def add_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

                                        #Lista circular
    class CircularLinkedList:
        def init(self):
            self.head = None
    def add_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        self.head = new_node
        current.next = self.head
