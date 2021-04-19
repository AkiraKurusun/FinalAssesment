# PLATFORMER (Launch File AKA main.py)
# Created by Ethan Frailey
# CopyRight 2021
# Credit for images "Kenney.nl" or "www.kenney.nl"
# Happy Tune by http://opengameart.org/users/syncopika
# Yippee by http://opengameart.org/users/snabisch
# Any person who reuses or distributes this program without written permission is subject to Copyright

######################################

# Imports:
import pygame as pg
import os
import random
from os import path

# Import Local Files:
from Sprites import *


######################################

class Game(object):

    def __init__(self):
        self.running = True

        # Initialize Pygame and Create Window
        pg.init()
        pg.mixer.init()  # For Sound
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))  # Set Display Size
        pg.display.set_caption(TITLE)  # Set The Title
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)  # Font Name import
        self.load_data()

    ######################
    def load_data(self):
        """Load High Score"""
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, "Images")
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:  # Tries to read the file
                self.highscore = int(f.read())  # Reads the file
            except:  # Condition if there is nothing in the file
                self.highscore = 0

        # Loads sprite sheet image
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITE_FILE))

        # CLoud Images
        self.cloud_images = []
        for i in range(1, 4):
            self.cloud_images.append(pg.image.load(path.join(CLOUD_PATH, 'cloud{}.png'.format(i))).convert())

        # Load sound files
        self.snd_dir = path.join(self.dir, "Sounds")
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, "Jump33.wav"))

    def new(self):
        """Start a New Game"""
        # Create Sprite Groups
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.Player_Group = pg.sprite.Group()
        self.Platforms_Group = pg.sprite.Group()
        self.Mob_Group = pg.sprite.Group()
        self.Cloud_Group = pg.sprite.Group()
        # Create Game Objects
        self.player = Player(self)
        self.Player_Group.add(self.player)

        # Creation of Platforms
        for plat in PLATFORMS_LIST:
            p = Platform(self, *plat)
            self.Platforms_Group.add(p)

        self.mob_timer = 0

        # Score
        self.score = 0

        # Add Game Objects to Groups
        for i in self.Player_Group:
            self.all_sprites.add(i)
        for i in self.Platforms_Group:
            self.all_sprites.add(i)
        for i in self.Mob_Group:
            self.all_sprites.add(i)
        for i in self.Cloud_Group:
            self.all_sprites.add(i)

        for i in range(8):
            c = Cloud(self)
            c.rect.y += 500

        pg.mixer.music.load(path.join(self.snd_dir, "Happy Tune.ogg"))

        # Run
        self.run()

    ######################
    def run(self):
        """Main Game Loop"""
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)

    ######################
    def events(self):
        """Game Loop - Events"""
        for event in pg.event.get():
            # Check for Closing the Window
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    ######################
    def update(self):
        """ Game Loop - Update"""
        self.all_sprites.update()

        # Spawn a Mob
        now = pg.time.get_ticks()
        if now - self.mob_timer > 3000 + random.choice([-1000, -500, 0, 500, 1000]):
            self.mob_timer = now
            Mob(self)

        mob_hits = pg.sprite.spritecollide(self.player, self.Mob_Group, False, pg.sprite.collide_mask)
        if mob_hits:
            self.playing = False


        # Checks if player has hit a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.Platforms_Group, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.centery:
                        lowest = hit
                if self.player.pos.y < hits[0].rect.bottom:
                    self.player.pos.y = lowest.rect.top
                    self.player.vel.y = 0
                    self.player.jumping = False

        # if player reached top 1/4 of the screen
        if self.player.rect.top <= HEIGHT / 4:
            if random.randrange(100) < 13:
                Cloud(self)
            self.player.pos.y += max(abs(self.player.vel.y), 2)
            for cloud in self.Cloud_Group:
                cloud.rect.y += max(abs(self.player.vel.y / 2), 2)
            for mob in self.Mob_Group:
                mob.rect.y += max(abs(self.player.vel.y), 2)
            for plat in self.Platforms_Group:
                plat.rect.y += max(abs(self.player.vel.y), 2)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
                    self.score += 10

        # Game Over screen
        if self.player.rect.top > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.Platforms_Group) == 0:
            self.playing = False

        # Spawn New Platforms
        while len(self.Platforms_Group) < 6:
            width = random.randrange(50, 100)
            p = Platform(self, random.randrange(0, WIDTH - width), random.randrange(-75, -30))
            self.Platforms_Group.add(p)
            self.all_sprites.add(p)

    ######################
    def draw(self):
        """ Game Loop - Draw"""
        self.screen.fill(BACK_GROUND)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)

        # After Drawing Everything Flip the Display
        pg.display.flip()

    ######################
    def show_start_screen(self):
        """Show Game Start Screen"""
        pg.mixer.music.load(path.join(self.snd_dir, "Yippee.ogg"))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BACK_GROUND)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("WSAD to move, Space to jump", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_press()
        pg.mixer.fadeout(500)

    ######################
    def show_game_over_screen(self):
        """Show Game Over/Continue Screen"""
        if not self.running:
            return
        pg.mixer.music.load(path.join(self.snd_dir, "Yippee.ogg"))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BACK_GROUND)
        self.draw_text("Game Over", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:  # If new High Score
            self.highscore = self.score
            self.draw_text("New HighScore: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            print(self.score)

            # Opens the file to rewrite high score
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))

        else:  # If High score wasn't beat. Displays the current high score
            self.draw_text("HighScore: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)

        pg.display.flip()
        self.wait_for_press()
        pg.mixer.fadeout(500)

    def wait_for_press(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        """Draws text on the screen"""
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


######################################

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_game_over_screen()

pg.quit()
