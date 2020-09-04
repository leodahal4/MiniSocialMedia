# This one controlles the register form
from app.LoginRegister import LoginRegister

class Register:
    ''' Register:
            This class controlles all the register activities / request
    '''
    def register(self, credentials):
        '''register(self, rq_cred):
            self: very first argument of a method
            credentials:  credentials passed as arguments

            This method calls the register method of register model for checking
            the valid credentails of the user.

            returns data provided by the model
        '''
        model = LoginRegister()
        return model.register(credentials)
