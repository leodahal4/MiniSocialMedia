class Routes:
    def __init__(self, master, source, destination):
        print(master, source, destination)
        if destination == "register":
            from pages.register import RegisterForm
            RegisterForm(master)
        elif destination == 'login':
            from pages.login import LoginForm
            LoginForm(master)
        else:
            from pages.login import LoginForm
            LoginForm(master)
