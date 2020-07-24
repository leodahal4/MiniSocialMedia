from tkinter import Tk, Frame, Menu
from config import Global_all
from pages import login_form

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
        self.menuBar()
        login_form.LoginForm(self.master)

    def menuBar(self):
        """menuBar
            This function is responsible for creating the menus bar at the top
            of the window along with ohter submenus with them.
        """
        self.__font_size = 10

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(
            label='File',
            font=(self.__font_family, self.__font_size),
            menu=filemenu
        )
        filemenu.add_command(
            label="Exit",
            font=(self.__font_family, self.__font_size),
            command=self.quit_all
        )
        helpmenu = Menu(menu)
        menu.add_cascade(
            label='Help',
            font=(self.__font_family, self.__font_size),
            menu=helpmenu
        )
        helpmenu.add_command(
            label='About',
            font=(self.__font_family, self.__font_size)
        )
        helpmenu.add_command(
            label="How to use?",
            font=(self.__font_family, self.__font_size)
        )

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
    my_root_app = Tk()
    my_root_app.resizable(False, False)
    my_app = mainClass(master=my_root_app)
    my_app.mainloop()


if __name__ == "__main__":
    # If this file is executed as a script then,
    # only call the main function nor do nothing.
    main()
