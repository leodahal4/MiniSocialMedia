from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
from PIL import Image, ImageTk
from resources.views.AllPosts import AllPosts
import fontawesome as fa
from routes.index import Routes


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
        print(self.master.winfo_children())

    def posts(self):
        AllPosts(self.canvas, self.master)

    def navbar(self):
        # Create a vertical line for seperating Nav Bar from rest of the
        # contents
        self.__font_size = 10
        self.canvas = Canvas(self.master, bg="white")
        self.canvas.create_line(150, 10, 150, 600, dash = (5, 2))
        self.canvas.pack(fill=BOTH, expand = True)

        # Username
        self.__user_name = "Leo"
        self.app_title = Label(
            self.master,
            bd=1,
            relief='flat',
            bg="white",
            text=self.__user_name if (self.__user_name) else "Username",
            font=(20)
        )
        self.app_title.place(x=100, y=5)
        self.logout = Button(
            self.master,
            relief='flat',
            text = "Logout",
            bg="white",
            command = self.logout,
            width=17,
        )
        self.logout.place(x=0, y=650)

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
