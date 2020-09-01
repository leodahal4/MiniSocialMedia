from app.User import User


class UserController:
    def __init__(self):
        pass

    def get_user(self, userId):
        model = User()
        return model.getUser(userId)

    def get_users(self, userId):
        model = User()
        return model.getUsers()
