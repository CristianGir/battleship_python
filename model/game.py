from model.user import User

class Game:
    def __init__(self, id, board_1, board_2, ships_number, turn, hits_p1, hits_p2):
        self.id = id
        self.board_1 = board_1
        self.board_2 = board_2
        self.ships_number = ships_number
        self.turn = turn
        self.hits_p1 = hits_p1
        self.hits_p2 = hits_p2

    def game(self):
        pass

    def validate_sho0t(self):
        pass

    def __create_boards(self):
        pass

    def __validate_winner(self):
        pass
