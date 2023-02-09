                                    #Lista simple
class Node:
    def remove_start(self):
        if self.head is None:
            return None
        self.head = self.head.next

                                    #Lista circular
class CircularLinkedList:
    def init(self):
        self.head = None                                       

    def remove_start(self):
        if self.head is None:
            return None
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next
