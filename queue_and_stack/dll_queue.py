from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # FIFO
        # Why is our DLL a good choice to store our elements?
        # Bec it has buit-in methods that allow us to
        # easily remove from the head and add to the tail
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 1:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size
