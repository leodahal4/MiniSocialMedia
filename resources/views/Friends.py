from Config.config import Global_all
from tkinter import Frame, Entry, StringVar, END, Label, Button, LEFT, RIGHT, messagebox
from tkinter import NORMAL, DISABLED
from validation.send_to_server import Send
import fontawesome as fa
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
        self.__all_users = self.fetchUsers()
        self.__backup = self.__all_users
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
            text="Connect with People"
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
        self.search_name.insert(0, 'Enter the username')
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
        self.getFriends()
        self.allUsers()

    def search_the_query(self, *args):
        '''search_the_query(self, *args):
            self: method first argument
            *args: all the key events generated while typing the name

            This method lists all the users of the specific name typed on the
            search bar of the view.

            This method uses the list comprehension method to list down all the
            users of the name.
        '''
        search_item = self.searchquery.get()
        if search_item == "":
            self.allUsersFrame.destroy()
            self.__all_users = self.__backup
            self.allUsers()
        else:
            self.allUsersFrame.destroy()
            # self.__all_users = [user for user in self.__backup if search_item in user[1]]
            self.__all_users = self.search_algorithm(search_item, self.__backup)
            self.allUsers()

    def search_algorithm(self, query, valuePot):
        result = []
        for user in valuePot:
            if query in user[1]:
                result.append(user)
        return result

    def allUsers(self):
        self.totalUsers = len(self.__all_users)
        self.allUsersFrame = Frame(self.frame)
        self.allUsersFrame.config(borderwidth=1, width=650, bg=self.__backgorud_color)
        self.allUsersFrame.place(height=450*(self.totalUsers / 5), x=0, y=120)
        index = 0
        for user in self.__all_users:
            name = Button(
                self.allUsersFrame,
                font=(self.__font_family, 12),
                width=15,
                relief="flat",
                bg=self.__backgorud_color,
                text=user[2] + " " + user[3] + "\n\t" + user[1]
            )
            self.relation = self.checkFriend(user[0])
            addFriend = Button(
                self.allUsersFrame,
                relief="flat",
                bg=self.__backgorud_color,
                command = lambda userId=user[0], relation=self.relation : self.process(userId, relation),
                text=self.relation,
                state=DISABLED if ("Sent" in self.relation) else NORMAL
            )
            if index == 0:
                name.place(x=0, y=0)
                addFriend.place(x=100, y =60)
            elif index == 1:
                name.place(x=250, y=0)
                addFriend.place(x=350, y = 60)
            elif (index % 2 == 0):
                xIndex = 250
                yIndex = 60*index
                name.place(x=xIndex, y=yIndex)
                addFriend.place(x = xIndex+100, y = yIndex+60)
            else:
                xIndex = 0
                yIndex = 60*(index - 1)
                name.place(x=xIndex, y=yIndex)
                addFriend.place(x=xIndex+100, y = yIndex+60)
            index += 1

    def process(self, requestTo, relation):
        self.allUsersFrame.destroy()
        if "Sent" in relation:
            pass
        elif "Accept" in relation:
            valid = Send()
            msg = {
                "route": "accept_request",
                "add": requestTo,
                "userId": self.master.user[0]
            }
            msg = json.loads(valid.message(msg))
        elif "Add" in relation:
            valid = Send()
            msg = {
                "route": "send_request",
                "add": requestTo,
                "userId": self.master.user[0]
            }
            msg = json.loads(valid.message(msg))
        else:
            pass
        self.frame.destroy()
        self.create()

    def getFriends(self):
        valid = Send()
        msg = {
            "route": "get_friends",
            "userId": self.master.user[0]
        }
        self.friends = json.loads(valid.message(msg))

    def checkFriend(self, friendId):
        for people in self.friends:
            destination_user = people[1]
            origin_user = people[0]
            request = people[2]

            if friendId == destination_user and self.master.user[0] == origin_user:
                return fa.icons["check-circle"] + "  Sent"
            elif friendId == origin_user and self.master.user[0] == destination_user:
                if request:
                    return fa.icons["check-circle"] + "  Friends"
                else:
                    return fa.icons["check-circle"] + "  Accept"
        else:
            return fa.icons["plus-square"] + "  Add"

    def fetchUsers(self):
        valid = Send()
        get_post = {
            "route": "get_users",
            "userId": self.master.user[0]
        }
        return json.loads(valid.message(get_post))
