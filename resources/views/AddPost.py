from tkinter import Frame, Entry


class AddPost:
    def __init__(self, canvas, master):
        self.canvas = canvas
        self.master = master
        self.__draw_components()

    def __draw_components(self):
        self.frame = Frame(self.canvas, bg="white")
        self.canvas.create_window(
            (160,50),
            window=self.frame,
            anchor='nw',
            width="500"
        )

        self.postTitle = Entry(self.frame)
        self.postTitle.pack()
