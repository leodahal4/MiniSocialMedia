from tkinter import Frame, Entry, FLAT, StringVar, END, Button
import fontawesome as fa


class AddPost:
    def __init__(self, canvas, master):
        self.canvas = canvas
        self.master = master
        self.__draw_components()

    def __draw_components(self):
        self.__cleared = 0
        self.frame = Frame(
            self.canvas,
            bg="white",
            height=650,
        )
        self.canvas.create_window(
            (160,50),
            window=self.frame,
            anchor='nw',
            width="500"
        )
        self.backButton = Button(
            self.canvas,
            text=fa.icons['arrow-circle-left'],
            font="-size 15",
            command = self.backToHome,
            bg="white",
            relief='flat'
        )
        self.backButton.place(x=10,y=5)

        self.__postTitle_var = StringVar()
        self.__postTitle = Entry(
            self.frame,
            relief=FLAT,
            font=("monospace", 12),
            textvariable=self.__postTitle_var,
            width=22,
            selectforeground="green",
            bd=0
        )
        self.__postTitle.insert(0, 'Enter the title')
        self.__postTitle.bind("<Button-1>", self.__callback_for_change)
        self.__postTitle.pack()

    def __callback_for_change(self, *args):
        if self.__postTitle.get() == "Username" and self.__cleared == 0:
            self.__postTitle.delete(0, END)
        self.__cleared = 1

    def backToHome(self):
        self.backButton.destroy()
        self.frame.destroy()
        from resources.views.AllPosts import AllPosts
        AllPosts(self.canvas, self.master)
