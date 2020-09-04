from Config.config import Global_all
from tkinter import Frame, Label, Scrollbar, Canvas, Button, Entry, StringVar
from tkinter import Text, INSERT, END, BOTH
from validation.send_to_server import Send
import fontawesome as fa
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
        self.toEntryError = Label(
            self.newMessage,
            text="",
            fg="red",
            bg=self.__backgorud_color,
            font=(self.__font_family, 8)
        )
        self.toEntryError.place(x=70, y=60)
        self.sendSuccess = Label(
            self.newMessage,
            text="",
            fg="blue",
            bg=self.__backgorud_color,
            font=(self.__font_family, 8)
        )
        self.sendSuccess.place(x=70, y=60)
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
            command=lambda x="search": self.sendMessage(x)
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
        self.getMessages()
        self.pickUnique()

        self.oldLabel = Label(
            self.lastMessages,
            text="Old Messages",
            font=(self.__font_family, 9),
            underline=0,
            bg=self.__backgorud_color
        )
        self.oldLabel.place(x=0, y=40)
        initialy = 30
        times = 1
        for user in self.__oldmessage:
            messageButton = Button(
                self.lastMessages,
                bg=self.__backgorud_color,
                width=8,
                relief="flat",
                font=(self.__font_family, 12),
                activeforeground="blue",
                fg="red" if not(user[4]) else "black",
                text=self.getUser(user[2] if user[2] != self.master.user[0] else user[3]),
                command=lambda id=user[2] if user[2] != self.master.user[0] else user[3]:self.openMessage(id)
            )
            messageButton.place(x=0, y=initialy + times*30)
            times += 1

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

    def getMessages(self):
        valid = Send()
        get_messages = {
            "route": "get_messages",
            "userId": self.master.user[0]
        }
        self.__allMessages = json.loads(valid.message(get_messages))
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

    def pickUnique(self):
        self.__oldmessage = []
        self.allindex = []
        for user in self.__allMessages:
            self.__oldmessage.append(self.__allMessages[0])
            self.allindex.append([user[2],user[3]])
            break
        for user in self.__allMessages:
            for index in self.allindex:
                if user[2] not in index or user[3] not in index:
                    append = True
                else:
                    append = False
                    break

            if append:
                self.allindex.append([user[2], user[3]])
                self.__oldmessage.append(user)
            else:
                pass

    def openMessage(self, userId):
        eval(self.activeFrame).destroy()
        self.activeFrame = "self.conversationFrame"
        conversation = self.getConversation(userId)
        self.setSeen(userId)
        self.conversationFrame = Frame(
            self.frame,
            height = 380,
            width = 380,
            bd=1
        )
        self.conversationFrame.place(x = 130, y=100)
        placeX = 0
        placeY = 0
        for messages in conversation:
            if messages[2] != self.master.user[0]:
                if len(messages[1]) < 25:
                    display = messages[1]
                else:
                    fill_gaps = 28 - len(messages[1][27:])
                    display = str(messages[1][:27]) + "\n" + str(messages[1][27:]) + fill_gaps*" "
                messageLabel = Label(
                    self.conversationFrame,
                    fg="black",
                    text=display,
                    font=(self.__font_family, 9)
                )
                messageLabel.place(x=placeX, y=placeY)
                placeY += 40 if "\n" in display else 20
            else:
                if len(messages[1]) < 21:
                    display = messages[1]
                else:
                    fill_gaps = 21 - len(messages[1][21:])
                    display = str(messages[1][:21]) + "\n" + str(messages[1][21:]) + fill_gaps*" "
                messageLabel = Label(
                    self.conversationFrame,
                    fg="black",
                    font=(self.__font_family, 9),
                    text=display
                )
                messageLabel.place(x=placeX+220, y=placeY)
                placeY += 40 if "\n" in display else 20
        self.message = StringVar()
        messageEntry = Entry(
            self.conversationFrame,
            textvariable=self.message,
            width=42,
            relief="flat",
            highlightcolor="blue",
            font=(self.__font_family, 9)
        )
        messageEntry.place(height=50, x=0, y=325)
        sendButton = Button(
            self.conversationFrame,
            text="Send",
            font=(self.__font_family, 10),
            relief="flat",
            width=5,
            activeforeground="blue",
            underline=0,
            command=lambda toUser=userId: self.sendMessage(toUser)
        )
        sendButton.place(height=40, x=305, y=330)

    def getConversation(self, userId):
        valid = Send()
        get_message = {
            "route": "get_message",
            "messegerId": userId,
            "userId": self.master.user[0]
        }
        return json.loads(valid.message(get_message))

    def sendMessage(self, toUser):
        if toUser == "search":
            self.search_the_query()
            if self.toUserId != self.master.user[0]:
                if self.toUserId:
                    valid = Send()
                    msg = {
                        "route": "send_message",
                        "messageContent": self.messageText.get("1.0","end-1c"),
                        "fromUser": self.master.user[0],
                        "toUser": self.toUserId
                    }
                    self.response = json.loads(valid.message(msg))
                    self.newMessage.destroy()
                    self.newMessages()
                    self.sendSuccess.config(text="Send Success")
                else:
                    self.toEntry.config(highlightcolor="red")
                    self.toEntryError.config(text="Username not found")
            else:
                self.toEntry.config(highlightcolor="red")
                self.toEntryError.config(text="Send message to self?\nMay be next Update")
        else:
            valid = Send()
            msg = {
                "route": "send_message",
                "messageContent": self.message.get(),
                "fromUser": self.master.user[0],
                "toUser": toUser
            }
            self.response = json.loads(valid.message(msg))
            self.openMessage(toUser)

    def setSeen(self, fromUser):
        valid = Send()
        set_seen = {
            "route": "set_seen_message",
            "fromUser": fromUser,
            "toUser": self.master.user[0]
        }
