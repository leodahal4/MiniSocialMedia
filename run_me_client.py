from Config.config import Global_all
from routes.index import Routes
from tkinter import Tk, Frame, Menu, messagebox
import os, os.path
import shutil
import subprocess

my_root_app = ""

class mainClass(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.width = 5
        master.borderwidth = 5
        self.get_config()
        master.title("MSM - Mini Social Media")
        master.geometry("700x700+550+180")
        master.config(bg=self.__background_color)
        Routes(master=master, source="initial", destination="login")

    def quit_all(self):
        self.destroy()
        self.master.destroy()

    def get_config(self):
        returned = Global_all.global_config_for_font()
        self.__font_family = returned[0]
        self.__font_size = returned[1]
        self.__weight = returned[2]
        self.__background_color = returned[3]


def main():
    """main
        Create a tk window for making the things true.
    """
    if os.path.isdir('temp'):
        pass
    else:
        make_temp_Folder()

    global my_root_app
    my_root_app = Tk()
    my_root_app.resizable(False, False)
    my_app = mainClass(master=my_root_app)
    my_root_app.protocol("WM_DELETE_WINDOW", on_closing)
    my_app.mainloop()

def make_temp_Folder():
    temp_path = os.path.join('temp', 'assets')
    os.mkdir('temp')
    os.mkdir(temp_path)


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        clear_all_temp()
        my_root_app.destroy()

def clear_all_temp():
    folder_path = "temp"
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
        except OSError as e:
            print("Error: %s : %s" % (folder_path, e.strerror))


if __name__ == "__main__":
    # If this file is executed as a script then,
    # only call the main function nor do nothing.
    main()
