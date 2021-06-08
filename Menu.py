
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

buttonhight =  int(screen_hight / 10)
buttonWidth = int(screen_width / 3)


font = pygame.font.SysFont(None, screen_width // 20)

#class that sets background
class background():
    def __init__(self):
        self.background = None
        self.background = pygame.image.load(
            image_path + 'Menu2.png').convert()
        self.background = pygame.transform.scale(
            self.background, size)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

#function being used to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
bg = background()

# The main menu runs his own game loop and is called at the bottom of the screen.
def main_menu():
    while True:
        global click

        #background is set.
        screen.fill((0, 0, 0))
        bg.draw(screen)

        #these variables are being set to the x annd y cordinates of your mouse
        mx, my = pygame.mouse.get_pos()

        #Button images are loaded at this place in the code.
        img_button1 = pygame.image.load('images_thij/Game_button.png').convert_alpha()
        img_button2 = pygame.image.load('images_thij/Options_button.png').convert_alpha()
        img_button3 = pygame.image.load('images_thij/Quit_button.png').convert_alpha()

        # Is dit nodig? @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        img_button1 = pygame.transform.scale(img_button1, [buttonWidth, buttonhight])
        img_button2 = pygame.transform.scale(img_button2, [buttonWidth, buttonhight])
        img_button3 = pygame.transform.scale(img_button3, [buttonWidth, buttonhight])
    
        #For the buttons to work, we will need invicible rectangles. they are made at this place in the code.
        button_1 = pygame.Rect(
            screen_width / 3, buttonhight * 3, buttonWidth, buttonhight)
        button_2 = pygame.Rect(
            screen_width / 3, buttonhight * 5, buttonWidth, buttonhight)
        button_3 = pygame.Rect(
            screen_width / 3, buttonhight * 7, buttonWidth, buttonhight)
        
        #If the mouse collides with one of the rectangles created at line 70 and the mouse mouse is clicked at the same time, the program wil run the code beneath the if statements. 
        #In this instance there are three options: Running the game, opening the options menu and quiting the game.
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

        #The images are being blit on top of the invicible reectangles at this place.
        screen.blit(img_button1, [screen_width / 3, buttonhight * 3])
        screen.blit(img_button2, [screen_width / 3, buttonhight * 5])
        screen.blit(img_button3, [screen_width / 3, buttonhight * 7])

        click = False

        #The first event makes sure the game closes when the red cross is being pressed.
        #The second event registers if the mouse is being clicked. The click variable will be set to True.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

#The option menu is a close copy to the main menu. It has its own game loop and is being called by pressing the option menu button.
#To return to the menu, the while loop will be set to false.
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

# The whole program is started at this point
main_menu()
