from model.ship import Ship

class Node:
    def __init__(self, data: Ship):
        self.data = data
        self.next = None
        self.previous = None

    def node(self):
        return Node(self.data)
    