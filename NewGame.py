import pygame
from pygame.locals import *
import pickle
import Menu
import os
from os import path

pygame.init()
pygame.display.init()
clock = pygame.time.Clock()

screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('ons eerste spelletje')
image_path = os.path.dirname(__file__) + '/Images/'

door = pygame.image.load(image_path + "tiles_door.png")
key = pygame.image.load(image_path + "tiles_oldkey.png")
level_counter = 1

BLUE = (0,   0, 255)
tile_size = 25

class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'background_Poseidon-02').convert()
        self.background = pygame.transform.scale(
            self.background, (screenWidth, screenHeight))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


class level(pygame.sprite.Sprite):

    def __init__(self, data):
        self.tile_list = []
        self.coin_list = pygame.sprite.Group()
        self.spike_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.key_list = pygame.sprite.Group()

        self.platform_img = pygame.image.load(image_path + "dirt.png")
        self.dirt = self.platform_img
        self.dirt = pygame.transform.scale(
            self.dirt, (tile_size, tile_size))
        self.platform_img = pygame.image.load(image_path + "grass.png")
        self.grass = self.platform_img
        self.grass = pygame.transform.scale(
            self.grass, (tile_size, tile_size))
        self.platform_img = pygame.image.load(image_path + "water.png")
        self.water = self.platform_img
        self.water = pygame.transform.scale(
            self.water, (tile_size, tile_size))
        self.platform_img = pygame.image.load(image_path + "waterwave.png")
        self.waterwave = self.platform_img
        self.waterwave = pygame.transform.scale(
            self.waterwave, (tile_size, tile_size))           

        self.coin_img = pygame.image.load(image_path + "grass.png")
        self.coin = self.coin_img
        self.coin = pygame.transform.scale(
            self.coin, (tile_size, tile_size))

        row_count = 0
        for row in data:
            colum_count = 0
            for tile in row:
                if tile == 1:
                    img_rect = self.dirt.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.dirt, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img_rect = self.grass.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.grass, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img_rect = self.water.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.water, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img_rect = self.waterwave.get_rect()
                    img_rect.x = colum_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (self.waterwave, img_rect)
                    self.tile_list.append(tile)           
                if tile == 5:
                    platform = platform_move(
                        colum_count * tile_size, row_count * tile_size, 1, 0)
                    self.platform_list.add(platform)
                if tile == 6:
                    platform = platform_move(
                        colum_count * tile_size, row_count * tile_size, 0, 1)
                    self.platform_list.add(platform)
                if tile == 9:
                    door = Doors(colum_count * tile_size, row_count * tile_size)     
                    self.door_list.add(door)
                if tile == 10:
                    key = Keys(colum_count * tile_size, row_count * tile_size)     
                    self.key_list.add(key)    

                colum_count += 1
            row_count += 1

    def draw(self,):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


class player():
    def __init__(self, x, y):
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

    def update(self):
        dx = 0
        dy = 0
        col_tresh = 20

        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False and self.in_air == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        self.in_air = True
        for tile in lv.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False

        for platform in lv.platform_list:
            if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if abs((self.rect.top + dy) - platform.rect.bottom) < col_tresh:
                    self.vel_y = 0
                    dy = platform.rect.bottom - self.rect.top
                elif abs((self.rect.bottom + dy) - platform.rect.top) < col_tresh:
                    self.rect.bottom = platform.rect.top - 1
                    dy = 0
                    self.in_air = False
                if platform.move_x != 0:
                    self.rect.x += platform.move_direction

        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)

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



player = player(100, screenHeight - 130)

class Doors(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + 'tiles_door.png')
        self.image = pygame.transform.scale(
            img, ( int (tile_size * 1.5), int (tile_size * 2)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Keys(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + 'tiles_oldkey.png')
        self.image = pygame.transform.scale(
            img, ( int (tile_size * 1.5), int (tile_size * 2)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class coins(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + 'coin.png')
        self.image = pygame.transform.scale(
            img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)        

class platform_move(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "platform.png")
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

#  functie maken die return van lv (World_data) weergeeft

# Load in level data and create world
pickle_in = open(f"level{level_counter}_data","rb")
World_data = pickle.load(pickle_in)
lv = level(World_data)


def main(level_counter):

    bg = background()
    running = True
    key_found = False

    while running:
        global lv
        clock.tick(60)
        bg.draw(screen)
        lv.draw()
        lv.platform_list.update()
        player.update()
        lv.platform_list.draw(screen)
        lv.door_list.draw(screen)
        if pygame.sprite.spritecollide(player,lv.door_list, False) and key_found:
            print("next level")
            level_counter += 1
            player.reset(100, screenHeight - 130)
            # Load in level data and create world
            pickle_in = open(f"level{level_counter}_data","rb")
            World_data = pickle.load(pickle_in)
            lv = level(World_data)
            print(level_counter)
        lv.key_list.draw(screen)
        if pygame.sprite.spritecollide(player,lv.key_list, True):
            key_found = True
            print("Go to Next level")    
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                runnig = False
          
