from tkinter import Frame, StringVar, Label, Tk, Menu, Canvas, BOTH, RIGHT
from tkinter import LEFT, Listbox, END, Scrollbar, Y, TOP, Button
from validation.send_to_server import Send
import json
import fontawesome as fa
from resources.views.AllPosts import AllPosts


class OpenPost:
    def __init__(self, canvas, clickedPostId, master):
        self.canvas = canvas
        self.master = master
        self.clickedPostId = clickedPostId
        self.get_post()
        self.__draw_contents()
        self.__getComments()

    def __draw_contents(self):
        self.backButton = Button(
            self.master,
            text=fa.icons['arrow-circle-left'],
            font="-size 15",
            command = self.backToAllPosts,
            bg="white",
            relief='flat'
        )
        self.backButton.place(x=10,y=5)
        self.frame = Frame(self.canvas)
        self.canvas.create_window(
            (160,0),
            window=self.frame,
            anchor='nw',
            width="500"
        )
        for i in self.__post:
            user = self.getUser(i[3])
            desc = i[2]
            title = user.capitalize() + " said : \"" + i[1] + "\""
            if len(title) < 75:
                fill_gaps = 95 - len(title)
                title += fill_gaps*" "
            else:
                data = 1
                headTitle = title
                while True:
                    if len(headTitle) > 75:
                        title = title[:data*75] + "\n" + title[data*75:]
                        headTitle = title[data*75:]
                        data += 1
                    else:
                        title = title[:data*75] + "\n" + title[data*75:]
                        headTitle = title[data*75:]
                        break

            if len(desc) < 80:
                textD = title + "\n\n" + desc + "\n"
            else:
                data = 1
                headDesc = desc
                while True:
                    if len(headDesc) > 75:
                        desc = desc[:data*75] + "\n" + desc[data*75:]
                        headDesc = desc[data*75:]
                        data += 1
                    else:
                        desc = desc[:data*75] + "\n" + desc[data*75:]
                        headDesc = desc[data*75:]
                        break

            textD = title + "\n\n" + desc
            l = Label(
                self.frame,
                text=textD,
                font="-size 10",
                pady=50,
                bg="white",
                width="300"
            )
            l.pack()

        self.likeButton = Button(
            self.frame,
            text=fa.icons['thumbs-up'] + " \t 0",
            bg="white",
            width="10"
        )
        self.likeButton.pack(side=LEFT)
        self.comment = Button(
            self.frame,
            text=fa.icons['comment-alt'] + " \t 0",
            bg="white",
            width="10"
        )
        self.comment.pack()

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
        AllPosts(self.canvas, self.master)

    def getUser(self, userId):
        getUser = {
            "route": "get_user",
            "userId": userId
        }
        from validation.send_to_server import Send
        valid = Send()
        reply = json.loads(valid.message(getUser))
        print(reply)
        print(type(reply))
        for i in reply:
            print(i)
            for j in i:
                print(j)
                reply = j
        return reply
