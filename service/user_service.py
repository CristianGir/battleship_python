from model.user import User
from model.type_user import TypeUser

class UserService:
    def __init__(self):
        self.administrator = User("cgiraldo93759@umanizales.edu.co", "123456", TypeUser(1, "Administrador"))
        self.player_1 = User()
        self.player_2 = User()

    def list_users(self):
        list = []
        list.append(self.administrator.user_to_DTO())
        if self.player_1 is not None:
            list.append(self.player_1.user_to_DTO())
        if self.player_2 is not None:
            list.append(self.player_2.user_to_DTO())
        return list

    def create_players(self, player, num_player):
        if num_player == 1 and self.player_1 is not None:
            return "El jugador 1 ya se encuentra creado."
        if num_player == 2 and self.player_2 is not None:
            return "El jugador 2 ya se encuentra creado."
        if num_player == 1:
            self.player_1 = player
        else:
            self.player_2 = player
        return "El jugador se creó con éxito."
