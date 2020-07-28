class Routes:
    def __init__(self, master, source, destination):
        print("source :" + source + "\ndestination: " + destination)
        if destination == "register":
            from resources.views.register import RegisterForm
            RegisterForm(master)
        elif destination == 'login':
            from resources.views.login import LoginForm
            LoginForm(master)
        else:
            from resources.views.login import LoginForm
            LoginForm(master)

        from_address(source, destination)

    def from_address(self, source, destination):
        # some defined paths are given below
        # destination: Dashboard -> source: login
        # destination: Register -> source: login
        # destination: Forgot password -> source: login
        # destination: Change password -> source: settings
        pass
