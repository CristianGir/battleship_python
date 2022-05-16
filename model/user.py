from .User_DTO import UserDTO

class User:
    def __init__(self, mail, password, type_user):
        self.mail = mail
        self.password = password
        self.type_user = type_user

    def user_to_DTO(self):
        user_DTO = UserDTO(self.email, self.type_user.description)
        return user_DTO
