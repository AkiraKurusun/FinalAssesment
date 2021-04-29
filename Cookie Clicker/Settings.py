# Pygame Template -- Skeleton for a new pygame project -- Settings Folder

# Imports:
import pygame as pg
import os
import random
######################################

# Directories:
Game_folder = os.path.dirname(__file__)

Image_folder = os.path.join(Game_folder, "Images")
Upgrades_folder = os.path.join(Image_folder, "Upgrades")
Background_Main_folder = os.path.join(Image_folder, "Background and Main Cookie")

Sounds_folder = os.path.join(Game_folder, "Sounds")
######################################

# Images
Mouse_Image = os.path.join(Upgrades_folder, "Mouse.png")

######################################

# Title:
TITLE = "COOKIE CLICKER"

# Dimensions:
HEIGHT = 700
WIDTH = 900
FPS = 60

# Colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)