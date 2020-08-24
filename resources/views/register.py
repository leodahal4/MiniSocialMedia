from Config import image_works
from Config.config import Global_all
from PIL import Image, ImageTk
from app.Exceptions.DuplicateUserName import DuplicateUserName
from resources.views.clear_widgets import Clear
from routes.index import Routes
from tkinter import Frame, Button, Label, Entry, FLAT, END, StringVar
from tkinter import filedialog, Tk, messagebox
from validation.core_validation import CoreValidation
import hashlib
import os
import shutil


class RegisterForm(Frame):
    """RegisterForm(Frame)
        This class will create a form with different widgets in it,
        in order to make a user able to register.
        Widgets used in this class are listed below:
            Text Field : First name entry, Last name Entry, Password,
                        Username
            Button: Register, Login, Image Browser
            Image: Default Avatar and User Image
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.__user_avatar_path = ""

        # declare the global configurations
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__background_color = returned[3]
        self.create_all_fields()

    def create_all_fields(self):
        """create_all_fields
                This function is responsible for creating all the entries,
                 and the labels used for the registration process
        """

        if self.__user_avatar_path != "":
            load = Image.open(self.__user_avatar_path)
        else:
            # use the default image as the default user avatar at first
            self.__user_avatar_path = "Images/default_avatar.png"
            load = Image.open("resources/assets/default_avatar.png")
        load.resize((100, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        self.__img = Label(
            self.master,
            bg=self.__background_color,
            image=render
        )
        self.__img.image = render
        self.__img.place(x=580, y=5)

        # create a button for choosing the avatar by the user
        self.__user_avatar_browser = Button(
            self.master,
            text="Choose Avtar",
            font=(self.__font_family, 8),
            relief=FLAT,
            bg=self.__background_color,
            width=10,
            command=self.user_avtar
        )
        self.__user_avatar_browser.place(x=580, y=120)

        # Create First Name field
        self.__first_name_error_label = Label(
            self.master,
            bg=self.__background_color,
            fg="red",
            font=(self.__font_family, 8)
        )
        self.__first_name_error_label.place(x=180, y=130)
        self.__first_name_var = StringVar()
        self.first_name_entry = Entry(
            self.master,
            textvariable=self.__first_name_var,
            width=18,
            bg=self.__background_color,
            font=(self.__font_family, self.__font_size),
            relief=FLAT
        )
        self.first_name_entry.insert(0, "First Name")
        self.first_name_entry.bind(
            "<Button-1>",
            lambda x: self.first_name_entry.delete(0, END)
        )
        self.first_name_entry.place(height=50, x=120, y=80)

        # Create Last Name field
        self.__last_name_error_label = Label(
            self.master,
            text="",
            fg="red",
            bg=self.__background_color,
            font=(self.__font_family, 8),
            relief=FLAT
        )
        self.__last_name_error_label.place(x=380, y=130)
        self.__last_name_var = StringVar()
        self.__last_name_entry = Entry(
            self.master,
            textvariable=self.__last_name_var,
            width=18,
            bg=self.__background_color,
            font=(self.__font_family, self.__font_size),
            relief=FLAT
        )
        self.__last_name_entry.insert(0, "Last Name")
        self.__last_name_entry.bind(
            "<Button-1>",
            lambda x: self.__last_name_entry.delete(0, END)
        )
        self.__last_name_entry.place(height=50, x=360, y=80)

        # Create User Name field
        self.__user_name_error_label = Label(
            self.master,
            text="",
            fg="red",
            bg=self.__background_color,
            font=(self.__font_family, 8),
            relief=FLAT
        )
        self.__user_name_error_label.place(x=180, y=200)
        self.__user_name_var = StringVar()
        self.__user_name_entry = Entry(
            self.master,
            textvariable=self.__user_name_var,
            width=40,
            font=(self.__font_family, self.__font_size),
            bg=self.__background_color,
            relief=FLAT
        )
        self.__user_name_entry.insert(0, "UserName")
        self.__user_name_entry.bind(
            "<Button-1>",
            lambda x: self.__user_name_entry.delete(0, END)
        )
        self.__user_name_entry.place(height=50, x=120, y=150)

        # Create Password field
        self.__password_label = Label(
            self.master,
            font=(self.__font_family, 13),
            bg=self.__background_color,
            text="Password",
            relief=FLAT
        )
        self.__password_label.place(height=20, x=120, y=220)
        self.__password_error_label = Label(
            self.master,
            fg="red",
            font=(self.__font_family, 8),
            bg=self.__background_color,
            relief=FLAT
        )
        self.__password_error_label.place(x=180, y=300)
        # Password entry
        self.__password_var = StringVar()
        self.__entry = self.__password_entry = Entry(
            self.master,
            textvariable=self.__password_var,
            width=40,
            show="\u2022",
            bg=self.__background_color,
            font=(self.__font_family, self.__font_size),
            relief=FLAT
        )
        self.__password_entry.bind("<Key>", self.show_pass)
        self.__password_entry.place(height=50, x=120, y=250)

        # Create Re-Type Password Field
        self.__re_password_label = Label(
            self.master,
            font=(self.__font_family, 13),
            bg=self.__background_color,
            text="Re-Type Password",
            relief=FLAT
        )
        self.__re_password_label.place(height=20, x=120, y=330)
        self.__re_password_var = StringVar()
        self.__entry2 = self.__re_password_entry = Entry(
            self.master,
            textvariable=self.__re_password_var,
            show="\u2022",
            bg=self.__background_color,
            width=40,
            font=(self.__font_family, self.__font_size),
            relief=FLAT
        )
        self.__re_password_entry.bind("<Key>", self.re_show_pass)
        self.__re_password_entry.place(height=50, x=120, y=350)

        # Create Register Button
        self.__register_button = Button(
            self.master,
            text="Register",
            font=(self.__font_family, self.__font_size, self.__weight),
            bg=self.__background_color,
            relief=FLAT,
            width=10,
            command=self.register
        )
        self.__register_button.place(height=50, x=240, y=430)

        # Create a login Button
        self.__login_button = Button(
            self.master,
            text="Login",
            font=(self.__font_family, self.__font_size, self.__weight),
            relief=FLAT,
            width=10,
            bg=self.__background_color,
            command=self.login
        )
        self.__login_button.place(height=50, x=0, y=10)

    def show_pass(self, event):
        self.__entry.config(show="")
        self.__entry.after(1000, lambda: self.__entry.config(show="\u2022"))

    def re_show_pass(self, event):
        self.__entry2.config(show="")
        self.__entry2.after(1000, lambda: self.__entry2.config(show="\u2022"))

    def user_avtar(self):
        """user_avtar
                This function is responsible for creating a image browser
                for letting the user choose the image for his/her avatar.
        """
        self.__img.pi = self.__img.place_info()
        self.__img.place_forget()

        filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select a Image",
            filetypes=(
                ("jpeg files", "*.jpg"),
                ("all files", "*.*"))
        )
        self.__user_avatar_path = filename

        # now use the selected image as the avatar of the user
        crop_images = image_works.Image_work()
        self.__user_avatar_path = crop_images.crop_image(
            self.__user_avatar_path
        )
        load = Image.open(self.__user_avatar_path)

        image = load.resize((100, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)
        self.__img = Label(self.master, image=render)
        self.__img.image = render
        self.__img.place(x=580, y=5)

    def register(self):
        """register
                This function creates the different error labels
                ( if there are any ).
        """
        self.__first_name_info = self.__first_name_var.get()
        self.__password_info = self.__password_var.get()
        self.__last_name_info = self.__last_name_var.get()
        self.__re_password_info = self.__re_password_var.get()
        self.__user_name_info = self.__user_name_var.get()

        valid = CoreValidation()
        # Check for the first name
        if valid.isBlank(self.__first_name_var.get(), "First Name"):
            self.__first_name_error_label.config(text="*Required")
            self.__first_name_error_count = 1
        else:
            self.__first_name_error_label.config(text="")
            self.__first_name_error_count = 0
        # Check for the last name
        if valid.isBlank(self.__last_name_var.get(), "Last Name"):
            self.__last_name_error_label.config(text="*Required")
            self.__last_name_error_count = 1
        else:
            self.__last_name_error_label.config(text="")
            self.__last_name_error_count = 0
        # Check for the username and its length
        # i.e username length must be equal or greater than 3
        if valid.isBlank(self.__user_name_var.get(), "UserName"):
            self.__user_name_error_label.config(text="*Required")
            self.__user_name_error_count = 1
        elif valid.length(self.__user_name_var.get(), 3, "greater"):
            self.__user_name_error_label.config(
                text="*Username must be greater than 2 characters."
            )
            self.__user_name_error_count = 1
        else:
            try:
                pass
            except DuplicateUserName:
                self.__user_name_error_label.config(text="*UserName taken")

            except FileNotFoundError:
                self.__user_name_error_label.config(text="")
                self.__user_name_error_count = 0

            else:
                self.__user_name_error_label.config(text="")
                self.__user_name_error_count = 0
        # Check for the password
        if valid.isBlank(self.__password_var.get()):
            self.__password_error_label.config(text="*Enter your password")
            self.__password_error_count = 1
        elif valid.length(self.__password_var.get(), 5, "greater"):
            self.__password_error_label.config(
                text="*Passwords length must be greater than 5 characters."
            )
            self.__password_error_count = 1
        elif self.__password_info != self.__re_password_info:
            self.__password_error_label.config(text="*Passwords donot match")
            self.__password_error_count = 1
        elif not valid.length(self.__password_var.get(), 5, "greater") and (
            self.__password_info == self.__re_password_info
        ):
            print("in hre")
            from Config.check import Check_strength
            valid = Check_strength()
            password_condition = valid.password_strength(self.__password_info)
            if not password_condition:
                self.__password_error_label.config(
                    text=
                    "*Password must have one number and one UPPER case letter."
                )
                self.__password_error_count = 1
            else:
                self.__password_error_label.config(text="")
                self.__password_error_count = 0
        else:
            self.__password_error_label.config(text="")
            self.__password_error_count = 0
        self.check_errors()

    def check_errors(self):
        """check_errors
                This function checks whether there are any error labels
                left on the tk window and than if not it pass the execution
                of the program to create function.
        """
        self.__total_error = True if (
            self.__first_name_error_count or
            self.__last_name_error_count or
            self.__user_name_error_count or
            self.__password_error_count
        ) else False

        if not(self.__total_error):
            self.create()

    def login(self):
        """login
            What if user has got id?
            After pressing login button this function executes.
            This function destroys the running session and recalls
            the main class ( i.e User_management_system ) as
            setting the scheme as login
        """
        self.forget_all()
        Routes(master=self.master, source='register', destination='login')

    def forget_all(self):
        """forget_all
            This method removes all the widgets that is created by the register
            page
        """

        self.__img.image = ""
        now = Clear()
        now.this_one(
            self.first_name_entry,
            self.__first_name_error_label,
            self.__img,
            self.__last_name_entry,
            self.__last_name_error_label,
            self.__user_name_entry,
            self.__user_name_error_label,
            self.__user_avatar_browser,
            self.__register_button,
            self.__password_entry,
            self.__password_label,
            self.__password_error_label,
            self.__re_password_entry,
            self.__re_password_label,
            self.__login_button
        )

    def create(self):
        """create
                This function is called when there will be no error
                left on the window and everything will be good to go.
                This function creates first checks if there was any
                database( file ) defined already, and uses it if declared.
                Nor than this function creates a database( file )
                to save the details of the user.
        """
        self.__encoded_pass = hashlib.md5(self.__password_info.encode())
        self.__encrypted_pass = self.__encoded_pass.hexdigest()
        from validation.send_to_server import Send
        valid = Send()
        try:
            to_register = {
                "route": "register",
                "username": self.__user_name_var.get(),
                "password": self.__encrypted_pass,
                "fname": self.__first_name_var.get(),
                "lname": self.__last_name_var.get()
            }
            reply = valid.message(to_register)
            if reply == "False":
                self.__user_name_error_label.config(text="Username taken")
            elif reply == "True":
                print("database updated with provided cred")
                self.forget_all()
                Routes(master=self.master, source='register', destination='login')
            elif reply == "Error":
                raise ConnectionRefusedError
        except ConnectionRefusedError:
            messagebox.showerror(
                title="Eroor",
                message="Unable to connect to the server."
            )

    def forgot_password_form(self):
        pass
