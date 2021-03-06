from Config.config import Global_all
from tkinter import Frame, Entry, FLAT, StringVar, END, Button, Text, INSERT, Label
from tkinter import messagebox
from validation.core_validation import CoreValidation
from validation.send_to_server import Send
import fontawesome as fa


class AddPost:
    def __init__(self, canvas, master):
        self.canvas = canvas
        self.master = master
        self.__primary_color="blue"
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__backgorud_color = returned[3]
        self.__draw_components()

    def __draw_components(self):
        self.__cleared = 0
        self.frame = Frame(
            self.canvas,
            bg=self.__backgorud_color,
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
            bg=self.__backgorud_color,
            relief='flat'
        )
        self.backButton.place(x=10,y=5)

        self.addpostTitle = Label(
            self.frame,
            font=(self.__font_family, 12, "bold"),
            width=45,
            bg=self.__backgorud_color,
            text="New Post"
        )
        self.addpostTitle.place(height=60, x=10, y=-5)

        self.__postTitle = Text(
            self.frame,
            relief=FLAT,
            font=(self.__font_family, 12),
            width=45,
            selectforeground="green",
            highlightcolor=self.__primary_color,
            bd=0,
            pady=5,
            padx=5
        )
        self.__postTitle.insert(INSERT, 'Enter the title')
        self.__postTitle.bind("<Button-1>", self.__callback_for_change)
        self.__postTitle.place(height=60, x=10, y=50)

        self.__postDescripton = Text(
            self.frame,
            relief=FLAT,
            font=(self.__font_family, 12),
            width=45,
            selectforeground="green",
            highlightcolor=self.__primary_color,
            bd=0,
            pady=5,
            padx=5
        )
        self.__postDescripton.insert(INSERT, 'Enter the Description for the post\nOver Here.')
        self.__postDescripton.bind("<Button-1>", self.__callback_for_changeDes)
        self.__postDescripton.place(height=400, x=10, y=130)

        self.postError = Label(
            self.frame,
            font=(self.__font_family, 8, "bold"),
            width=45,
            fg="red",
            bg=self.__backgorud_color
        )
        self.postError.place(height=50,x=130, y=550)

        self.__submitButton = Button(
            self.frame,
            bg=self.__backgorud_color,
            text="Submit",
            font=(self.__font_family, 12),
            activeforeground=self.__primary_color,
            width=10,
            bd=0,
            command=self.__postThis,
            underline=0
        )
        self.__submitButton.place(height=50, x=350, y=550)

    def __callback_for_change(self, *args):
        if self.__postTitle.get("1.0","end-1c") == "Enter the title":
            self.__postTitle.delete("1.0", END)

    def __callback_for_changeDes(self, *args):
        if self.__postDescripton.get("1.0","end-1c") == "Enter the Description for the post\nOver Here.":
            self.__postDescripton.delete("1.0", END)

    def backToHome(self):
        self.backButton.destroy()
        self.frame.destroy()
        from resources.views.AllPosts import AllPosts
        AllPosts(self.canvas, self.master)

    def __postThis(self):
        valid = CoreValidation()
        if valid.isBlank(self.__postTitle.get("1.0", "end-1c"), "Enter the title"):
            self.__titleError = 1
        else:
            self.__titleError = 0

        if valid.isBlank(self.__postDescripton.get("1.0", "end-1c"), "Enter the Description for the post\nOver Here."):
            self.__descError = 1
        else:
            self.__descError = 0

        notValid = True if(self.__descError or self.__titleError) else False

        if notValid:
            self.postError.config(text="Fill all the Text Boxes")
        else:
            self.postError.config(text="")
            self.__title = self.__postTitle.get("1.0","end-1c")
            self.__description = self.__postDescripton.get("1.0","end-1c")
            valid = Send()
            commitPost = {
                "route": "add_post",
                "postTitle": self.__title,
                "postDescription": self.__description,
                "userId": self.master.user[0]
            }
            response = valid.message(commitPost)
            messagebox.showinfo(
                title="Success",
                message="Your Update has been successfully posted."
            )
