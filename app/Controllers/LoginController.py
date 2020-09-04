# This one the login controller
from app.LoginRegister import LoginRegister

class LoginController:
    ''' LoginController:
            This class controlles all the login activities / request
    '''
    def check(self, rq_cred):
        '''check(self, rq_cred):
            self: very first argument of a method
            rq_cred:  credentials passed as arguments

            This method calls the login method of LoginRegister model
            for checking the login credentails of the user

            returns data provided by the model
        '''
        model = LoginRegister()
        return model.login(rq_cred)
