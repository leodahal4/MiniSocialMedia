class Routes:
    def __init__(self, master, source, destination):
        print(master, source, destination)
        if destination == "register":
            from resources.views.register import RegisterForm
            RegisterForm(master)
        elif destination == 'login':
            from resources.views.login import LoginForm
            LoginForm(master)
        else:
            from resources.views.login import LoginForm
            LoginForm(master)
