import pygame
import os

pygame.init()
pygame.display.init()
clock = pygame.time.Clock()

screenWidth = 1000
screenHeight = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight))
image_path = os.path.dirname(__file__) + '/images/'

BLUE = (0,   0, 255)
tile_size = 50

world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
]


class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'Starry_night_Image.png').convert()
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

        self.platform_img = pygame.image.load(image_path + "dirt.png")
        self.dirt = self.platform_img
        self.dirt = pygame.transform.scale(
            self.dirt, (tile_size, tile_size))
        self.platform_img = pygame.image.load(image_path + "grass.png")
        self.grass = self.platform_img
        self.grass = pygame.transform.scale(
            self.grass, (tile_size, tile_size))

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
                colum_count += 1
            row_count += 1

    def draw(self,):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


def main():

    bg = background()
    lv = level(world_data)
    running = True

    while running:
        clock.tick(60)

        bg.draw(screen)
        lv.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
