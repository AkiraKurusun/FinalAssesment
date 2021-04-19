# PLATFORMER (Launch File AKA main.py)
# Created by Ethan Frailey
# CopyRight 2021
# Any person who reuses or distributes this program without written permission is subject to Copyright
######################################

# Imports:
import pygame as pg
import os
import random
from Settings import *
from random import choice
vec = pg.math.Vector2

######################################

# Sprite Classes
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = PLAYER_LAYER
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 100 )
        self.pos = vec(40, HEIGHT - 100)
        # Speed X and Y
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    ######################
    def load_images(self):
        # This groups the images for organization of animations
        self.standing_frames = [self.game.spritesheet.get_image(614, 1063, 120, 191),
                                self.game.spritesheet.get_image(690, 406, 120, 201)]
        for frame in self.standing_frames:
            frame.set_colorkey(BLACK)

        self.walk_frames_r = [self.game.spritesheet.get_image(678, 860, 120, 201),
                            self.game.spritesheet.get_image(692, 1458, 120, 207)]
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)

        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))

        self.jump_frame = self.game.spritesheet.get_image(382, 763, 150, 181)
        self.jump_frame.set_colorkey(BLACK)

    # Update Function for PLayer Class
    def update(self):
        self.animate()
        # Resting Speed
        self.acc = vec(0, PLAYER_GRAVITY)

        # Getting which keys are pressed down
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # Applying Friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        if abs(self.vel.x) < 0.1:
            self.vel.x =0

        # Equations of Motion
        self.vel += self.acc
        if abs(self.vel.x) < .1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc

        # Wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2

        # Defining position
        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        if self.walking:
            if now - self.last_update > 180:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]

                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        self.mask = pg.mask.from_surface(self.image)

        if not self.jumping and not self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                bottom = self.rect.bottom
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

    ######################
    def jump(self):
        """Allow the player to jump if they are standing on something"""
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self, self.game.Platforms_Group, False)
        self.rect.y -= 2
        if hits and not self.jumping:
            self.game.jump_sound.play()
            self.jumping = True
            self.vel.y = -PLAYER_JUMP

    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

class Cloud(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = CLOUD_LAYER
        self.groups = game.all_sprites, game.Cloud_Group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = choice(self.game.cloud_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        scale = random.randrange(50, 101) / 100
        self.image = pg.transform.scale(self.image, (int(self.rect.width * scale), int(self.rect.height * scale)))
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-500, -50)

    def update(self):
        if self.rect.top == HEIGHT * 2:
            self.kill()



class Platform(pg.sprite.Sprite):
    def __init__(self, game,  x, y):
        self._layer = PLATFROM_LAYER
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = [self.game.spritesheet.get_image(0, 288, 380, 94), self.game.spritesheet.get_image(213, 1662, 201, 100)]
        self.image = choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mob(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = MOB_LAYER
        self.groups = game.all_sprites, game.Mob_Group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_up = self.game.spritesheet.get_image(566, 510, 122, 139)
        self.image_up.set_colorkey(BLACK)
        self.image_down = self.game.spritesheet.get_image(568, 1534, 122, 135)
        self.image_down.set_colorkey(BLACK)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.centerx = choice([-100, WIDTH + 100])
        self.vx = random.randrange(1, 4)
        if self.rect.centerx > WIDTH:
            self.vx *= -1
        self.rect.y = random.randrange(HEIGHT / 2)
        self.vy = 0
        self.dy = 0.5

    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:
            self.dy *= -1
        center = self.rect.center
        if self.dy < 0:
            self.image = self.image_up
        else:
            self.image = self.image_down
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.center = center
        self.rect.y += self.vy
        if self.rect.left > WIDTH + 100 or self.rect.right < -100:
            self.kill()


class Spritesheet:
    """Utility class for loading and parsing spritesheets"""
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height):
        """Grab an image out of a sprite sheet"""
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        return image