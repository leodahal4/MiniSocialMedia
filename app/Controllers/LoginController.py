# This one the login controller
from app.LoginRegister import LoginRegister

class LoginController:
    ''' LoginController:
            This class controlles all the login activities / request
    '''
    def check(self, rq_cred):
        print("[CHECK] checking the credentials")
        model = LoginRegister()
        return model.login(rq_cred)
