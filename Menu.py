
import pygame
import sys
import NewGame
import os
from pygame.locals import *


mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Menu')
size = [1000, 1000]
screen_hight = 1000
screen_width = 1000
screen = pygame.display.set_mode(size)
image_path = os.path.dirname(__file__) + '/Images1/'

buttonhight = screen_hight / 10
buttonWidth = screen_width / 3


font = pygame.font.SysFont(None, screen_width // 20)


class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'Menu.png').convert()
        self.background = pygame.transform.scale(
            self.background, size)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
bg = background()


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        bg.draw(screen)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(
            screen_width / 3, buttonhight * 3, buttonWidth, buttonhight)
        button_2 = pygame.Rect(
            screen_width / 3, buttonhight * 5, buttonWidth, buttonhight)
        button_3 = pygame.Rect(
            screen_width / 3, buttonhight * 7, buttonWidth, buttonhight)

        if button_1.collidepoint((mx, my)):
            if click:
                NewGame.main(NewGame.game_over)
        if button_2.collidepoint((mx, my)):
            if click:
                options_menu()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), button_1, 1)
        pygame.draw.rect(screen, (255, 0, 0), button_2, 1)
        pygame.draw.rect(screen, (255, 0, 0), button_3, 1)

        draw_text('Game', font, (255, 255, 255),
                  screen,  buttonWidth * 1.1, buttonhight * 3.4)
        draw_text('Options', font, (255, 255, 255),
                  screen,  buttonWidth * 1.1, buttonhight * 5.4)
        draw_text('Quit', font, (255, 255, 255),
                  screen,  buttonWidth * 1.1, buttonhight * 7.4)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def options_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        draw_text('Druk op escape om terug te gaan',
                  font, (255, 255, 255), screen, 20, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()
