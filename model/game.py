from .board import Board

class Game:
    def __init__(self, player_1, player_2, ships_list):
        self.player_1 = player_1
        self.player_2 = player_2
        self.ships_list = ships_list

    def validate_shoot(self, x, y, player):
        pass

    def create_boards(self, player_1, player_2, ships_list):
        if ships_list.count <= 9:
            self.player_1 = Board(10, 10, player_1, ships_list)
            self.player_2 = Board(10, 10, player_2, ships_list.clone_list())
        elif 10 <= ships_list.count <= 20:
            self.player_1 = Board(20, 20, player_1, ships_list)
            self.player_2 = Board(20, 20, player_2, ships_list.clone_list())
        else:
            self.player_1 = Board(30, 30, player_1, ships_list)
            self.player_2 = Board(30, 30, player_2, ships_list.clone_list())

        def validate_winner():
            pass
