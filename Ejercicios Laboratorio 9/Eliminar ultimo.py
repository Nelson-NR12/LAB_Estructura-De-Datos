                            #lista simple
class Node:
    def remove_last(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
                                        #lista circular



    def remove_last(self):
        if self.head is None:
            return None
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head
