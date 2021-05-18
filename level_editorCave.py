import pygame
import pickle
from os import path


pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
tile_size = 20
cols = 40
margin = 100
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor Cave')


#load images
sun_img = pygame.image.load('Images3/sun.png')
sun_img = pygame.transform.scale(sun_img, (tile_size, tile_size))
bg_img = pygame.image.load('Images3/bg.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
dirt_img = pygame.image.load('Images3/dirt.png')
grass_img = pygame.image.load('Images3/grass.png')
waterblock_img = pygame.image.load('Images3/waterblock.png')
waterwave_img = pygame.image.load('Images3/waterwave.png')
platform_x_img = pygame.image.load('Images3/platform.png')
platform_y_img = pygame.image.load('Images3/platform.png')
lava_img = pygame.image.load('Images3/lava.png')
spikesR_img = pygame.image.load('Images3/spikes_right.png')
spikesL_img = pygame.image.load('Images3/spikes_left.png')
water_img = pygame.image.load('Images3/water.png')
coin_img = pygame.image.load('Images3/coin.png')
exit_img = pygame.image.load('Images3/tiles_door.png')
key_img = pygame.image.load('Images3/tiles_oldkey.png')
save_img = pygame.image.load('Images3/save_btn.png')
load_img = pygame.image.load('Images3/load_btn.png')


#define game variables
clicked = False
level_counter = 1

#define colours
white = (255, 255, 255)
green = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

#create empty tile list
world_data = []
for row in range(40):
	r = [0] * 40
	world_data.append(r)

#create boundary
for tile in range(0, 40):
	world_data[39][tile] = 2
	world_data[0][tile] = 1
	world_data[tile][0] = 1
	world_data[tile][39] = 1

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_grid():
	for c in range(41):
		#vertical lines
		pygame.draw.line(screen, white, (c * tile_size, 0), (c * tile_size, screen_height - margin))
		#horizontal lines
		pygame.draw.line(screen, white, (0, c * tile_size), (screen_width, c * tile_size))


def draw_world():
	for row in range(40):
		for col in range(40):
			if world_data[row][col] > 0:
				if world_data[row][col] == 1:
					#dirt blocks
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 2:
					#grass blocks
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 3:
					#waterblock blocks
					img = pygame.transform.scale(waterblock_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 4:
					#waterwave blocks
					img = pygame.transform.scale(waterwave_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))		
				if world_data[row][col] == 5:
					#horizontally moving platform
					img = pygame.transform.scale(platform_x_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 6:
					#vertically moving platform
					img = pygame.transform.scale(platform_y_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 7:
					#lava
					img = pygame.transform.scale(lava_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
				if world_data[row][col] == 8:
					#Spikes Right blocks
					img = pygame.transform.scale(spikesR_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))	
				if world_data[row][col] == 9:
					#Spikes Left blocks
					img = pygame.transform.scale(spikesL_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))		
				if world_data[row][col] == 10:
					#water
					img = pygame.transform.scale(water_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
				if world_data[row][col] == 11:
					#door
					img = pygame.transform.scale(exit_img, (tile_size, int(tile_size * 1.5)))
					screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))
				if world_data[row][col] == 12:
					#key
					img = pygame.transform.scale(key_img, (tile_size, int(tile_size * 1.1)))
					screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))	
				if world_data[row][col] == 13:
					#coins
					img = pygame.transform.scale(coin_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))	



class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action

#create load and save buttons
save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

#main game loop
run = True
while run:

	clock.tick(fps)

	#draw background
	screen.fill(green)
	screen.blit(bg_img, (0, 0))
	screen.blit(sun_img, (tile_size * 2, tile_size * 2))

	#load and save level
	if save_button.draw():
		#save level data
		pickle_out = open(f'level{level_counter}_data', 'wb')
		pickle.dump(world_data, pickle_out)
		pickle_out.close()
	if load_button.draw():
		#load in level data
		if path.exists(f'level{level_counter}_data'):
			pickle_in = open(f'level{level_counter}_data', 'rb')
			world_data = pickle.load(pickle_in)


	#show the grid and draw the level tiles
	draw_grid()
	draw_world()


	#text showing current level
	draw_text(f'Level: {level_counter}', font, white, tile_size, screen_height - 60)
	draw_text('Press UP or DOWN to change level', font, white, tile_size, screen_height - 40)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		#mouseclicks to change tiles
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = pos[0] // tile_size
			y = pos[1] // tile_size
			#check that the coordinates are within the tile area
			if x < 40 and y < 40:
				#update tile value
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 13:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 13
		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		#up and down key presses to change level number
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level_counter += 1
			elif event.key == pygame.K_DOWN and level_counter > 1:
				level_counter -= 1

	#update game display window
	pygame.display.update()

pygame.quit()
