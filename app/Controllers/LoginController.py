# This one the login controller
class LoginController:
    ''' LoginController:
            This class controlles all the login activities / request
    '''
    def __init__(self, rq_cred):
        self.__credentials = rq_cred
        print('loginContoller says ', end="\t")
        print(self.__credentials)
