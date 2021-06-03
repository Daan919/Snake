import pygame
from pygame.locals import *
from pygame import mixer
import pickle
import math
import Menu
import os
from os import path, walk

pygame.mixer.pre_init(44100, -16, 2, 512)

mixer.init()
pygame.init()
pygame.display.init()

clock = pygame.time.Clock()
tile_size = 25
level_counter = 13

screenWidth = 1000
screenHeight = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('ons eerste spelletje')
image_path = os.path.dirname(__file__) + '/Images' + \
    str(math.ceil(level_counter/3)) + '/'
sound_path = os.path.dirname(__file__) + '/Sounds/'

font_score = pygame.font.SysFont("Comic Sans", tile_size)

# load sounds
sound_get_coin = pygame.mixer.Sound(sound_path + "coin.wav")
sound_get_coin.set_volume(0.5)
sound_game_over = pygame.mixer.Sound(sound_path + "game_over.wav")
sound_game_over.set_volume(0.5)

game_over = 0

white = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


def drawText(text, font, tect_col, x, y):
    img = font.render(text, True, tect_col)
    screen.blit(img, (x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path + 'barbarian.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(image_path +
                                            'background.png').convert()
        self.background = pygame.transform.scale(self.background,
                                                 (screenWidth, screenHeight))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


class level(pygame.sprite.Sprite):
    def mapTiles(self, data):

        self.tile_list = []
        self.coin_list = pygame.sprite.Group()
        self.spike_list = pygame.sprite.Group()
        self.lava_list = pygame.sprite.Group()
        self.water_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.key_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()

        self.score = 0

        self.img_dirt = pygame.image.load(image_path + 'dirt.png')
        self.img_grass = pygame.image.load(image_path + 'grass.png')
        self.img_static_platform_left = pygame.image.load(
            image_path + 'static_platform_left.png')
        self.img_static_platform_mid = pygame.image.load(
            image_path + 'static_platform_mid.png')
        self.img_static_platform_right = pygame.image.load(
            image_path + 'static_platform_right.png')
        self.img_water = pygame.image.load(image_path + 'water.png')
        self.img_lava = pygame.image.load(image_path + 'lava.png')
        self.img_spike_right = pygame.image.load(image_path +
                                                 'spike_right.png')
        self.img_spike_left = pygame.image.load(image_path + 'spike_left.png')
        self.img_spike_up = pygame.image.load(image_path + 'spike_up.png')
        self.img_spike_down = pygame.image.load(image_path + 'spike_down.png')
        self.img_key = pygame.image.load(image_path + 'key.png')
        self.img_door = pygame.image.load(image_path + 'door.png')
        self.img_coin = pygame.image.load(image_path + 'Coin.png')
        self.img_enemy = pygame.image.load(image_path + 'coin.png')

        self.img_dirt = pygame.transform.scale(self.img_dirt,
                                               (tile_size, tile_size))
        self.img_grass = pygame.transform.scale(self.img_grass,
                                                (tile_size, tile_size))
        self.img_static_platform_left = pygame.transform.scale(
            self.img_static_platform_left, (tile_size, tile_size))
        self.img_static_platform_mid = pygame.transform.scale(
            self.img_static_platform_mid, (tile_size, tile_size))
        self.img_static_platform_right = pygame.transform.scale(
            self.img_static_platform_right, (tile_size, tile_size))
        self.img_water = pygame.transform.scale(self.img_water,
                                                (tile_size, tile_size))
        self.img_lava = pygame.transform.scale(self.img_lava,
                                               (tile_size, tile_size))
        self.img_spike_right = pygame.transform.scale(self.img_spike_right,
                                                      (tile_size, tile_size))
        self.img_spike_left = pygame.transform.scale(self.img_spike_left,
                                                     (tile_size, tile_size))
        self.img_spike_up = pygame.transform.scale(self.img_spike_up,
                                                   (tile_size, tile_size))
        self.img_spike_down = pygame.transform.scale(self.img_spike_down,
                                                     (tile_size, tile_size))
        self.img_key = pygame.transform.scale(self.img_key,
                                              (tile_size, tile_size))
        self.img_door = pygame.transform.scale(self.img_door,
                                               (tile_size, tile_size))
        self.img_coin = pygame.transform.scale(self.img_coin,
                                               (tile_size, tile_size))
        self.img_enemy = pygame.transform.scale(self.img_enemy,
                                                (tile_size, tile_size))

        row_count = 0
        for row in data:
            colum_count = 0
            for tile in row:
                if tile == 1:
                    img_rect = self.img_dirt.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_dirt, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img_rect = self.img_grass.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_grass, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img_rect = self.img_static_platform_left.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_static_platform_left, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img_rect = self.img_static_platform_mid.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_static_platform_mid, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img_rect = self.img_static_platform_right.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_static_platform_right, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    platform = platform_move(colum_count * tile_size,
                                             row_count * tile_size, 1, 0)
                    self.platform_list.add(platform)
                if tile == 7:
                    platform = platform_move(colum_count * tile_size,
                                             row_count * tile_size, 0, 1)
                    self.platform_list.add(platform)
                if tile == 8:
                    water = Water(colum_count * tile_size,
                                  row_count * tile_size + (tile_size // 2), 1,
                                  0)
                    self.water_list.add(water)
                if tile == 9:
                    lava = Lava(colum_count * tile_size,
                                row_count * tile_size + (tile_size // 2))
                    self.lava_list.add(lava)
                if tile == 10:
                    spike = spikes_r(
                        colum_count * tile_size + (tile_size // 2),
                        row_count * tile_size)
                    self.spike_list.add(spike)
                if tile == 11:
                    spike = spikes_l(
                        colum_count * tile_size + (tile_size // 2),
                        row_count * tile_size)
                    self.spike_list.add(spike)

                    # create spike up down
                if tile == 12:
                    spike = spikes_l(
                        colum_count * tile_size + (tile_size // 2),
                        row_count * tile_size)
                    self.spike_list.add(spike)
                if tile == 13:
                    spike = spikes_l(
                        colum_count * tile_size + (tile_size // 2),
                        row_count * tile_size)
                    self.spike_list.add(spike)

                if tile == 14:
                    key = Keys(colum_count * tile_size, row_count * tile_size)
                    self.key_list.add(key)
                if tile == 15:
                    door = Doors(colum_count * tile_size,
                                 row_count * tile_size)
                    self.door_list.add(door)
                if tile == 16:
                    coin = coins(colum_count * tile_size + (tile_size // 2),
                                 row_count * tile_size + (tile_size // 2))
                    self.coin_list.add(coin)
                if tile == 17:  # create enamy class
                    coin = coins(colum_count * tile_size + (tile_size // 2),
                                 row_count * tile_size + (tile_size // 2))
                    self.coin_list.add(coin)

                if tile == 18:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_1.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 19:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_2.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 20:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_3.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 21:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_4.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 22:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_5.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 23:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_6.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 24:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_7.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 25:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_8.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 26:
                    self.img_deco_block = pygame.image.load(image_path +
                                                            'deco_block_9.png')
                    self.img_deco_block = pygame.transform.scale(
                        self.img_deco_block, (tile_size, tile_size))
                    img_rect = self.img_deco_block.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco_block, img_rect)
                    self.tile_list.append(tile)
                if tile == 27:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_1.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 28:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_2.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 29:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_3.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 30:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_4.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 31:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_5.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 32:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_6.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 33:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_7.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 34:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_8.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 35:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_9.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                if tile == 36:
                    self.img_deco = pygame.image.load(image_path +
                                                      'decoratie_10.png')
                    self.img_deco = pygame.transform.scale(
                        self.img_deco, (tile_size, tile_size))
                    img_rect = self.img_deco.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.img_deco, img_rect)
                    self.tile_list.append(tile)
                colum_count += 1
            row_count += 1

        score_coin = coins(tile_size // 2, tile_size // 2)
        self.coin_list.add(score_coin)

    def draw(self, ):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.images_right_walk = []
        self.images_left_walk = []
        self.index = 0
        self.index_walk = 0
        self.counter = 0
        self.counter_walk = 0
        for number in range(1, 7):
            img_right = pygame.image.load(image_path + f'run{number}.png')
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        for number in range(1, 5):
            img_right_walk = pygame.image.load(image_path +
                                               f'walk{number}.png')
            img_left_walk = pygame.transform.flip(img_right_walk, True, False)
            self.images_right_walk.append(img_right_walk)
            self.images_left_walk.append(img_left_walk)

        self.image = self.images_right[self.index]
        self._image_walk = self.images_right_walk[self.index_walk]
        self.dead_image = pygame.image.load(image_path + 'ghost.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.direction = 0
        self.life = 3
        self.jumped = False
        self.in_air = False
        self.walking = False
        self.walking_sound = True

    def update(self, game_over):
        dx = 0
        dy = 0
        col_tresh = 20
        run_cooldown = 10
        walk_cooldown = 10

        if game_over == 0:

            key = pygame.key.get_pressed()
            if key[pygame.
                   K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
                self.walking = True

            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
                self.walking = True

            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.counter_walk += 1
                self.index = 0
                self.walking = False
                self.walking_sound = True
                if self.direction == 1:
                    self.image = self.images_right_walk[self.index_walk]
                elif self.direction == -1:
                    self.image = self.images_left_walk[self.index_walk]

            # animatie voor het rennen > kijkt naar de array met de png's
            if self.counter > run_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                elif self.direction == -1:
                    self.image = self.images_left[self.index]

            if self.counter_walk > walk_cooldown:
                self.counter_walk = 0
                self.index_walk += 1
                if self.index_walk >= len(self.images_right_walk):
                    self.index_walk = 0
                if self.direction == 1:
                    self.image = self.images_right_walk[self.index]
                elif self.direction == -1:
                    self.image = self.images_left_walk[self.index]

            # gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            self.in_air = True

            # check for collision
            for tile in lv.tile_list:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y,
                                       self.width, self.height):
                    dx = 0

                if tile[1].colliderect(self.rect.x, self.rect.y + dy,
                                       self.width, self.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            if pygame.sprite.spritecollide(self, lv.lava_list, False):
                self.life -= 1
                if self.life != 0:
                    self.rect.x = 100
                    self.rect.y = screenHeight - 130
                if self.life == 0:
                    game_over = 1

            if pygame.sprite.spritecollide(self, lv.spike_list, False):
                self.life -= 1
                if self.life != 0:
                    self.rect.x = 100
                    self.rect.y = screenHeight - 130
                if self.life == 0:
                    game_over = 1

            for platform in lv.platform_list:
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y,
                                             self.width, self.height):
                    dx = 0
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy,
                                             self.width, self.height):
                    if abs((self.rect.top + dy) -
                           platform.rect.bottom) < col_tresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    elif abs((self.rect.bottom + dy) -
                             platform.rect.top) < col_tresh:
                        self.rect.bottom = platform.rect.top - 1
                        dy = 0
                        self.in_air = False
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            for platform in lv.water_list:
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y,
                                             self.width, self.height):
                    dx = 0
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy,
                                             self.width, self.height):
                    if abs((self.rect.top + dy) -
                           platform.rect.bottom) < col_tresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    elif abs((self.rect.bottom + dy) -
                             platform.rect.top) < col_tresh:
                        self.rect.bottom = platform.rect.top - 1
                        dy = 0
                        self.in_air = False
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            # update speler zijn coordinates
            self.rect.x += dx
            self.rect.y += dy

        if game_over == 1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5

        screen.blit(self.image, self.rect)

        return game_over

    def reset(self, x, y):
        img = img = pygame.image.load(image_path + "Fall (32x32).png")
        self.image = pygame.transform.scale(img, (20, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = False


class coins(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + 'coin.png')
        self.image = pygame.transform.scale(img,
                                            (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Doors(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + 'door.png')
        self.image = pygame.transform.scale(
            img, (int(tile_size), int(tile_size * 2)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y + tile_size)


class Keys(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + 'key.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class platform_move(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "moving_platform.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 100:
            self.move_direction *= -1
            self.move_counter *= -1


class Water(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "water.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 100:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "lava.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class spikes_r(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "spike_right.png")
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class spikes_l(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "spike_left.png")
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Load in level data and create world
pickle_in = open(f"level{level_counter}_data", "rb")
World_data = pickle.load(pickle_in)
lv = level()
realLevel = lv.mapTiles(World_data)
player = player(130, screenHeight - 130)


def levelUp(counter):
    counter += 1
    return counter


def main(game_over):
    global level_counter
    bg = background()
    running = True
    key_found = False
    game_over_sound = True

    while running:
        global lv
        clock.tick(60)
        bg.draw(screen)
        lv.draw()

        if game_over == 0:
            lv.platform_list.update()
        if game_over != 0:
            drawText("Game Over", font_score, BLACK, screenHeight // 2.5,
                     screenWidth // 2)

            if game_over_sound:
                sound_game_over.play()
                game_over_sound = False

        lv.door_list.draw(screen)
        lv.key_list.draw(screen)
        lv.coin_list.draw(screen)
        lv.water_list.draw(screen)
        lv.lava_list.draw(screen)
        lv.spike_list.draw(screen)

        lv.platform_list.draw(screen)
        game_over = player.update(game_over)

        # update score

        if pygame.sprite.spritecollide(player, lv.coin_list, True):
            lv.score += 1
            sound_get_coin.play()
        drawText(" X" + str(lv.score), font_score, white, tile_size // 2,
                 tile_size // 4)
        drawText(
            str(player.life) + " lifes left", font_score, white, tile_size * 4,
            tile_size // 4)

        # update level
        if pygame.sprite.spritecollide(player, lv.door_list,
                                       False) and key_found:
            print("next level")
            level_counter = levelUp(level_counter)
            player.reset(100, screenHeight - 130)
            # Change Tiles and Load in level data and create world

            pickle_in = open(f"level{level_counter}_data", "rb")
            World_data = pickle.load(pickle_in)
            realLevel = lv.mapTiles(World_data)
            print(level_counter)

        if pygame.sprite.spritecollide(player, lv.key_list, True):
            key_found = True
            print("Go to Next level")

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                runnig = False


# main(level_counter,game_over)
