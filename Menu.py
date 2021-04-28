import pygame, sys
import NewGame
import os
from pygame.locals import *


mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Menu')
size = [500, 500]
screen = pygame.display.set_mode(size)
image_path = os.path.dirname(__file__) + '/Images/'


font = pygame.font.SysFont(None, 20)

class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'Menu.png').convert()
        self.background = pygame.transform.scale(
            self.background, (500, 500))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

def draw_text(text, font, color, surface, x , y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

click = False
bg = background()

def main_menu():
    while True:

        screen.fill((0,0,0))
        bg.draw(screen)
        
        
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(140, 156, 220, 50)
        button_2 = pygame.Rect(140, 256, 220, 50)
        button_3 = pygame.Rect(140, 356, 220, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                NewGame.main()
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

        draw_text('Game', font, (255, 255, 255), screen, 230, 165)
        draw_text('Options', font, (255, 255, 255), screen, 230, 265)
        draw_text('Quit', font, (255, 255, 255), screen, 230, 365)

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
        screen.fill((0,0,0))
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        draw_text('Druk op escape om terug te gaan', font, (255, 255, 255), screen, 20, 50)
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