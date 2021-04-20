import pygame
import constants


class player():
    def __init__(self):

        self.change_x = 0
        self.change_y = 0
        self.velocity = 5
        self.direction = 'neutral'

    def draw(self, image, surface):
        self.image = image
        self.surface = surface
