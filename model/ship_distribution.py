
class ShipDistribution:
    def __init__(self, ship):
        self.ship = ship
        self.coordinates = []
        self.state = "FREE"
        self.orientation = 0

    def validate_existing_coordinate(self, coordinate):
        if self.orientation == 0:
            return False
        for coord in self.coordinates:
            if coord.x == coordinate.x and coord.y == coordinate.y:
                return True
        return False
