class Routes:
    def __init__(self, master, source, destination):
        print(master, source, destination)
        if destination == "register":
            from pages.register_form import RegisterForm
            RegisterForm(master)
        elif destination == 'login':
            from pages.login_form import LoginForm
            LoginForm(master)
