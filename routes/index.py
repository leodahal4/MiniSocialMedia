class Routes:
    def __init__(self, master, source, destination):
        print("source :" + source + "\ndestination: " + destination)
        if destination == "register":
            from resources.views.register import RegisterForm
            RegisterForm(master)
        elif destination == 'login':
            from resources.views.login import LoginForm
            LoginForm(master)
        elif destination == 'home':
            if self.from_address(source, destination):
                from resources.views.home import Home
                Home(master)
        else:
            from resources.views.login import LoginForm
            LoginForm(master)

    def from_address(self, source, destination):
        if destination == "home":
            return True if source == "login" or source == "register" else False
