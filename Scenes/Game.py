import pygame
import os

pygame.init()
pygame.display.init()
clock = pygame.time.Clock()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
image_path = os.path.dirname(__file__) + '/images/'

BLUE = (0,   0, 255)


class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'Starry_night_Image.png').convert()
        self.background = pygame.transform.scale(
            self.background, (screenWidth, screenHeight))

    def draw(self, screen):
        screen.fill(BLUE)
        screen.blit(self.background, (0, 0))


class level(pygame.sprite.Sprite):

    def __init__(self):
        self.coin_list = pygame.sprite.Group()
        self.spike_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()

        platform_smal = pygame.image.load(image_path + "")

    def platform(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = spriteSheet(
            image_path + 'platforms.png')

        image = sprite_sheet.get_image(0, 0, 132, 978)
        self.platforms.append(iamge)
        self.rect = self.platforms.get_rect()

    def draw(self):
        self.platform_list.draw(screen)

    def level1(self):

        level = [grootPlatform, 50, 400]

        for platform in level:
            block = platform[0]
            blockX = platform[1]
            blockY = platform[2]
            self.platform_list.add(block)


def main():

    bg = background()
    lv = level()
    lv.platform()

    running = True

    while running:
        clock.tick(60)

        bg.draw(screen)

        lv.level1()
        lv.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
