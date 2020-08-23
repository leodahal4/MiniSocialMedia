# This one controlles the register form
from app.LoginRegister import LoginRegister
import json

class Register:
    def __init__(self):
        pass

    def register(self, credentials):
        print("Registering user")
        model = LoginRegister()
        return model.register(credentials)
