from Config.config import Global_all
from tkinter import Frame, Entry, StringVar, END, Label, Button, LEFT, RIGHT
from validation.send_to_server import Send
import json


class FriendsView:
    def __init__(self, canvas, master):
        self.canvas = canvas
        self.master = master
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__backgorud_color = returned[3]
        self.create()

    def create(self):
        self.frame = Frame(
            self.canvas,
            bg="white",
            height=600
        )
        self.canvas.create_window(
            (160,50),
            window=self.frame,
            anchor='nw',
            width="500"
        )
        self.frameTitle = Label(
            self.frame,
            font=(self.__font_family, 12, "bold"),
            width=45,
            bg=self.__backgorud_color,
            text="Connect People"
        )
        self.frameTitle.place(height=60, x=10, y=-20)
        self.searchquery = StringVar()
        self.search_name = Entry(
            self.frame,
            textvariable=self.searchquery,
            bg=self.__backgorud_color,
            font=(self.__font_family, self.__font_size),
            relief='flat',
            width=35
        )
        # self.search_name.pack()
        self.search_name.insert(0, 'Enter the name')
        self.search_name.bind("<Key>", self.search_the_query)
        self.search_name.bind("<Button-1>", lambda x: self.search_name.delete(0, END)),
        self.search_name.place(height=35, x=10, y=30)

        search_button = Button(
            self.frame,
            text="Search",
            bg=self.__backgorud_color,
            font=(self.__font_family, self.__font_size),
            relief="flat",
            command=self.search_the_query
        )
        search_button.place(x=400, y=30)

        f = Frame(self.frame, height=1, width=700, bg="black")
        f.place(x=0, y=80)
        self.allUsers()

    def search_the_query(self, *args):
        print(args)

    def allUsers(self):
        self.__all_users = self.fetchUsers()
        self.totalUsers = len(self.__all_users)
        list_frame = Frame(self.frame)
        list_frame.config(borderwidth=1, width=650, bg=self.__backgorud_color)
        list_frame.place(height=250*(self.totalUsers / 6), x=0, y=120)
        index = 0
        for user in self.__all_users:
            name = Button(
                list_frame,
                font=(self.__font_family, 12),
                width=15,
                relief="flat",
                bg=self.__backgorud_color,
                text=user[2] + " " + user[3] + "\n\t" + user[1]
            )
            addFriend = Button(
                list_frame,
                relief="flat",
                bg=self.__backgorud_color,
                text="Add"
            )
            if index == 0:
                name.place(x=0, y=0)
                addFriend.place(x=180, y = 5)
            elif index == 1:
                name.place(x=250, y=0)
                addFriend.place(x=430, y = 5)
            elif (index % 2 == 0):
                name.place(x=250, y=42*index)
                addFriend.place(x=430, y = 45*index)
            else:
                name.place(x=0, y=40*(index-1))
                addFriend.place(x=180, y = 45*(index-1))
            index += 1

    def fetchUsers(self):
        valid = Send()
        get_post = {
            "route": "get_users",
            "userId": self.master.user[0]
        }
        return json.loads(valid.message(get_post))
