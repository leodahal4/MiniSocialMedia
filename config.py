global font_family, font_size, weight
font_family = ""
font_size = 13
weight = "bold"


class Global_all:
    def global_config_for_font():
        # try:
        #     import pyglet
        #     from pyglet import font
        #     print('here')
        #     font.add_file("my_font.ttf")
        #     print('here')
        #     firacode_font = font.load('Fira Code')
        #     print('here')
        #
        #     font_family = "Fira Code"
        #
        # except:
        #     try:
        #         print('except try')
        #         import subprocess
        #         import platform
        #         if platform.system() == "Linux":
        #             subprocess.call("sudo pip3 install pyglet", shell=True)
        #         else:
        #             subprocess.call("pip install pyglet", shell=True)
        #         import pyglet
        #         pyglet.font.add_file('fonts/my_font.ttf')
        #         source_code_pro = pyglet.font.load('Fira Code')
        #         font_family = "Fira Code"
        #     except:

        font_family = "Courier"
        color = background_color()
        return font_family, font_size, weight, color


def background_color():
    return "white"
