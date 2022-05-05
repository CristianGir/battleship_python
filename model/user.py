from model.type_user import Type

class User:
    def __init__(self, id, mail, password, type_user):
        self.id = id
        self.mail = mail
        self.password = password
        self.type_user = type_user

    def user(self, email, password, type_user):
        self.email = email
        self.password = password
        self.type_user = type_user
