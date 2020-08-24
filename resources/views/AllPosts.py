from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
from app.Controllers.PostController import PostController


class AllPosts:
    def __init__(self, canvas, master):
        self.canvas = canvas
        self.get_posts()
        self.master = master
        self.__allPosts()

    def __allPosts(self):
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

    def get_posts(self):
        controller = PostController()
        self.__posts = controller.get()

    def clickThis(self, clickedPostId):
        print(str(clickedPostId) + " is clicked")
        self.frame.destroy()
        from resources.views.OpenPost import OpenPost
        OpenPost(self.canvas, clickedPostId, self.master)
