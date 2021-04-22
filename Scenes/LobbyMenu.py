import pygame, sys
import Constants
import Game
from pygame.locals import *


mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Menu')
size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x , y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    
    while True:

        screen.fill((0,0,0))
        
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                Game.main()
        if button_2.collidepoint((mx, my)):
            if click:
                options_menu()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

        draw_text('Menu - The Ares game!', font, (255, 255, 255), screen, 20, 20)
        draw_text('Game', font, (255, 255, 255), screen, 50, 100)
        draw_text('Options', font, (255, 255, 255), screen, 50, 200)
        draw_text('Quit', font, (255, 255, 255), screen, 50, 300)

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

