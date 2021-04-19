# PLATFORMER (Launch File AKA main.py)
# Created by Ethan Frailey
# CopyRight 2021
# Any person who reuses or distributes this program without written permission is subject to Copyright

######################################

# Imports:
import pygame as pg
import os
from os import path
import random
######################################

# Directories:
Game_folder = os.path.dirname(__file__)
Image_folder = os.path.join(Game_folder, "Images")
Sounds_folder = os.path.join(Game_folder, "Sounds")
CLOUD_PATH = os.path.join(Image_folder, "clouds")
MOB_FREQ = 5000
######################################

# Title:
TITLE = "Jumpy!"

# Font Options:
FONT_NAME = 'arial'

# Dimensions:
HEIGHT = 600
WIDTH = 480
FPS = 60

# Player Properties
PLAYER_ACC = 0.6
PLAYER_FRICTION = -0.09
PLAYER_GRAVITY = 0.8
PLAYER_JUMP = 20

MOB_LAYER = 2
PLAYER_LAYER = 2
PLATFROM_LAYER = 1
CLOUD_LAYER = 0

# Name of files
HS_FILE = "highscore.txt"
SPRITE_FILE = "spritesheet_jumper.png"

# Platforms list
PLATFORMS_LIST = [(0, HEIGHT - 60),
                  (WIDTH / 2 - 50,  HEIGHT * 3/4 - 50),
                  (125, HEIGHT - 350),
                  (350, 200),
                  (175, 100)]

# Colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BACK_GROUND = (112, 88, 163)