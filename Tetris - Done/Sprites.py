# Pygame Template -- Skeleton for a new pygame project -- Sprite Folder

# Imports:
import pygame as pg
import os
import random

# Import Files:
from Settings import *
from Functions import *

class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3