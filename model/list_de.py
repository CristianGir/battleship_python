from .node_de import NodeDE

class ListDE:
    def __init__(self):
        self.head = None
        self.count = 0

    def enlist(self):
        list = []
        if self.head is not None:
            temp = self.head
            while temp is not None:
                list.append(temp.data)
                temp = temp.next
            return list
        else:
            raise Exception("La lista está vacía.")

    def add(self, ship):
        if self.head is None:
            new_node = NodeDE(ship)
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            new_node = NodeDE(ship)
            temp.next = new_node
            new_node.previous = temp
        self.count += 1

    def add_first(self, ship):
        if self.head is None:
            new_node = NodeDE(ship)
            self.head = new_node
        else:
            new_node = NodeDE(ship)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.count += 1

    def clone_list(self):
        if self.head is not None:
            new_list = ListDE()
            temp = self.head
            while temp is not None:
                new_list.add(temp.data)
                temp = temp.next
            return new_list
        else:
            raise Exception("La lista está vacía.")

    def verify_existing_coordinates(self, coordinates):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                if temp.data.orientation != 0:
                    for coord in coordinates:
                        if temp.data.validate_existing_coordinate(coord):
                            return True
                temp = temp.next
        return False
