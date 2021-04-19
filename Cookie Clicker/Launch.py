# Pygame Template -- Skeleton for a new pygame project -- Launch File AKA main.py
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
        self.Player_Group = pg.sprite.Group()
        self.Enemy_Group = pg.sprite.Group()

        # Create Game Objects
        self.player = Player()

        # Add Game Objects to Groups
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        """Main Game Loop"""
        self.playing = True
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
                self.runnning = False

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