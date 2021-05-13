# Cookie Clicker -- Launch File AKA main.py
######################################

# Imports:
import pygame as pg
import os
import random

# Import Local Files:
from Settings import *
from Sprites import *
######################################

class Game(object):

    def __init__(self):
        self.running = True
        self.playing = True
        self.mouse_amount = 0
        self.grandma_amount = 0
        self.temple_amount = 0
        self.world_amount = 0
        ######################################
        # Initialize Pygame and Create Window
        pg.init()
        pg.mixer.init()  # For Sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    ######################################
    def new(self):
        """Start a New Game"""
        # Create Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.Cookie_Group = pg.sprite.Group()
        self.Mouse_Group = pg.sprite.Group()
        self.Grandma_Group = pg.sprite.Group()
        self.Temple_Group = pg.sprite.Group()
        self.Cookie_World_Group = pg.sprite.Group()
        ######################################
        # Create Game Objects
        self.main_cookie = Cookie()
        self.Cookie_Group.add(self.main_cookie)
        ######################################
        # Add Game Objects to Groups
        for i in self.Cookie_Group:
            self.all_sprites.add(i)
        ######################################
        # Run it
        self.run()

    ######################################
    def run(self):
        """Main Game Loop"""
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    ######################################
    def events(self):
        """Game Loop - Events"""
        for event in pg.event.get():
            # Check for Closing the Window
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if self.main_cookie.rect.collidepoint(event.pos):
                    self.main_cookie.clicked()

                if self.buy_mouse_rect.collidepoint(event.pos):
                    Cookie.buy_mouse(self.main_cookie, self)

                if self.buy_grandma_rect.collidepoint(event.pos):
                    Cookie.buy_grandma(self.main_cookie, self)

                if self.buy_temple_rect.collidepoint(event.pos):
                    Cookie.buy_temple(self.main_cookie, self)

                if self.buy_world_rect.collidepoint(event.pos):
                    Cookie.buy_world(self.main_cookie, self)

    ######################################
    def update(self):
        """ Game Loop - Update"""
        self.all_sprites.update()

    ######################################
    def draw(self):
        """ Game Loop - Draw"""
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        ######################################
        # Draws Score
        font = pg.font.Font(font_name, 30)
        text_surface = font.render("Score: " + str(self.main_cookie.times_clicked), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2 - 120, HEIGHT - 100)
        self.screen.blit(text_surface, text_rect)
        # Mouses
        ######################################
        text_surface = font.render("Mouses: " + str(self.mouse_amount), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2 + 120, HEIGHT - 180)
        self.screen.blit(text_surface, text_rect)
        # Buy Mouse
        ######################################
        self.buy_mouse = font.render("Buy Mouse: " + str(self.main_cookie.mouse_price), True, WHITE)
        self.buy_mouse_rect = text_surface.get_rect()
        self.buy_mouse_rect.midtop = (WIDTH / 2 + 110, 10)
        self.screen.blit(self.buy_mouse, self.buy_mouse_rect)
        # Grandma
        ######################################
        text_surface = font.render("Grandmas: " + str(self.grandma_amount), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2 + 120, HEIGHT - 140)
        self.screen.blit(text_surface, text_rect)
        # Buy Grandma
        ######################################
        self.buy_grandma = font.render("Buy Grandma: " + str(self.main_cookie.grandma_price), True, WHITE)
        self.buy_grandma_rect = text_surface.get_rect()
        self.buy_grandma_rect.midtop = (WIDTH / 2 + 110, 60)
        self.screen.blit(self.buy_grandma, self.buy_grandma_rect)
        # Temples
        ######################################
        text_surface = font.render("Temples: " + str(self.temple_amount), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2 + 120, HEIGHT - 100)
        self.screen.blit(text_surface, text_rect)
        # Buy Temple
        ######################################
        self.buy_temple = font.render("Buy Temple: " + str(self.main_cookie.temple_price), True, WHITE)
        self.buy_temple_rect = text_surface.get_rect()
        self.buy_temple_rect.midtop = (WIDTH / 2 + 110, 110)
        self.screen.blit(self.buy_temple, self.buy_temple_rect)
        # Worlds
        ######################################
        text_surface = font.render("Worlds: " + str(self.world_amount), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2 + 120, HEIGHT - 60)
        self.screen.blit(text_surface, text_rect)
        # Buy
        self.buy_world = font.render("Buy World: " + str(self.main_cookie.world_price), True, WHITE)
        self.buy_world_rect = text_surface.get_rect()
        self.buy_world_rect.midtop = (WIDTH / 2 + 110, 160)
        self.screen.blit(self.buy_world, self.buy_world_rect)
        ######################################
        # After Drawing Everything Flip the Display
        pg.display.flip()

######################################
g = Game()
while g.running:
    g.new()

pg.quit()