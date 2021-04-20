import pygame
import os

pygame.init()

image_path = os.path.dirname(__file__) + '/images/'
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

playerImage = pygame.image.load(image_path + 'mainplayer.png')


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


class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player = pygame.sprite.Group()

        self.change_x = 0
        self.change_y = 0

        self.walking_frames_l = []
        self.walking_frames_r = []

        self.direction = "R"

        image = playerImage.get_image(0, 0, 50, 50)
        self.walking_frames_r.append(image)


p = player()
running = True

while running:
    screen.blit(p.walking_frames_r[0], (14, 44))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
