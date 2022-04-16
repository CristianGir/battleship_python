
class Board:
    def __init__(self, id, columns, rows, player, ships_list, condition, shots_received):
        self.id = id
        self.columns = columns
        self.rows = rows
        self.player = player
        self.ships_list = ships_list
        self.condition = condition
        self.shots_received = shots_received

    def boards(self):
        pass

    def validate_shoot(self):
        pass
