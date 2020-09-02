from Config.config import Global_all
from tkinter import Frame, Label, Scrollbar, Canvas, Button, Entry, StringVar
from tkinter import Text, INSERT, END
import fontawesome as fa
from validation.send_to_server import Send
import json


class Message:
    def __init__(self, canvas, master):
        self.canvas = canvas
        self.master = master
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__backgorud_color = returned[3]
        self.__primary_color = "blue"
        self.__all_users = self.fetchUsers()
        self.create()

    def create(self):
        self.frame = Frame(
            self.canvas,
            bg=self.__backgorud_color,
            height=600
        )
        self.canvas.create_window(
            (160,50),
            window=self.frame,
            anchor='nw',
            width="550"
        )
        self.frameTitle = Label(
            self.frame,
            font=(self.__font_family, 12, "bold"),
            width=45,
            bg=self.__backgorud_color,
            text="Message And make world Smaller"
        )
        self.frameTitle.place(height=60, x=10, y=-20)
        self.lastMessagesNav()
        self.newMessages()

    def newMessages(self):
        self.newMessage = Frame(
            self.frame,
            height = 380,
            width = 380,
            bg=self.__backgorud_color
        )
        self.activeFrame = "self.newMessage"
        self.newMessage.place(x = 130, y=100)
        toLabel = Label(
            self.newMessage,
            text="To :",
            bg=self.__backgorud_color,
            width=5,
            font=(self.__font_family, 12)
        )
        toLabel.place(x=0, y=20)
        self.toWhom = StringVar()
        self.toEntry = Entry(
            self.newMessage,
            relief="flat",
            textvariable=self.toWhom,
            bg=self.__backgorud_color,
            font=(self.__font_family, self.__font_size),
            width=30,
            highlightcolor=self.__primary_color,
            selectforeground="green",
            bd=0
        )
        self.toEntry.insert(0, "Enter Username")
        self.toEntry.bind("<Key>", self.search_the_query)
        self.toEntry.bind("<Button-1>", self.__callback_for_change)
        self.toEntry.place(height=50, x=70, y=0)

        self.messageText = Text(
            self.newMessage,
            relief="flat",
            font=(self.__font_family, 12),
            width=36,
            selectforeground="green",
            highlightcolor=self.__primary_color,
            bd=0,
            pady=5,
            padx=5
        )
        self.messageText.insert(INSERT, "Enter Message")
        self.messageText.bind("<Button-1>", self.__callback_for_changeMessage)
        self.messageText.place(height=200, x=0, y=100)

        self.sendButton = Button(
            self.newMessage,
            text="Send",
            font=(self.__font_family, 12),
            relief="flat",
            bg=self.__backgorud_color,
            command=self.sendMessage
        )
        self.sendButton.place(x=300, y=320)

    def on_configure(self, event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        self.lastMessages.configure(scrollregion=self.canvas.bbox('all'))

    def lastMessagesNav(self):
        self.lastMessages = Frame(
            self.frame,
            width=120,
            bg=self.__backgorud_color,
            height=400
        )
        self.lastMessages.place(x = 0, y =100)

        newMessage = Button(
            self.lastMessages,
            text= fa.icons["plus-square"] + "  New",
            font=(self.__font_family, 12),
            bg=self.__backgorud_color,
            command=self.openNewMessage,
            relief="flat"
        )
        newMessage.place(x = 0, y = 0)
    def __callback_for_change(self, *args):
        if self.toEntry.get() == "Enter Username":
            self.toEntry.delete(0, END)

    def __callback_for_changeMessage(self, *args):
        if self.messageText.get("1.0","end-1c") == "Enter Message":
            self.search_the_query()
            self.messageText.delete("1.0", END)

    def openNewMessage(self):
        eval(self.activeFrame).destroy()
        self.newMessages()

    def sendMessage(self):
        if self.toUserId:
            valid = Send()
            msg = {
                "route": "send_message",
                "messageContent": self.messageText.get("1.0","end-1c"),
                "toUser": self.toWhom.get(),
                "fromUser": self.master.user[0]
            }
            self.response = json.loads(valid.message(msg))
            print(self.response)
        else:
            print('user with that username not found')

    def search_the_query(self, *args):
        '''search_the_query(self, *args):
            self: method first argument
            *args: all the key events generated while typing the name of the user

            This method lists all the users of the specific name typed on the
            search bar of the view.

            This method uses the list comprehension method to list down all the
            users of the name.
        '''
        search_item = self.toWhom.get()
        if search_item != "":
            self.toUserId = [user for user in self.__all_users if search_item == user[1]]
            if self.toUserId:
                self.toUserId = self.toUserId[0][0]

    def fetchUsers(self):
        valid = Send()
        get_post = {
            "route": "get_users",
            "userId": self.master.user[0]
        }
        return json.loads(valid.message(get_post))
