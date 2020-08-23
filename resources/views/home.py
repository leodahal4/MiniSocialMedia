from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
from PIL import Image, ImageTk
from app.Controllers.PostController import PostController
from resources.views.OpenPost import OpenPost

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
        self.menu_bar()
        self.navbar()
        self.posts()

    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def forget_all(self):
        pass

    def posts(self):
        self.get_posts()

        self.scrollbar = Scrollbar(self.master, command=self.canvas.yview)
        self.scrollbar.place(height=690, x=686, y=0)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_configure)
        self.frame = Frame(self.canvas, bg="white")
        self.canvas.create_window(
            (160,50),
            window=self.frame,
            anchor='nw',
            width="500"
        )
        for i in self.__posts:
            title = i[3].capitalize() + " says \t" + i[1]
            if len(title) < 120:
                fill_gaps = 120 - len(title)
                title += fill_gaps*" "

            desc = i[2]
            if len(desc) > 90:
                textD = title + "\n" + desc[:90] + "\n" + desc[90:]
            else:
                textD = title + "\n" + desc
            l = Button(
                self.frame,
                text=textD,
                font="-size 8",
                command= lambda id=i[0]: self.clickThis(id),
                pady=1,
                width="300",
                bg="white"
            )
            l.pack()

    def clickThis(self, clickedPostId):
        print(str(clickedPostId) + " is clicked")
        self.frame.destroy()
        OpenPost(self.canvas, clickedPostId)


    def get_posts(self):
        controller = PostController()
        self.__posts = controller.get()

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
