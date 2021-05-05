# Ethan Frailey
# Auto Clicker Program
# 5/21
##########################################
# Imports
from tkinter import *
import os

##########################################
# Attributes
HEIGHT = 210
WIDTH = 300
FULLSCREEN = False

##########################################
class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.master = master
        self.value = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(text="Auto Clicker Program")
        self.title.pack()

        self.borderline = Label(text="-------------------------------------")
        self.borderline.pack()

        self.instructions = Label(text="- When Running Press M to Start Clicking. "
                                       "\n- Press M Again to Stop. "
                                       "\n- Press B to exit and change your Clicking Speed.")
        self.instructions.pack()

        self.slider = Scale(self, from_=100, to=1000, length=600, tickinterval=100, orient=HORIZONTAL)
        self.slider.pack()

        self.borderline1 = Label(text="-------------------------------------")

        self.start = Button(text="Start", command=self.start, width=200)
        self.start.pack(side="left", padx=5, pady=5, fill="x")

    def start(self):
        self.value = self.slider.get()
        self.master.attributes('-disabled', True)
        os.system("Launch.pyw " + str(self.value))
        self.master.attributes('-disabled', False)

##########################################
def launch():
    root = Tk()
    root.title("AutoClicker")
    photo = PhotoImage(file = "Clicker_Image.png")
    root.iconphoto(False, photo)
    root.geometry(str(str(WIDTH) + "x" + str(HEIGHT)))
    root.resizable(False, False)
    root.attributes("-fullscreen", FULLSCREEN)
    app = App(root)
    root.mainloop()

launch()
