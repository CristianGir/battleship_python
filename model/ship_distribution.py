
class Ship_Distribution:
    def __init__(self, ship, state, coordinates, condition):
        self.ship = ship
        self.state = state
        self.coordinates = coordinates
        self.condition = condition

    def __init__(self, ship):
        self.ship = ship
        self.coordinates = []
        self.state = "FREE"
        for i in range(ship.num_places):
            self.coordinates.append(None)
