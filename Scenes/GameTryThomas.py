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

grootPlatform = (1, 1, 976, 133)

class Platform(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("platforms.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class level():

platform_list = None

    def __init__(self, player):
        self.coin_list = pygame.sprite.Group()
        self.spike_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.player = player
    
    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        self.platform_list.draw(screen)
    
class level1(level):

    def __init__(self, player):

        level.__init__(self, player)
        
        level = [ [platforms.grooPlatform, 0, 0],
                  ]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[0]
            block.rect.y = platform[0]
            block.player = self.player
            self.platform_list.add(block)
        
def main():

    bg = background()
    running = True

    while running:
        clock.tick(60)

        bg.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
