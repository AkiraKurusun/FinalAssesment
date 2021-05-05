# Pygame Template -- Skeleton for a new pygame project -- Launch File AKA main.py
# Music = https://opengameart.org/content/title-theme-8-bit-style
######################################

# Imports:
import pygame as pg
import os
import random

# Import Local Files:
from Settings import *
from Sprites import *
from Functions import *

######################################

# Game Class
class Game(object):

    def __init__(self):
        self.run = True
        self.playing = True
        # Initialize Pygame and Create Window
        pg.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.grid = None
        self.fall_speed = 0.25
        self.fall_time = 0

    def new(self):
        pg.mixer.music.load(os.path.join(Sounds_folder, "MenuTheme.ogg"))
        pg.mixer.music.set_volume(0.5)
        self.show_start_screen()

    def main(self):
        pg.mixer.music.play(loops=-1)
        locked_positions = {}  # (x,y):(255,0,0)
        self.grid = create_grid(locked_positions)

        change_piece = False
        current_piece = get_shape()
        next_piece = get_shape()

        self.playing = True # Makes the Game Replayable

        while self.playing:
            now = pg.time.get_ticks()

            self.grid = create_grid(locked_positions)
            self.fall_time += self.clock.get_rawtime()
            self.clock.tick()

            # PIECE FALLING CODE
            if self.fall_time / 1000 >= self.fall_speed:
                self.fall_time = 0
                current_piece.y += 1
                if not (valid_space(current_piece, self.grid)) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    pg.display.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        current_piece.x -= 1
                        if not valid_space(current_piece, self.grid):
                            current_piece.x += 1

                    elif event.key == pg.K_RIGHT:
                        current_piece.x += 1
                        if not valid_space(current_piece, self.grid):
                            current_piece.x -= 1
                    elif event.key == pg.K_UP:
                        # rotate shape
                        current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                        if not valid_space(current_piece, self.grid):
                            current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                    if event.key == pg.K_DOWN:
                        # move shape down
                        current_piece.y += 1
                        if not valid_space(current_piece, self.grid):
                            current_piece.y -= 1

                    if event.key == pg.K_SPACE:
                        while valid_space(current_piece, self.grid):
                            current_piece.y += 1
                        current_piece.y -= 1


            shape_pos = convert_shape_format(current_piece)

            # add piece to the grid for drawing
            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    self.grid[y][x] = current_piece.color

            # IF PIECE HIT GROUND
            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color
                current_piece = next_piece
                next_piece = get_shape()
                change_piece = False

                # call four times to check for multiple clear rows
                clear_rows(self.grid, locked_positions)

            draw_window(g.screen, self.grid)
            draw_next_shape(next_piece, g.screen)
            pg.display.update()

            # Check if user lost
            if check_lost(locked_positions):
                self.playing = False

        pg.mixer.music.fadeout(500)
        self.show_game_over_screen()



    def create_grid(self, locked_positions={}):
        self.grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (j, i) in locked_positions:
                    c = locked_positions[(j, i)]
                    self.grid[i][j] = c
        return self.grid

    def show_start_screen(self):
        g.screen.fill((0, 0, 0))
        draw_text_middle('Press any key to begin.', 60, (255, 255, 255), g.screen)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

            if event.type == pg.KEYDOWN:
                self.main()

    def show_game_over_screen(self):
        g.screen.fill((0, 0, 0))
        draw_text_middle("You Lost", 60, (255, 255, 255), g.screen)
        pg.display.update()
        pg.time.delay(3000)


g = Game()
while g.run:
    g.new()

pg.quit()