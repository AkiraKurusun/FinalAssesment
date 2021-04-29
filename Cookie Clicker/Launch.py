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

        # Initialize Pygame and Create Window
        pg.init()
        pg.mixer.init()  # For Sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def new(self):
        """Start a New Game"""
        # Create Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.Cookie_Group = pg.sprite.Group()
        self.Mouse_Group = pg.sprite.Group()
        self.Grandma_Group = pg.sprite.Group()
        self.Temple_Group = pg.sprite.Group()
        self.Cookie_World_Group = pg.sprite.Group()

        # Create Game Objects
        self.main_cookie = Cookie()
        self.Cookie_Group.add(self.main_cookie)

        # Add Game Objects to Groups
        for i in self.Cookie_Group:
            self.all_sprites.add(i)
        for i in self.Mouse_Group:
            self.all_sprites.add(i)
        for i in self.Grandma_Group:
            self.all_sprites.add(i)
        for i in self.Temple_Group:
            self.all_sprites.add(i)
        for i in self.Cookie_World_Group:
            self.all_sprites.add(i)

        # Run it
        self.run()

    def run(self):
        """Main Game Loop"""
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        """Game Loop - Events"""
        for event in pg.event.get():
            # Check for Closing the Window
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

            if event.type == pg.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                clicked_sprites = [s for s in sprites if s.rect.collidepoint(pos)]

    def update(self):
        """ Game Loop - Update"""
        self.all_sprites.update()

    def draw(self):
        """ Game Loop - Draw"""
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # After Drawing Everything Flip the Display
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_game_over_screen()

pg.quit()