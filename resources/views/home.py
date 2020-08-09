from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
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

    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def forget_all(self):
        pass

    def posts(self):
        self.get_posts()

        scrollbar = Scrollbar(self.master, command=self.canvas.yview)
        scrollbar.place(height=690, x=686, y=0)
        self.canvas.configure(yscrollcommand = scrollbar.set)
        self.canvas.bind('<Configure>', self.on_configure)
        frame = Frame(self.canvas, bg="white")
        self.canvas.create_window(
            (160,0),
            window=frame,
            anchor='nw',
            width="500"
        )

        # l = Button(frame, text="Hello World", font="-size 50", command=self.clickThis)
        # l.pack()
        # l = Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
        # l.pack()
        # l = Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
        # l.pack()
        # l = Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
        # l.pack()
        for i in self.__posts:
            print(i)
            print(type(i))
            l = Button(
                frame,
                text=i[1] + "\n" + i[2],
                font="-size 10",
                command=self.clickThis,
                width="300"
            )
            l.pack()

    def clickThis(self):
        print("clicked")

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
