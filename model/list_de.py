from .ship import Ship
from .node import Node

class ListDE:
    def __init__(self):
        self.head = None

    def count(self):
        if self.head is None:
            return 0
        else:
            temp = self.head
            count = 1
            while temp.next is not None:
                count += 1
                temp = temp.next
            return count

    def add(self, pet:Pet):
        if self.head is None:
            self.head = Node(pet)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(pet)

    def add_to_start(self, pet:Pet):
        if self.head is None:
            self.head = Node(pet)
        else:
            temp = self.head
            self.head = Node(pet)
            self.head.next = temp

    def validate_existing_coordinate(self):
        pass

    def clone_list(self):
        pass
