from tkinter import Frame, StringVar, Label, Tk
from PIL import Image, ImageTk


class Home(Frame):
    '''Home(Frame):
        This is the default window or View that will be executed after the
        user logs in to the system.
    '''
    def __init__(self, master):
        self.master = master
        self.master.title("Home")

        self.__create_all_fields()

    def __create_all_fields(self):
        # navbar
        # app bar
        # initial is posts
        #
        pass

    def forget_all(self):
        pass

    def posts(self):
        pass

    def navbar(self):
        pass

    def app_bar(self):
        pass
