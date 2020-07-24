from tkinter import *
from config import Global_all
import hashlib
from tkinter import Frame, StringVar, Entry, Button, END, Label, FLAT
from tkinter import GROOVE, RIDGE, Tk
from PIL import Image, ImageTk
import fontawesome as fa


class LoginForm(Frame):
    '''loginForm
        This class is responsible for generating the form which is used
        to log in to the system.
    '''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.__primary_color="blue"
        # declare the global configurations
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__backgorud_color = returned[3]

        self.master.config(bg=self.__backgorud_color)
        # bind ENTER key or RETURN key to the login button
        self.master.bind("<Return>", lambda x: self.__login())
        # now pass the program flow to create_all_fields
        self.__create_all_fields()

    def __callback_for_change(self, *args):
        self.__user_name.delete(0, END)

    def __create_all_fields(self):
        """create_all_fields
                This function is responsible for creating all the entries and
                buttons on the window for making a successfull login
        """

        # Create a button for registering the user
        register_button = Button(
            self.master,
            bg=self.__backgorud_color,
            text="Register?",
            width=10,
            font=(self.__font_family, 10),
            relief=FLAT,
            command=self.register
        )
        register_button.place(x=570, y=3)

        self.__loginHead = Label(
            self.master,
            width=10,
            bd=0,
            relief="flat",
            text="Login",
            bg=self.__backgorud_color,
            font=(self.__font_family, 15)
        )
        self.__loginHead.place(height=40, x=250, y=130)
        # Create username field with a label on the top of it.
        self.__user_name = StringVar()
        self.__user_name = Entry(
            self.master,
            relief=FLAT,
            bg=self.__backgorud_color,
            font=("monospace", self.__font_size),
            textvariable=self.__user_name,
            width=22,
            highlightcolor=self.__primary_color,
            selectforeground="green",
            bd=0
        )
        self.__user_name.insert(0, 'Username')
        self.__user_name.place(height=50, x=250, y=180)
        self.__user_name.bind("<Button-1>", self.__callback_for_change)

        # Create a password field with a label on the top of it.
        # Global password
        self.__password = StringVar()
        self.__password = Entry(
            self.master,
            bg=self.__backgorud_color,
            font=("monospace", self.__font_size),
            width=16,
            bd=0,
            show="\u2022",
            relief=FLAT,
            textvariable=self.__password,
            highlightcolor=self.__primary_color,
            selectforeground="green"
        )
        self.__password.place(height=50, x=250, y=270)

        # Show pass eye button
        self.eye_show = Button(
            self.master,
            bg=self.__backgorud_color,
            bd=0,
            width=4,
            text=fa.icons['eye'],
            font=(self.__font_family, self.__font_size - 2),
            command=self.show,
            activeforeground=self.__primary_color
        )
        self.eye_show.place(height=50, x=410, y=270)

        # Hide pass eye button
        self.eye_hide = Button(
            self.master,
            bg=self.__backgorud_color,
            text=fa.icons['eye-slash'],
            width=4,
            font=(self.__font_family, self.__font_size - 2),
            bd=0,
            command=self.hide,
            activeforeground=self.__primary_color
        )

        self.error_label = Label(
            fg="red",
            bd=0,
            bg=self.__backgorud_color,
            font=(self.__font_family, self.__font_size - 2)
        )
        self.error_label.place(x=250, y=320)

        # Create a forgot password button
        var = StringVar()
        forgot_password = Button(
            self.master,
            font=(self.__font_family, 10),
            bg=self.__backgorud_color,
            textvar=var,
            bd=0,
            command=self.forgot_pass,
            relief=FLAT
        )
        var.set("Forgot Password?")
        forgot_password.place(x=310, y=340)

        # Create the login Button
        self.__login_button = Button(
            self.master,
            bg=self.__backgorud_color,
            text="Login",
            font=(self.__font_family, self.__font_size),
            width=10,
            command=self.__login,
            bd=0,
            underline=0
        )
        self.__login_button.place(x=280, y=390)

    def show(self):
        self.__password.config(show="")
        self.eye_show.place_forget()
        self.eye_hide.place(height=50, x=410, y=270)

    def hide(self):
        self.__password.config(show="\u2022")
        self.eye_hide.place_forget()
        self.eye_show.place(height=50, x=410, y=270)


    def forgot_pass(self):
        """forgot_pass
            This function is called whenever the user clicks on the Forgot
            Password button on the window
        """
        if (
            self.__user_name.get() == ""
        ) or (
            self.__user_name.get() == "Username"
        ):
            self.error_label.config(text="Provide Username First.")
        else:
            username = self.__user_name.get()
            self.master.destroy()
            forgot = Tk()
            forgot_password.ForgotPass(forgot, user=username)
            forgot.mainloop()

    def __login(self):
        """login
            This is the gateway for the user to login.
            This function checks whether the user provied id and password
            matches to the id and password on the databases.
        """
        global all
        self.error_label.config(text="")
        self.__provided_user_name = self.__user_name.get()
        self.__provided_password = self.__password.get()
        if self.__provided_user_name == "" or self.__provided_password == "":
            self.error_label.config(text="Fill the credentials")
            return 0
        else:
            try:
                with open("database/user_names") as all_users:
                    users = all_users.readlines()
                    for i in users:
                        if self.__provided_user_name+"\n" == i:
                            try:
                                with open(
                                    "database/user_details/"+
                                    self.__provided_user_name,
                                    "r"
                                ) as details:
                                    original_password = details.readline()
                                    encoded_provided_pass = hashlib.md5(
                                        self.__provided_password.encode()
                                    )
                                    password_hash = encoded_provided_pass.hexdigest()
                                    if (
                                        password_hash + "\n"
                                    ) == original_password:
                                        self.log_user_in()
                                    else:
                                        print("Credentials donot match")
                                        self.error_label.config(
                                            text="Credentials donot match"
                                        )
                            except:
                                self.error_label.config(
                                    text="Credentials donot match"
                                )
                            break
                        else:
                            users = all_users.readline()
                    else:
                        self.error_label.config(text="Credentials donot match")
            except:
                with open("database/user_names", "a+") as done:
                    self.__login()

    def log_user_in(self):
        global all
        try:
            user = self.__user_name.get()
            with open("loggedin", "w") as logged_user:
                logged_user.write(user)
        except:
            pass
        self.destroy()
        self.master.destroy()
        my_root_app = Tk()
        my_root_app.resizable(False, False)
        my_app = mainClass(master=my_root_app, scheme="logged_in")
        my_app.mainloop()

    def register(self):
        """register
            What if user has no id?
            After pressing Register button this function executes
        """
        self.master.destroy()
        my_root_app = Tk()
        my_root_app.resizable(False, False)
        my_app = mainClass(master=my_root_app, scheme="register")
        my_app.mainloop()
