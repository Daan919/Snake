import pygame
import pickle
from os import path


pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
tile_size = 20
cols = 40
margin = 100
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor Water')


ImgPath = "Images7/"

sun_img = pygame.image.load(ImgPath + 'sun.png')
sun_img = pygame.transform.scale(sun_img, (tile_size, tile_size))
bg_img = pygame.image.load(ImgPath + 'background.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))

img_dirt = pygame.image.load(ImgPath + 'dirt.png')
img_grass = pygame.image.load(ImgPath + 'grass.png')
img_static_platform_left = pygame.image.load(
    ImgPath + 'static_platform_left.png')
img_static_platform_mid = pygame.image.load(
    ImgPath + 'static_platform_mid.png')
img_static_platform_right = pygame.image.load(
    ImgPath + 'static_platform_right.png')
img_moving_platform = pygame.image.load(ImgPath + 'moving_platform.png')
img_moving_platform = pygame.image.load(ImgPath + 'moving_platform.png')
img_water = pygame.image.load(ImgPath + 'water.png')
img_lava = pygame.image.load(ImgPath + 'lava.png')
img_spike_right = pygame.image.load(ImgPath + 'spike_right.png')
img_spike_left = pygame.image.load(ImgPath + 'spike_left.png')
img_spike_up = pygame.image.load(ImgPath + 'spike_right.png')
img_spike_down = pygame.image.load(ImgPath + 'spike_right.png')
img_key = pygame.image.load(ImgPath + 'key.png')
img_door = pygame.image.load(ImgPath + 'door.png')
img_coin = pygame.image.load(ImgPath + 'Coin.png')
img_enemy = pygame.image.load(ImgPath + 'coin.png')
img_deco_block_1 = pygame.image.load(ImgPath + 'deco_block_1.png')
img_deco_block_2 = pygame.image.load(ImgPath + 'deco_block_2.png')
img_deco_block_3 = pygame.image.load(ImgPath + 'deco_block_3.png')
img_deco_block_4 = pygame.image.load(ImgPath + 'deco_block_4.png')
img_deco_block_5 = pygame.image.load(ImgPath + 'deco_block_5.png')
img_deco_block_6 = pygame.image.load(ImgPath + 'deco_block_6.png')
img_deco_block_7 = pygame.image.load(ImgPath + 'deco_block_7.png')
img_deco_block_8 = pygame.image.load(ImgPath + 'deco_block_8.png')
img_deco_block_9 = pygame.image.load(ImgPath + 'deco_block_9.png')
img_decoratie_1 = pygame.image.load(ImgPath + 'decoratie_1.png')
img_decoratie_2 = pygame.image.load(ImgPath + 'decoratie_2.png')
# img_decoratie_3 = pygame.image.load(ImgPath + 'decoratie_3.png')
# img_decoratie_4 = pygame.image.load(ImgPath + 'decoratie_4.png')
# img_decoratie_5 = pygame.image.load(ImgPath + 'decoratie_5.png')
# img_decoratie_6 = pygame.image.load(ImgPath + 'decoratie_6.png')
# img_decoratie_7 = pygame.image.load(ImgPath + 'decoratie_7.png')
# img_decoratie_8 = pygame.image.load(ImgPath + 'decoratie_8.png')
# img_decoratie_9 = pygame.image.load(ImgPath + 'decoratie_9.png')
# img_decoratie_10 = pygame.image.load(ImgPath + 'decoratie_10.png')

save_img = pygame.image.load('Images2/save_btn.png')
load_img = pygame.image.load('Images2/load_btn.png')

# define game variables
clicked = False
level_counter = 1

# define colours
white = (255, 255, 255)
green = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

# create empty tile list
world_data = []
for row in range(40):
    r = [0] * 40
    world_data.append(r)

# create boundary
for tile in range(0, 40):
    world_data[39][tile] = 20
    world_data[0][tile] = 1
    world_data[tile][0] = 1
    world_data[tile][39] = 1

# function for outputting text onto the screen


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_grid():
    for c in range(41):
        # vertical lines
        pygame.draw.line(screen, white, (c * tile_size, 0),
                         (c * tile_size, screen_height - margin))
        # horizontal lines
        pygame.draw.line(screen, white, (0, c * tile_size),
                         (screen_width, c * tile_size))


def draw_world():
    for row in range(40):
        for col in range(40):
            if world_data[row][col] > 0:

                # Standaart blockje
                if world_data[row][col] == 1:
                    img = pygame.transform.scale(
                        img_dirt, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 2:
                    img = pygame.transform.scale(
                        img_grass, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 3:
                    img = pygame.transform.scale(
                        img_static_platform_left, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 4:
                    img = pygame.transform.scale(
                        img_static_platform_mid, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 5:
                    img = pygame.transform.scale(
                        img_static_platform_right, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 6:
                    img = pygame.transform.scale(
                        img_moving_platform, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 7:
                    img = pygame.transform.scale(
                        img_moving_platform, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))

                    # interactieve blockjes
                if world_data[row][col] == 8:
                    img = pygame.transform.scale(
                        img_water, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 9:
                    img = pygame.transform.scale(
                        img_lava, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 10:
                    img = pygame.transform.scale(
                        img_spike_right, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 11:
                    img = pygame.transform.scale(
                        img_spike_left, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 12:
                    img = pygame.transform.scale(
                        img_spike_up, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 13:
                    img = pygame.transform.scale(
                        img_spike_down, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 14:
                    img = pygame.transform.scale(
                        img_key, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 15:
                    img = pygame.transform.scale(
                        img_door, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 16:
                    img = pygame.transform.scale(
                        img_coin, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 17:
                    img = pygame.transform.scale(
                        img_enemy, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                    # Deco block
                if world_data[row][col] == 18:
                    img = pygame.transform.scale(
                        img_deco_block_1, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 19:
                    img = pygame.transform.scale(
                        img_deco_block_2, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 20:
                    img = pygame.transform.scale(
                        img_deco_block_3, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 21:
                    img = pygame.transform.scale(
                        img_deco_block_4, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 22:
                    img = pygame.transform.scale(
                        img_deco_block_5, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 23:
                    img = pygame.transform.scale(
                        img_deco_block_6, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 24:
                    img = pygame.transform.scale(
                        img_deco_block_7, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 25:
                    img = pygame.transform.scale(
                        img_deco_block_8, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 26:
                    img = pygame.transform.scale(
                        img_deco_block_9, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))

                    # Decoratie block
                if world_data[row][col] == 27:
                    img = pygame.transform.scale(
                        img_decoratie_1, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 28:
                    img = pygame.transform.scale(
                        img_decoratie_2, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 29:
                    img = pygame.transform.scale(
                        img_decoratie_3, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 30:
                    img = pygame.transform.scale(
                        img_decoratie_4, (tile_size, tile_size // 2))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 31:
                    img = pygame.transform.scale(
                        img_decoratie_5, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 32:
                    img = pygame.transform.scale(
                        img_decoratie_6, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 33:
                    img = pygame.transform.scale(
                        img_decoratie_7, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 34:
                    img = pygame.transform.scale(
                        img_decoratie_8, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 35:
                    img = pygame.transform.scale(
                        img_decoratie_9, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))
                if world_data[row][col] == 36:
                    img = pygame.transform.scale(
                        img_decoratie_10, (tile_size, tile_size))
                    screen.blit(img, (col * tile_size, row * tile_size))


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


# create load and save buttons
save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

# main game loop
run = True
while run:

    clock.tick(fps)

    # draw background
    screen.fill(green)
    screen.blit(bg_img, (0, 0))

    # load and save level
    if save_button.draw():
        # save level data
        pickle_out = open(f'level{level_counter}_data', 'wb')
        pickle.dump(world_data, pickle_out)
        pickle_out.close()
    if load_button.draw():
        # load in level data
        if path.exists(f'level{level_counter}_data'):
            pickle_in = open(f'level{level_counter}_data', 'rb')
            world_data = pickle.load(pickle_in)

    # show the grid and draw the level tiles
    draw_grid()
    draw_world()

    # text showing current level
    draw_text(f'Level: {level_counter}', font,
              white, tile_size, screen_height - 60)
    draw_text('Press UP or DOWN to change level', font,
              white, tile_size, screen_height - 40)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // tile_size
            y = pos[1] // tile_size
            # check that the coordinates are within the tile area
            if x < 40 and y < 40:
                # update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] += 1
                    if world_data[y][x] > 36:
                        world_data[y][x] = 0
                elif pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] -= 1
                    if world_data[y][x] < 0:
                        world_data[y][x] = 36
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        # up and down key presses to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level_counter += 1
            elif event.key == pygame.K_DOWN and level_counter > 1:
                level_counter -= 1

    # update game display window
    pygame.display.update()

pygame.quit()
