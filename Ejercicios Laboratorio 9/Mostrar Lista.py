                                    #Lista simple
class LinkedList:
    def init(self):
        self.head = None
def show_list(self):
    current = self.head
    while current:
        print(current.data)
        current = current.next

                                    #Lista circular
class CircularLinkedList:
    def init(self):
        self.head = None
def show_list(self):
    if self.head is None:
        return
    current = self.head
    while current.next != self.head:
        print(current.data)
        current = current.next
    print(current.data)
