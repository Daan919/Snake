import pygame
from pygame.locals import *
from pygame import mixer
import pickle
import Menu
import os
from os import path

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
pygame.display.init()

clock = pygame.time.Clock()
tile_size = 25

screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('ons eerste spelletje')
image_path = os.path.dirname(__file__) + '/Images/'
sound_path = os.path.dirname(__file__) + '/Sounds/'

door = pygame.image.load(image_path + "tiles_door.png")
key = pygame.image.load(image_path + "tiles_oldkey.png")

font_score = pygame.font.SysFont("Comic Sans", tile_size)

# load sounds
sound_get_coin = pygame.mixer.Sound(sound_path + "coin.wav")
sound_get_coin.set_volume(0.5)
sound_game_over = pygame.mixer.Sound(sound_path + "game_over.wav")
sound_game_over.set_volume(0.5)


sound_walking = pygame.mixer.Sound(sound_path + "walking.wav")
sound_walking.set_volume(0.5)

level_counter = 1
game_over = 0


white = (255, 255, 255)
BLUE = (0,   0, 255)
BLACK = (0, 0, 0)

def drawText(text, font, tect_col, x, y):
    img = font.render(text, True, tect_col)
    screen.blit(img, (x, y)) 

class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'background_Poseidon-02.png').convert()
        self.background = pygame.transform.scale(
            self.background, (screenWidth, screenHeight))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


class level(pygame.sprite.Sprite):

    def __init__(self, data):
        self.tile_list = []
        self.coin_list = pygame.sprite.Group()
        self.spike_list = pygame.sprite.Group()
        self.lava_list = pygame.sprite.Group()
        self.water_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.key_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()

        self.score = 0

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
                if tile == 7:
                    lava = Lava(colum_count * tile_size,
                                row_count * tile_size + (tile_size // 2))
                    self.lava_list.add(lava)
                if tile == 8:
                    spike = spikes_r(colum_count * tile_size + (tile_size // 2),
                                     row_count * tile_size)
                    self.spike_list.add(spike)
                if tile == 9:
                    spike = spikes_l(colum_count * tile_size,
                                     row_count * tile_size)
                    self.spike_list.add(spike)
                if tile == 10:
                    water = Water(colum_count * tile_size,
                                     row_count * tile_size + (tile_size // 2), 1, 0)
                    self.water_list.add(water)    
                if tile == 11:
                    door = Doors(colum_count * tile_size, row_count * tile_size)     
                    self.door_list.add(door)
                if tile == 12:
                    key = Keys(colum_count * tile_size, row_count * tile_size)     
                    self.key_list.add(key)    

                colum_count += 1
            row_count += 1

        score_coin = coins(tile_size // 2, tile_size // 2)
        self.coin_list.add(score_coin)    

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
        self.life = 3
        self.jumped = False
        self.in_air = False
        self.walking = False
        self.walking_sound = True

    def playWalkingSound(self):
        if self.walking and self.walking_sound:
            sound_walking.play()
        elif self.walking == False:
            sound_walking.stop()    

    def update(self, game_over):
        dx = 0
        dy = 0
        col_tresh = 20

        if game_over == 0:

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 5
                self.walking = True
                self.playWalkingSound()
                self.walking_sound = False

            if key[pygame.K_RIGHT]:
                dx += 5
                self.walking = True
                self.playWalkingSound()
                self.walking_sound = False

            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                sound_walking.stop()
                self.walking = False
                self.walking_sound = True

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
            
            for platform in lv.water_list:
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
        self.image = pygame.transform.scale(
            img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)       

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
        img = pygame.image.load(image_path + "spikes_right.png")
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class spikes_l(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "spikes_left.png")
        self.image = pygame.transform.scale(img, (tile_size // 2, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 

# Load in level data and create world
pickle_in = open(f"level{level_counter}_data","rb")
World_data = pickle.load(pickle_in)
lv = level(World_data)
player = player(100, screenHeight - 130)



def main(level_counter, game_over):

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
            drawText("Game Over", font_score, BLACK,
                     screenHeight // 2.5, screenWidth // 2)

            if game_over_sound:
                sound_walking.stop()
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
        drawText(" X" + str(lv.score), font_score,
                 white, tile_size // 2, tile_size // 4)
        drawText(str(player.life) + " lifes left", font_score,
                 white, tile_size * 4, tile_size // 4)


        # update level
        if pygame.sprite.spritecollide(player,lv.door_list, False) and key_found:
            print("next level")
            level_counter += 1
            player.reset(100, screenHeight - 130)
            # Load in level data and create world
            pickle_in = open(f"level{level_counter}_data","rb")
            World_data = pickle.load(pickle_in)
            lv = level(World_data)
            print(level_counter)
        
        if pygame.sprite.spritecollide(player,lv.key_list, True):
            key_found = True
            print("Go to Next level")    
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                runnig = False

# main(level_counter,game_over)          
