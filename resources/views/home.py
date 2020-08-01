from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y
from PIL import Image, ImageTk
from app.Controllers.PostController import PostController


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
        # menu bar
        # navbar
        # initial is posts
        self.menu_bar()
        self.navbar()
        self.posts()

    def forget_all(self):
        pass

    def posts(self):
        scrollbar = Scrollbar(self.master)
        # scrollbar.pack( side = RIGHT, fill = Y )
        scrollbar.place(height=690, x=686, y=0)
        self.get_posts()
        mylist = Listbox(self.master, yscrollcommand = scrollbar.set )
        for line in range(100):
            mylist.insert(END, "This is line number " + str(line))
        # mylist.pack( side = LEFT, fill = BOTH )
        mylist.place(height=690, x=160, y=5, width=430)
        scrollbar.config( command = mylist.yview )

    def get_posts(self):
        pass

    def navbar(self):
        # Create a vertical line for seperating Nav Bar from rest of the
        # contents
        self.__font_size = 10
        self.canvas = Canvas(self.master, bg="white")
        self.canvas.create_line(150, 10, 150, 600, dash = (5, 2))
        self.canvas.pack(fill=BOTH, expand = True)

        # Username
        self.__user_name = "Leo"
        app_title = Label(
            self.master,
            bd=1,
            relief='flat',
            bg="white",
            text=self.__user_name if (self.__user_name) else "Username",
            font=(20)
        )
        app_title.place(x=100, y=5)

    def quit_all(self):
        pass

    def about(self):
        pass

    def guide_user_to_use(self):
        pass

    def menu_bar(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(
            label='File',
            menu=filemenu
        )
        filemenu.add_command(
            label="Exit",
            command=self.quit_all
        )
        helpmenu = Menu(menu)
        menu.add_cascade(
            label='Help',
            menu=helpmenu
        )
        helpmenu.add_command(
            label='About',
            command=self.about
        )
        helpmenu.add_command(
            label="How to use?",
            command=self.guide_user_to_use
        )
