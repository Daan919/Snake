import pygame
import os
from pygame.math import Vector2

clock = pygame.time.Clock()
pygame.init()

image_path = os.path.dirname(__file__) + '/images/'
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

bg = pygame.image.load(image_path + 'bg.png')


class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load(image_path + 'idle.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= Vector2(2, 1)
        if key[pygame.K_RIGHT]:
            dx += 1

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #update speler zijn coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screenHeight:
            self.rect.bottom = screenHeight
            dy = 0
        #teken de player op het scherm
        screen.blit(self.image, self.rect, (0, 0, 30, 30))


player = player(0, screenHeight - 32)


def main():
    running = True
    clock.tick(30)
    while running:
        screen.blit(bg, (0, 0))
        player.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


main()
