from model.ship import Ship

class NodeDE:
    def __init__(self, data: Ship):
        self.data = data
        self.next = None
        self.previous = None

    def NodeDE(self, data):
        self.data = data
    