from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
from validation.send_to_server import Send
import json


class OpenPost:
    def __init__(self, canvas, clickedPostId):
        self.canvas = canvas
        self.clickedPostId = clickedPostId
        self.get_post()
        self.__draw_contents()
        self.__getComments()

    def __draw_contents(self):
        self.frame = Frame(self.canvas)
        self.canvas.create_window(
            (160,50),
            window=self.frame,
            anchor='nw',
            width="500"
        )
        for i in self.__post:
            title = i[3].capitalize() + " said : \"" + i[1] + "\""
            if len(title) < 95:
                fill_gaps = 95 - len(title)
                title += fill_gaps*" "

            desc = i[2]
            if len(desc) > 80:
                textD = title + "\n\n" + desc[:75] + "\n" + desc[75:]
            else:
                textD = title + "\n\n" + desc
            l = Button(
                self.frame,
                text=textD,
                font="-size 10",
                pady=50,
                bg="white",
                width="300"
            )
            l.pack()

    def get_post(self):
        valid = Send()
        get_post = {
            "route": "get_post",
            "postId": self.clickedPostId,
        }
        self.__post = json.loads(valid.message(get_post))

    def __getComments(self):
        pass
