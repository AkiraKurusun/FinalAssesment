# Pygame Template -- Skeleton for a new pygame project -- Settings Folder

# Imports:
import pygame as pg
import os
import random
######################################

# Directories:
Game_folder = os.path.dirname(__file__)
Image_folder = os.path.join(Game_folder, "Images")
Sounds_folder = os.path.join(Game_folder, "Sounds")
######################################

# Title:
TITLE = "TEMPLATE"

# Dimensions:
HEIGHT = 700
WIDTH = 500
FPS = 60

# Colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)