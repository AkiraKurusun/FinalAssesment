# Ethan Frailey
# Clicker Program
# CopyRight 2021

###########################################################
# Credit
# Mouse_Image = https://www.clipartmax.com/middle/m2H7K9m2d3b1N4A0_mouse-pointer-01-clip-art-computer-mouse-on-screen/
###########################################################
# Imports
from tkinter import *
from PIL import Image, ImageTk
from os import path

###########################################################
# Attributes
HEIGHT = 150  #INT
WIDTH =  400 #INT
FULLSCREEN = False #BOOLEAN
Title = "Clicker Program"

###########################################################
# Classes
class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

    def create_widgets(self):
        # Creates The Widgets in the Program
        # Title
        self.title = Label(self, text="Clicker")
        self.title.config(font=("Arial Bold", 40))
        self.title.pack(anchor=CENTER)

        # Slider
        self.scale = Scale(self, from_=0, to=100, length=300, tickinterval=10, orient=HORIZONTAL)
        self.scale.pack(anchor=CENTER)
###########################################################

def launch():
    root = Tk()
    mouse_image = PhotoImage(file='Mouse_Image.png') # Loading in the image in the corner
    root.iconphoto(False, mouse_image) # Using the image
    root.resizable(False, False) # Setting the condition for resizing the window
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.title(Title)
    root.attributes("-fullscreen", FULLSCREEN)
    app = App(root)
    root.mainloop()
###########################################################

launch()