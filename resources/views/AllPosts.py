from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
from app.Controllers.PostController import PostController
import json
from Config.config import Global_all
from validation.send_to_server import Send



class AllPosts:
    def __init__(self, canvas, master):
        self.canvas = canvas
        # declare the global configurations
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__backgorud_color = returned[3]
        self.get_posts()
        self.master = master
        self.__allPosts()
        try:
            self.master.scrollbar.destroy()
        except:
            pass

        self.drawScrollBar()
        self.canvas.create_line(150, 10, 150, len(self.__posts)*100+20, dash = (5, 2))
        self.canvas.pack(fill=BOTH, expand = True)

    def drawScrollBar(self):
        self.master.scrollbar = Scrollbar(self.master, command=self.canvas.yview)
        self.master.scrollbar.place(height=690, x=686, y=0)
        self.canvas.configure(yscrollcommand = self.master.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_configure)

    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def __allPosts(self):
        self.frame = Frame(self.canvas, bg="white")
        self.canvas.create_window(
            (160,50),
            window=self.frame,
            anchor='nw',
            width="500"
        )
        for i in self.__posts:
            user = self.getUser(i[3])
            title = "\' " + i[1] + " \'"
            if len(title) < 55:
                fill_gaps = 55 - len(title)
                title += fill_gaps*" "
            else:
                title = title[:55] + " \'..."

            desc = i[2]
            if len(desc) < 60:
                fill_gaps = 60 - len(desc)
                textD = title + "\n\n" + desc + fill_gaps*" "
            else:
                if len(desc[60:]) > 60:
                    textD = title + "\n\n" + desc[:60] + "\n" + desc[60:118] + "..."
                else:
                    fill_gaps = 60 - len(desc[60:])
                    textD = title + "\n\n" + desc[:60] + "\n" + desc[60:] + fill_gaps*" "

            fill_gaps = 45 - len(user)
            user = fill_gaps*" " + user.capitalize()

            l = Button(
                self.frame,
                text=textD + "\n\n" + user,
                font=(self.__font_family, 10),
                command= lambda id=i[0]: self.clickThis(id),
                pady=1,
                width="300",
                bg="white"
            )
            l.pack()

    def get_posts(self):
        controller = PostController()
        self.__posts = controller.get()
        valid = Send()
        get_post = {
            "route": "get_all_posts"
        }
        self.__post = valid.message(get_post)

    def clickThis(self, clickedPostId):
        self.frame.destroy()
        # self.scrollbar.destroy()
        from resources.views.OpenPost import OpenPost
        OpenPost(self.canvas, clickedPostId, self.master)

    def getUser(self, userId):
        getUser = {
            "route": "get_user",
            "userId": userId
        }
        from validation.send_to_server import Send
        valid = Send()
        reply = json.loads(valid.message(getUser))
        for i in reply:
            for j in i:
                reply = j
        return reply
