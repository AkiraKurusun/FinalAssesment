# Pygame Template -- Skeleton for a new pygame project -- Sprite Folder

# Imports:
import pygame as pg
import os
import random

# Import Files:
from Settings import *

class Cookie(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.times_clicked = 0
