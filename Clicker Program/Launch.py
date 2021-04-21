# Ethan Frailey
# Clicker program for cookie clicker
####################################################

# Imports
import time
import tkinter as tk
from tkinter.ttk import *
import pyautogui
####################################################

# Variables
# Wait = None / 100
Height = 200
Width = 400
Click_pos = None
####################################################

# Functions
def click(event):
    if clicking:
        time.sleep(Wait)
        pyautogui.click(Click_pos)

def close(event):
    window.quit() # if you want to exit the entire thing

def change_click_pos(event):
    pass
####################################################

# Init
window = tk.Tk()
window.geometry("{}x{}".format(Width, Height))
Photo = tk.PhotoImage(file = "Clicker_Image.png")
window.iconphoto(False, Photo)
window.resizable(0, 0)
window.title("Clicker Program")
####################################################

# Master Bindings
window.bind('<Escape>', close)
####################################################

# Labels, Buttons, etc

####################################################
window.mainloop()