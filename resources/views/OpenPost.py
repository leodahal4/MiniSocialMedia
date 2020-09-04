from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import DISABLED, NORMAL
from validation.send_to_server import Send
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
import json
import fontawesome as fa
from Config.config import Global_all


class OpenPost:
    def __init__(self, canvas, clickedPostId, master):
        self.canvas = canvas
        self.master = master
        self.clickedPostId = clickedPostId
        # declare the global configurations
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__backgorud_color = returned[3]
        self.get_post()
        self.__draw_contents()
        self.__getComments()

    def __draw_contents(self):
        self.backButton = Button(
            self.canvas,
            text=fa.icons['arrow-circle-left'],
            font="-size 15",
            command = self.backToAllPosts,
            bg="white",
            relief='flat'
        )
        self.backButton.place(x=10,y=5)
        self.frame = Frame(self.canvas, bg="white")
        self.canvas.create_window(
            (160,0),
            window=self.frame,
            anchor='nw',
            width="500"
        )
        for i in self.__post:
            user = "- " + self.getUser(i[3]).capitalize()
            desc = i[2]
            title = "\"" + i[1] + "\""
            if len(title) < 60:
                fill_gaps = 62 - len(title)
                title += fill_gaps*" "
            else:
                data = 1
                headTitle = title
                while True:
                    if len(headTitle) > 60:
                        title = title[:data*60] + "\n" + title[data*60:]
                        headTitle = title[data*60:]
                        data += 1
                    else:
                        title = title[:data*60] + "\n" + title[data*60:]
                        headTitle = title[data*60:]
                        break

            if len(desc) < 60:
                fill_gaps = 62 - len(desc)
                textD = title + "\n\n" + desc + fill_gaps*" "
            else:
                data = 1
                headDesc = desc
                while True:
                    if len(headDesc) > 60:
                        desc = desc[:data*60] + "\n" + desc[data*60:]
                        headDesc = desc[data*60:]
                        data += 1
                    else:
                        desc = desc[:data*60] + "\n" + desc[data*60:]
                        headDesc = desc[data*60:]
                        textD = title + "\n\n" + desc
                        break
            fill_gaps = 60 - len(user)
            user = fill_gaps*" " + user

            l = Label(
                self.frame,
                text=textD + "\n\n" + user,
                font=(self.__font_family, 10),
                pady=50,
                bg="white",
                width="300"
            )
            l.pack()

        self.likeCount = i[4]
        self.drawLikeButton()

    def checkThisLike(self):
        valid = Send()
        get_post = {
            "route": "check_like_post",
            "postId": self.clickedPostId,
            "userId": self.master.user[0]
        }
        self.__message = json.loads(valid.message(get_post))
        if self.__message == "False":
            return True
        else:
            return False

    def drawLikeButton(self):
        self.liked = self.checkThisLike()
        if self.liked:
            self.newstate = DISABLED
        else:
            self.newstate = NORMAL

        self.likeButton = Button(
            self.frame,
            text=fa.icons['thumbs-up'] + " \t " + str(self.likeCount),
            bg="white",
            command=self.likeThis,
            relief="flat",
            width="10",
            state = self.newstate
        )
        self.likeButton.pack(side=LEFT)

    def likeThis(self):
        valid = Send()
        get_post = {
            "route": "like_post",
            "postId": self.clickedPostId,
            "userId": self.master.user[0]
        }
        self.__message = json.loads(valid.message(get_post))
        if self.__message != "False":
            self.likeButton.destroy()
            self.likeCount += 1
            self.drawLikeButton()

    def get_post(self):
        valid = Send()
        get_post = {
            "route": "get_post",
            "postId": self.clickedPostId,
        }
        self.__post = json.loads(valid.message(get_post))

    def __getComments(self):
        pass

    def backToAllPosts(self):
        self.backButton.destroy()
        self.frame.destroy()
        # self.master.scrollbar.destroy()
        from resources.views.AllPosts import AllPosts
        AllPosts(self.canvas, self.master)

    def getUser(self, userId):
        getUser = {
            "route": "get_user",
            "userId": userId
        }
        valid = Send()
        reply = json.loads(valid.message(getUser))
        for i in reply:
            for j in i:
                reply = j
        return reply
