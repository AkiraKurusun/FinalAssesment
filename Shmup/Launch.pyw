# Ethan Frailey
# 3/21
# Shoot Them Up (Smump)

# Attributes
#####################################################
# Code Ethan Frailey
# Artwork: Unknown Artist - Images found at https://opengameart.org/
# Sounds:
#####################################################

import random as R
from os import path
import pygame as pg


# Classes
#####################################################
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.image = pg.Surface((40, 40))
        self.image = Player_sprite
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(Player_sprite, (60, 60))
        self.rect = self.image.get_rect()
        self.radius = (self.rect.width * .65 / 2)
        # pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .1))
        self.sheild = 100
        self.shoot_delay = 250
        self.last_shot = pg.time.get_ticks()
        self.lives = 3
        self.hide_timer = pg.time.get_ticks()
        self.hidden = False
        self.power_level = 1
        self.powtimer = pg.time.get_ticks()

    def shields_up(self, num):
        self.sheild += 30
        if self.sheild > 100:
            self.sheild = 100

    def gun_powu_up(self):
        self.power_level += 1
        self.powtimer = pg.time.get_ticks()

    def update(self):
        self.speedy = 0
        self.speedx = 0

        if self.power_level > 2 and pg.time.get_ticks() - self.powtimer > POWERUP_Timer:
            self.power_level -= 1
            self.powtimer = pg.time.get_ticks()

        if self.hidden and pg.time.get_ticks() - self.hide_timer > 3000:
            self.hidden = False
            self.rect.centerx = (WIDTH / 2)
            self.rect.bottom = (HEIGHT - (HEIGHT * .1))
            self.sheild = 100

        keystate = pg.key.get_pressed()
        if keystate[pg.K_a] or keystate[pg.K_LEFT]:
            self.speedx = -4
        if keystate[pg.K_d] or keystate[pg.K_RIGHT]:
            self.speedx = 4


        if keystate[pg.K_r] or keystate[pg.K_SPACE] and not self.hidden:
            Player.shoot(self)

        # We are binding it to the screen
        # if self.rect.left <= 0:
        #     self.rect.left = 0
        # if self.rect.right >= WIDTH:
        #     self.rect.right = WIDTH

        # if self.rect.left <= 0:
        #     self.speedx = 5
        # if self.rect.right >= WIDTH:
        #     self.speedx = -5

        self.rect.x += self.speedx

    def shoot(self):
        now = pg.time.get_ticks()
        if ((now - self.last_shot) > self.shoot_delay):
            self.last_shot = now
            if self.power_level == 1:
                laser = Laser(player.rect.centerx, player.rect.top + 1, -10)
                shoot_snd.play()
                all_sprites.add(laser)
                Bullet_Group.add(laser)
            elif self.power_level == 2:
                b1 = Laser(player.rect.right, player.rect.top + 1, -10)
                b2 = Laser(player.rect.left, player.rect.top + 1, -10)
                all_sprites.add(b1)
                all_sprites.add(b2)
                Bullet_Group.add(b1)
                Bullet_Group.add(b2)
                shoot_snd.play()
            elif self.power_level == 3:
                self.shoot_delay = 175
                b1 = Laser(player.rect.right, player.rect.top + 1, -20)
                b2 = Laser(player.rect.left, player.rect.top + 1, -20)
                all_sprites.add(b1)
                all_sprites.add(b2)
                Bullet_Group.add(b1)
                Bullet_Group.add(b2)
                shoot_snd.play()
            elif self.power_level == 4:
                self.shoot_delay = 150
                b1 = Laser(player.rect.right, player.rect.top + 1, -20)
                b2 = Laser(player.rect.left, player.rect.top + 1, -20)
                b3 = Laser(player.rect.centerx, player.rect.top + 1, -10)
                all_sprites.add(b1)
                all_sprites.add(b2)
                all_sprites.add(b3)
                Bullet_Group.add(b1)
                Bullet_Group.add(b2)
                Bullet_Group.add(b3)
                shoot_snd.play()
            elif self.power_level >= 5 < 10:
                self.shoot_delay = 100
                b1 = Laser(player.rect.right, player.rect.top + 1, -20)
                b2 = Laser(player.rect.left, player.rect.top + 1, -20)
                b3 = Laser(player.rect.centerx, player.rect.top + 1, -10)
                b4 = Laser(player.rect.centerx, player.rect.top + 1, -20, 5)
                b5 = Laser(player.rect.centerx, player.rect.top + 1, -20, -5)
                all_sprites.add(b1)
                all_sprites.add(b2)
                all_sprites.add(b3)
                all_sprites.add(b4)
                all_sprites.add(b5)
                Bullet_Group.add(b1)
                Bullet_Group.add(b2)
                Bullet_Group.add(b3)
                Bullet_Group.add(b4)
                Bullet_Group.add(b5)
                shoot_snd.play()

    def hide(self):
        # Hide Player Temporarally
        self.lives -= 1
        self.hidden = True
        self.hide_timer = pg.time.get_ticks()
        self.rect.x = HEIGHT+200


#####################################################
class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((35, 35))
        self.image_original = asteriod_sprite
        self.image_original = pg.transform.scale(asteriod_sprite, (35, 35))
        self.image_original.set_colorkey(BLACK)
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()
        self.radius = (self.rect.width * .65 / 2)
        # pg.draw.circle(self.image_original, RED, self.rect.center, self.radius)
        self.rect.centerx = R.randint(10, (HEIGHT - 10))
        self.rect.bottom = 0
        self.speedy = R.randint(1, 5)
        self.speedx = R.randint(-3, 3)
        self.rot = 0
        self.rot_speed = R.randint(-8, 8)
        self.last_update = pg.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top >= HEIGHT:
            self.rect.center = ((R.randint(0, WIDTH)), -10)
        if self.rect.left >= WIDTH:
            self.rect.right = 0
        if self.rect.right <= 0:
            self.rect.left = WIDTH

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            # Do the rotation
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_original, self.rot)
            self.image = new_image
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def spawn():
        npc = NPC()
        NPC_Group.add(npc)
        all_sprites.add(npc)


#####################################################
class STAR(pg.sprite.Sprite):
    def __init__(self):
        super(STAR, self).__init__()
        self.image = pg.Surface((3, 3))
        self.image.fill(White)
        self.rect = self.image.get_rect()
        self.rect.centerx = R.randint(10, (WIDTH - 10))
        self.rect.centery = R.randint(0, HEIGHT)
        self.rect.bottom = 0
        self.speedy = R.randint(8, 25)
        self.speedx = R.randint(-2, 2)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top >= HEIGHT:
            self.rect.center = ((R.randint(0, WIDTH)), -10)
        if self.rect.left >= WIDTH:
            self.rect.right = 0
        if self.rect.right <= 0:
            self.rect.left = WIDTH

    def spawn():
        star = STAR()
        STAR_Group.add(star)
        all_sprites.add(star)


#####################################################
class Laser(pg.sprite.Sprite):
    def __init__(self, x, y, speedy, speedx=0):
        super(Laser, self).__init__()
        self.image = pg.Surface((5, 10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = speedy
        self.speedx = speedx


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # Kill the bullet
        if self.rect.bottom < 0:
            self.kill()


#####################################################
class Explosion(pg.sprite.Sprite):
    def __init__(self, center, size):
        super(Explosion, self).__init__()
        self.size = size
        self.image = explosion_animation[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_animation[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_animation[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


#####################################################
class Pow(pg.sprite.Sprite):
    def __init__(self, center):
        super(Pow, self).__init__()
        self.type = R.choice(powerups_chance)
        self.image = pows_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()


#####################################################
#  Game Funtions
#####################################################
def draw_text(surf, text, size, x, y, color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    bar_len = 100
    bar_height = 10
    fill = (pct / 100) * bar_len
    outline_rect = pg.Rect(x, y, bar_len, bar_height)
    fill_rect = pg.Rect(x, y, fill, bar_height)
    pg.draw.rect(surf, BLUE, fill_rect)
    pg.draw.rect(surf, White, outline_rect, 2)

def drawlives(surf, x, y, lives, image):
    for i in range(lives):
        image_rect = image.get_rect()
        image_rect.x = x+30*i
        image_rect.y = y
        surf.blit(image, image_rect)

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "SHMUP", 64, WIDTH/2, HEIGHT/4, White)
    draw_text(screen, "Arrows and 'a' and 'd' move. Space is to shoot", 22, WIDTH/2, HEIGHT/2, White)
    draw_text(screen, "Press a key to Play", 18, WIDTH/2, HEIGHT * 3 / 4, White)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False
# Game Constants
#####################################################
HEIGHT = 700
WIDTH = 500
FPS = 60

# Colors
BLACK = (0, 0, 0)
White = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

TITLE = "Shump"

font_name = pg.font.match_font("arial")

powerups_list = ["shield", "gun"]
powerups_chance = ["shield", "shield", "shield", "shield", "shield", "shield", "gun"]

POWERUP_Timer = 4000
#####################################################

# Folder Variables
#####################################################
game_folder = path.dirname(__file__)
images_folder = path.join(game_folder, "Images")
sprite_folder = path.join(images_folder, "Sprites")
sprite_enemy_folder = path.join(sprite_folder, "enemy")
sprite_player_folder = path.join(sprite_folder, "Player")
background_folder = path.join(images_folder, "Background")
sounds_folder = path.join(game_folder, "Sounds")
backgroud_sound = path.join(sounds_folder, "Background")
expload_sounds = path.join(sounds_folder, "Expload")
laser_sounds = path.join(sounds_folder, "Laser")
scores_folder = path.join(game_folder, "Scores")
explosion_folder = path.join(sprite_folder, "Explosions")
player_explosions_folder = path.join(sprite_folder, "Player Explosions")
PowerUps_folder = path.join(sprite_folder, "PowerUps")
#####################################################

# Initialize Pygame and create window
#####################################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()
#####################################################

# Load Sounds
#####################################################
shoot_snd = pg.mixer.Sound(path.join(laser_sounds, "laser1.wav"))
explosion_snds = []
for snd in ["expl3.wav", "expl6.wav"]:
    explosion_snds.append(pg.mixer.Sound(path.join(expload_sounds, snd)))

pg.mixer.music.load(path.join(backgroud_sound, "Orbitron.wav"))
pg.mixer.music.set_volume(2)
pg.mixer.music.play(loops=-1)
#####################################################

# Load Images
#####################################################
# Background Loading
background = pg.image.load(path.join(background_folder, "background.png")).convert()
background = pg.transform.scale(background, (WIDTH, HEIGHT))
background_rect = background.get_rect()

# Player Images Loaded
Player_sprite = pg.image.load(path.join(sprite_player_folder, "Player.png")).convert()

# Lives Image
player_mini_image = pg.transform.scale(Player_sprite, (20, 20))
player_mini_image.set_colorkey(BLACK)

# Enemies Image Loaded
asteriod_sprite = pg.image.load(path.join(sprite_enemy_folder, "NPC_Asteriod.png")).convert()
asteriod_rect = background.get_rect()

explosion_animation = {}
explosion_animation["lg"] = []
explosion_animation["sm"] = []
explosion_animation["player"] = []
for i in range(0, 9):
    fn = "regularExplosion0{}.png".format(i)
    img = pg.image.load(path.join(explosion_folder, fn)).convert()
    img.set_colorkey(BLACK)
    img_lg = pg.transform.scale(img, (100, 100))
    img_sm = pg.transform.scale(img, (40, 40))
    explosion_animation["sm"].append(img_sm)
    explosion_animation["lg"].append(img_lg)

for i in range(0, 9):
    fn = "sonicExplosion0{}.png".format(i)
    player_explosion = pg.image.load(path.join(player_explosions_folder, fn)).convert()
    player_explosion.set_colorkey(BLACK)
    explosion_animation["player"].append(player_explosion)

# Load in Power up Images
pows_images = {}
for i in range(len(powerups_list)):
    fn = "img_{}.png".format(i)
    pows_images[powerups_list[i]] = pg.image.load(path.join(PowerUps_folder, fn)).convert()

#####################################################

# Create Sprite Groups
#####################################################
all_sprites = pg.sprite.Group()
player_Group = pg.sprite.Group()
NPC_Group = pg.sprite.Group()
Laser_Group = pg.sprite.Group()
Bullet_Group = pg.sprite.Group()
STAR_Group = pg.sprite.Group()
Enemey_Bullet_Group = pg.sprite.Group()
Powerups_Group = pg.sprite.Group()


#####################################################
# Game Loop
#####################################################
# Game Update Variables
###################################
playing = True
game_over = True
score = 0

###################################
while playing:
    if game_over:
        show_go_screen()
        game_over = False
        # Create Game Objects
        #####################################################
        player = Player()
        for i in range(10):
            NPC.spawn()

        for i in range(20):
            STAR.spawn()

        #####################################################

        # Add Objects to Sprite Group
        #####################################################
        player_Group.add(player)

        for i in player_Group:
            all_sprites.add(i)
        for i in NPC_Group:
            all_sprites.add(i)
        for i in Bullet_Group:
            all_sprites.add(i)
        #####################################################
    ###############################
    # Timing
    clock.tick(FPS)

    ###############################
    # Collecting Input

    # QUITING THE GAME
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                playing = False
            # if event.key == pg.K_SPACE:
            #     Player.shoot()
        if event.type == pg.QUIT:
            playing = False

    ###############################
    # Updates
    all_sprites.update()


    ###############################
    # If NPC hits Player
    hits = pg.sprite.spritecollide(player, NPC_Group, True, pg.sprite.collide_circle)
    for hit in hits:
        NPC.spawn()
        R.choice(explosion_snds).play()
        player.sheild -= hit.radius * 2
        exlp = Explosion(player.rect.center, "sm")
        all_sprites.add(exlp)
        if player.sheild <= 0:
            death_expl = Explosion(player.rect.center, "player")
            R.choice(explosion_snds).play()
            all_sprites.add(death_expl)
            player.hide()

            if player.lives <= 0:
                game_over = True

    ###############################
    # If Laser hits npc
    hits = pg.sprite.groupcollide(NPC_Group, Bullet_Group, True, True)
    for hit in hits:
        score += 30
        expl = Explosion(hit.rect.center, "sm")
        all_sprites.add(expl)
        R.choice(explosion_snds).play()
        NPC.spawn()
        pow = Pow(hit.rect.center)
        if R.random() > .999999:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            Powerups_Group.add(pow)
    ###############################
    # If Power up hits player
    # hits = pg.sprite.spritecollide(player, Powerups_Group, True, pg.sprite.spritecollide)
    # for hit in hits:
    #     if hit.type == "shield":
    #         player.shields_up(30)
    #     elif hit.type == "gun":
    #         player.gun_powu_up()



    ###############################
    # Render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # Draw Hud
    draw_text(screen, "Score: " + str(score), 18, WIDTH / 2, 10, White)
    draw_bar(screen, 5, 10, player.sheild)
    drawlives(screen, WIDTH-100, 10, player.lives, player_mini_image)

    pg.display.flip()
    ###############################

pg.quit()
#####################################################
