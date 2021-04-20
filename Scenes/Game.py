import pygame
import os

image_path = os.path.dirname(__file__) + '/images/'
screenWidth = 800
screenHeight = 600
pygame.display.set_mode((screenWidth, screenHeight))

pygame.image.load(image_path + 'mainplayer.png')


class spriteSheet(object):
    


class player(pygame.sprite.Sprite):
    def __init__(self):
        self.player = pygame.sprite.Group()


class enemies():
    pass


class coins():
    pass


class traps():
    pass


p = player()


def main():
    print(p.player)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

main()
