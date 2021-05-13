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
        self.image = pg.image.load(str(os.path.join(Background_Main_folder, "MainCookie.png"))).convert()
        self.image = pg.transform.scale(self.image, (200, 200))
        self.image.set_colorkey("BLACK")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 - 120, HEIGHT / 2 - 60)
        self.times_clicked = 0
        self.multiplyer = 1

        self.mouse_price = 10
        self.grandma_price = 20
        self.temple_price = 50
        self.world_price = 100

    def clicked(self):
        self.times_clicked = round(self.times_clicked, 2)
        add = 1 * self.multiplyer
        self.times_clicked += add
        self.times_clicked = round(self.times_clicked, 2)

    def buy_mouse(self, Game):
        varible = self.check_vaild(self.mouse_price, self.times_clicked)
        if varible:
            self.times_clicked -= self.mouse_price
            self.multiplyer += .1
            Game.mouse_amount += 1
            self.times_clicked = round(self.times_clicked, 2)
            self.mouse_price += 2

    def buy_grandma(self, Game):
        varible = self.check_vaild(self.grandma_price, self.times_clicked)
        if varible:
            self.times_clicked -= self.grandma_price
            self.multiplyer += .3
            Game.grandma_amount += 1
            self.times_clicked = round(self.times_clicked, 2)
            self.grandma_price += 5

    def buy_temple(self, Game):
        varible = self.check_vaild(self.temple_price, self.times_clicked)
        if varible:
            self.times_clicked -= self.temple_price
            self.multiplyer += .3
            Game.temple_amount += 1
            self.times_clicked = round(self.times_clicked, 2)
            self.temple_price += 10

    def buy_world(self, Game):
        varible = self.check_vaild(self.world_price, self.times_clicked)
        if varible:
            self.times_clicked -= self.world_price
            self.multiplyer += 1
            Game.world_amount += 1
            self.times_clicked = round(self.times_clicked, 2)
            self.world_price += 20

    def check_vaild(self, purchaseP, total):
        if (total - purchaseP) >= 0:
            return True
        else:
            return False

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
