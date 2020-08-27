from tkinter import Frame, Entry, FLAT, StringVar, END, Button, Text, INSERT
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

        self.__postTitle = Text(
            self.frame,
            relief=FLAT,
            font=("monospace", 12),
            width=45,
            selectforeground="green",
            bd=0,
            pady=5,
            padx=5
        )
        self.__postTitle.insert(INSERT, 'Enter the title')
        self.__postTitle.bind("<Button-1>", self.__callback_for_change)
        self.__postTitle.place(height=60, x=10, y=20)

        self.__postDescripton = Text(
            self.frame,
            relief=FLAT,
            font=("monospace", 12),
            width=45,
            selectforeground="green",
            bd=0,
            pady=5,
            padx=5
        )
        self.__postDescripton.insert(INSERT, 'Enter the Description for the post\nOver Here.')
        self.__postDescripton.bind("<Button-1>", self.__callback_for_changeDes)
        self.__postDescripton.place(height=400, x=10, y=100)

        self.__submitButton = Button(
            self.frame,
            bg="white",
            text="Submit",
            font=("monospace", 12),
            width=10,
            bd=0,
            underline=0
        )
        self.__submitButton.place(height=50, x=350, y=520)

    def __callback_for_change(self, *args):
        if self.__postTitle.get("1.0","end-1c") == "Enter the title":
            self.__postTitle.delete("1.0", END)

    def __callback_for_changeDes(self, *args):
        print(self.__postDescripton.get("1.0", "end-1c"))
        if self.__postDescripton.get("1.0","end-1c") == "Enter the Description for the post\nOver Here.":
            self.__postDescripton.delete("1.0", END)

    def backToHome(self):
        self.backButton.destroy()
        self.frame.destroy()
        from resources.views.AllPosts import AllPosts
        AllPosts(self.canvas, self.master)