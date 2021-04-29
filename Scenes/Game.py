import pygame
from pygame.locals import *
import os
from pygame import mixer


pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
pygame.display.init()


clock = pygame.time.Clock()

screenWidth = 500
screenHeight = 500
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('ons eerste spelletje')
image_path = os.path.dirname(__file__) + '/images/'
sound_path = os.path.dirname(__file__) + '/Sounds/'


tile_size = 25
game_over = 0

font_score = pygame.font.SysFont("Comic Sans", tile_size)

# collors
white = (255, 255, 255)
BLUE = (0,   0, 255)
BLACK = (0, 0, 0)

world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 5, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 4, 4, 4, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 2, 2, 2, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]

# load sounds
sound_get_coin = pygame.mixer.Sound(sound_path + "coin.wav")
sound_get_coin.set_volume(0.5)
sound_game_over = pygame.mixer.Sound(sound_path + "game_over.wav")
sound_game_over.set_volume(0.5)


def drawText(text, font, tect_col, x, y):
    img = font.render(text, True, tect_col)
    screen.blit(img, (x, y))


class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'bg.png').convert()
        self.background = pygame.transform.scale(
            self.background, (screenWidth, screenHeight))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


class level(pygame.sprite.Sprite):

    def __init__(self, data):
        self.tile_list = []
        self.coin_list = pygame.sprite.Group()
        self.lava_list = pygame.sprite.Group()
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

        # self.coin_img = pygame.image.load(image_path + "coin.png")
        # self.coin = self.coin_img
        # self.coin = pygame.transform.scale(
        #     self.coin, (tile_size, tile_size))

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
                    platform = platform_move(
                        colum_count * tile_size, row_count * tile_size, 1, 0)
                    self.platform_list.add(platform)
                if tile == 4:
                    platform = platform_move(
                        colum_count * tile_size, row_count * tile_size, 0, 1)
                    self.platform_list.add(platform)
                if tile == 5:
                    coin = coins(
                        colum_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    self.coin_list.add(coin)
                if tile == 6:
                    lava = Lava(colum_count * tile_size,
                                row_count * tile_size + (tile_size // 2))
                    self.lava_list.add(lava)

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

            if pygame.sprite.spritecollide(self, lv.lava_list, False):
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

            self.rect.x += dx
            self.rect.y += dy

        screen.blit(self.image, self.rect)

        return game_over


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


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(image_path + "lava.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


lv = level(world_data)
player = player(100, screenHeight - 130)


def main(game_over):

    bg = background()
    running = True

    while running:
        clock.tick(60)

        bg.draw(screen)
        lv.draw()

        if game_over == 0:
            lv.platform_list.update()
        if game_over != 0:
            drawText("Game Over", font_score, BLACK,
                     screenHeight // 2.5, screenWidth // 2)
            sound_game_over.play()

        lv.coin_list.draw(screen)
        lv.lava_list.draw(screen)

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

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                runnig = False


main(game_over)
