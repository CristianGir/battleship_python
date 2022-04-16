from model.user_type import Type

class User:
    def __init__(self, id, mail, password, type):
        self.id = id
        self.mail = mail
        self.password = password
        self.type = type

    def user(self):
        pass
