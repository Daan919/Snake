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


class spriteSheet(object):
    sprite_sheet = None

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        # Creeer een lege image
        image = pygame.Surface([width, height]).convert()

        # Kopieer het de uitgeknipte sprite naar het lege image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image


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


grootPlatform = (0, 0, 978, 132)


class level(object):
    def __init__(self, player):
        self.coin_list = pygame.sprite.Group()
        self.spike_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.player = player
        # Variabele bevat platforms van verschillende grote word gebruikt om platforms te plaatsen
        self.platforms

    def platform(self, x, y, width, height):
        spriteSheet = pygame.image.load(
            image_path + 'platforms.png').convert()

        image = spriteSheet.get_image(x, y, width, height)
        self.platforms.append(iamge)
        self.rect = self.platforms.get_rect()

    def draw(self):
        self.platform_list.draw(screen)


class level1(level):

    super.__init__(level)

    def __init__(self):

        level = [[grootPlatform, 50, 400],
                 ]

        for platform in level:
            block = platform[0]
            blockX = platform[1]
            blockY = platform[2]
            self.platform_list.add(block)


def main():

    bg = background()
    lv = level1()
    running = True

    while running:
        clock.tick(60)

        bg.draw(screen)
        lv.draw
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
