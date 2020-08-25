from PIL import Image, ImageTk
from PIL import Image, ImageTk
from resources.views.AllPosts import AllPosts
from routes.index import Routes
from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
import fontawesome as fa


class Home(Frame):
    '''Home:
        This is the default window or View that will be executed after the
        user logs in to the system.
    '''
    def __init__(self, master):
        self.master = master
        self.master.title("Home")

        self.__create_all_fields()

    def __create_all_fields(self):
        # self.menu_bar()
        self.navbar()
        self.posts()
        self.drawScrollBar()

    def forget_all(self):
        for child in self.master.winfo_children():
            child.destroy()

    def posts(self):
        AllPosts(self.canvas, self.master)

    def navbar(self):
        # Create a vertical line for seperating Nav Bar from rest of the
        # contents
        self.__font_size = 10
        self.canvas = Canvas(self.master, bg="white")
        self.canvas.create_line(150, 10, 150, 600, dash = (5, 2))
        self.canvas.pack(fill=BOTH, expand = True)

        self.__user_avatar_path = "Images/default_avatar.png"

        # now use the selected image as the avatar of the user
        self.__user_avatar_path = "Images/default_avatar.png"
        load = Image.open("resources/assets/default_avatar.png")
        load.resize((100, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        self.__img = Label(
            self.master,
            bg="white",
            image=render
        )
        self.__img.image = render
        self.__img.place(x=10, y=50)

        # Username
        self.__user_name = "Leo"
        self.app_title = Label(
            self.master,
            bd=1,
            relief='flat',
            bg="white",
            text=self.__user_name if (self.__user_name) else "Username",
            font=(20),
            width=16
        )
        self.app_title.place(x=0, y=160)
        self.homeButton = Button(
            self.master,
            relief='flat',
            text=fa.icons["home"] + "\tHome      ",
            width=15,
            bg="white",
            command=self.homeView,
            font="-size 11"
        )
        self.homeButton.place(x=0, y=190)

        self.addPostButton = Button(
            self.master,
            relief='flat',
            text=fa.icons["plus-square"] + "\tAdd Post",
            width=15,
            bg="white",
            command=self.addPostView,
            font="-size 11"
        )
        self.addPostButton.place(x=0, y=220)
        self.messagesButton = Button(
            self.master,
            relief='flat',
            text=fa.icons["envelope"] + "\tMessages",
            width=15,
            font="-size 11",
            bg="white"
        )
        self.messagesButton.place(x=0, y=250)

        self.logoutButton = Button(
            self.master,
            relief='flat',
            text = "Logout",
            bg="white",
            command = self.logout,
            width=17,
        )
        self.logoutButton.place(x=0, y=650)

    def logout(self):
        self.forget_all()
        Routes(master=self.master, source="home", destination="login")

    def drawScrollBar(self):
        self.scrollbar = Scrollbar(self.master, command=self.canvas.yview)
        self.scrollbar.place(height=690, x=686, y=0)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_configure)

    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def addPostView(self):
        for child in self.canvas.winfo_children():
            child.destroy()
        from resources.views.AddPost import AddPost
        AddPost(self.canvas, self.master)

    def homeView(self):
        for child in self.canvas.winfo_children():
            child.destroy()
        AllPosts(self.canvas, self.master)
