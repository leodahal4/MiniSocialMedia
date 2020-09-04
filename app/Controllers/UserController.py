from app.User import User


class UserController:
    '''UserController
        This Controller class controlls all the user related activity
    '''
    def get_user(self, userId):
        '''get_user(self, userId):
            self: very first argument of the method
            userId: the Id of the user whose details is to be fetched

            this method fetches the user from the db by calling the User model.
        '''
        model = User()
        return model.getUser(userId)

    def get_users(self, userId):
        '''get_users(self, userId):
            self: very first argument of the method
            userId: contains all the userIds to be fetched

            this method fetches the users from the db by calling the User model.
        '''
        model = User()
        return model.getUsers()
