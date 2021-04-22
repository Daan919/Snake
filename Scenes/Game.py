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
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
                if tile == 3:
                    platform = platform_move(colum_count * tile_size, row_count * tile_size, 1, 0)
                    self.platform_list.add(platform)
                if tile == 4:
                    platform = platform_move(colum_count * tile_size, row_count * tile_size, 0, 1)
                    self.platform_list.add(platform)
                
                colum_count += 1
            row_count += 1

    def draw(self,):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

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


def main():

    bg = background()
    lv = level(world_data)
    running = True

    while running:
        clock.tick(60)

        bg.draw(screen)
        lv.draw()
        lv.platform_list.update()
        lv.platform_list.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
