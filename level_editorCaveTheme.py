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
pygame.display.set_caption('Level Editor Water')


#load images
sun_img = pygame.image.load('Images7/sun.png')
sun_img = pygame.transform.scale(sun_img, (tile_size, tile_size))
bg_img = pygame.image.load('Images8/bg_cave.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
dirt_img = pygame.image.load('Images7/dirt.png')
grass_img = pygame.image.load('Images7/grass.png')
waterblock_img = pygame.image.load('Images7/waterblock.png')
waterwave_img = pygame.image.load('Images7/waterwave.png')
platform_x_img = pygame.image.load('Images8/platform1.png')
platform_y_img = pygame.image.load('Images8/platform4.png')
lava_img = pygame.image.load('Images7/lava.png')
spikesR_img = pygame.image.load('Images7/spikes_right.png')
spikesL_img = pygame.image.load('Images7/spikes_left.png')
water_img = pygame.image.load('Images7/water.png')
coin_img = pygame.image.load('Images7/coin.png')
exit_img = pygame.image.load('Images7/tiles_door.png')
key_img = pygame.image.load('Images7/tiles_oldkey.png')
save_img = pygame.image.load('Images7/save_btn.png')
load_img = pygame.image.load('Images7/load_btn.png')

blokje1_linksboven_img = pygame.image.load('Images8/blokje1_linksboven.png')
blokje1_rechtsboven_img = pygame.image.load('Images8/blokje1_rechtsboven.png')
blokje1_linksonder_img = pygame.image.load('Images8/blokje1_linksonder.png')
blokje1_rechtsonder_img = pygame.image.load('Images8/blokje1_rechtsonder.png')
grond1_img = pygame.image.load('Images8/grond1.png')

platform1_links_img = pygame.image.load('Images8/platform1_links.png')
platform1_midden_img = pygame.image.load('Images8/platform1_midden.png')
platform1_rechts_img = pygame.image.load('Images8/platform1_rechts.png')


blokje2_linksboven_img = pygame.image.load('Images8/blokje2_linksboven.png')
blokje2_rechtsboven_img = pygame.image.load('Images8/blokje2_rechtsboven.png')
blokje2_linksonder_img = pygame.image.load('Images8/blokje1_linksonder.png')
blokje2_rechtsonder_img = pygame.image.load('Images8/blokje2_rechtsonder.png')
grond2_img = pygame.image.load('Images8/grond2.png')

platform2_links_img = pygame.image.load('Images8/platform2_links.png')
platform2_midden_img = pygame.image.load('Images8/platform2_midden.png')
platform2_rechts_img = pygame.image.load('Images8/platform2_rechts.png')


blokje3_linksboven_img = pygame.image.load('Images8/blokje3_linksboven.png')
blokje3_rechtsboven_img = pygame.image.load('Images8/blokje3_rechtsboven.png')
blokje3_linksonder_img = pygame.image.load('Images8/blokje3_linksonder.png')
blokje3_rechtsonder_img = pygame.image.load('Images8/blokje3_rechtsonder.png')
grond3_img = pygame.image.load('Images8/grond3.png')

platform3_links_img = pygame.image.load('Images8/platform3_links.png')
platform3_midden_img = pygame.image.load('Images8/platform3_midden.png')
platform3_rechts_img = pygame.image.load('Images8/platform3_rechts.png')

blokje4_linksboven_img = pygame.image.load('Images8/blokje4_linksboven.png')
blokje4_rechtsboven_img = pygame.image.load('Images8/blokje4_rechtsboven.png')
blokje4_linksonder_img = pygame.image.load('Images8/blokje4_linksonder.png')
blokje4_rechtsonder_img = pygame.image.load('Images8/blokje4_rechtsonder.png')
grond4_img = pygame.image.load('Images8/grond4.png')

platform4_links_img = pygame.image.load('Images8/platform4_links.png')
platform4_midden_img = pygame.image.load('Images8/platform4_midden.png')
platform4_rechts_img = pygame.image.load('Images8/platform4_rechts.png')

hout1_img = pygame.image.load('Images8/hout1.png')
hout2_img = pygame.image.load('Images8/hout2.png')
kar1_img = pygame.image.load('Images8/kar1.png')


spikes1_img = pygame.image.load('Images8/spikes1.png')
spikes2_img = pygame.image.load('Images8/spikes2.png')
spikes3_img = pygame.image.load('Images8/spikes3.png')




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
	world_data[39][tile] = 5
	world_data[0][tile] = 5
	world_data[tile][0] = 5
	world_data[tile][39] = 5

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
				
				#BLOKJE1
				if world_data[row][col] == 1:
					img = pygame.transform.scale(blokje1_linksboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 2:
					img = pygame.transform.scale(blokje1_rechtsboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 3:
					img = pygame.transform.scale(blokje1_linksonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 4:
					img = pygame.transform.scale(blokje1_rechtsonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 5:
					img = pygame.transform.scale(grond1_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))

				#BLOKJE2
				if world_data[row][col] == 6:
					img = pygame.transform.scale(blokje2_linksboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 7:
					img = pygame.transform.scale(blokje2_rechtsboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 8:
					img = pygame.transform.scale(blokje2_linksonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 9:
					img = pygame.transform.scale(blokje2_rechtsonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 10:
					img = pygame.transform.scale(grond2_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))

				#BLOKJE3
				if world_data[row][col] == 11:
					img = pygame.transform.scale(blokje3_linksboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 12:
					img = pygame.transform.scale(blokje3_rechtsboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 13:
					img = pygame.transform.scale(blokje3_linksonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 14:
					img = pygame.transform.scale(blokje3_rechtsonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 15:
					img = pygame.transform.scale(grond3_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				
				#BLOKJE4
				if world_data[row][col] == 16:
					img = pygame.transform.scale(blokje4_linksboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 17:
					img = pygame.transform.scale(blokje4_rechtsboven_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 18:
					img = pygame.transform.scale(blokje4_linksonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 19:
					img = pygame.transform.scale(blokje4_rechtsonder_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 20:
					img = pygame.transform.scale(grond4_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				
				#VERSIERING GROT
				if world_data[row][col] == 21:
					img = pygame.transform.scale(hout1_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 22:
					img = pygame.transform.scale(hout2_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 23:
					img = pygame.transform.scale(kar1_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 24:
					img = pygame.transform.scale(spikes1_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 25:
					img = pygame.transform.scale(spikes2_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 26:
					img = pygame.transform.scale(spikes3_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))



				if world_data[row][col] == 27:
					#waterwave blocks
					img = pygame.transform.scale(waterwave_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))		
				if world_data[row][col] == 28:
					#horizontally moving platform
					img = pygame.transform.scale(platform_x_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 29:
					#vertically moving platform
					img = pygame.transform.scale(platform_y_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 30:
					#lava
					img = pygame.transform.scale(lava_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
				if world_data[row][col] == 31:
					#Spikes Right blocks
					img = pygame.transform.scale(spikesR_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))	
				if world_data[row][col] == 32:
					#Spikes Left blocks
					img = pygame.transform.scale(spikesL_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))		
				if world_data[row][col] == 33:
					#water
					img = pygame.transform.scale(water_img, (tile_size, tile_size // 2))
					screen.blit(img, (col * tile_size, row * tile_size + (tile_size // 2)))
				if world_data[row][col] == 34:
					#door
					img = pygame.transform.scale(exit_img, (tile_size, int(tile_size * 1.5)))
					screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))
				if world_data[row][col] == 35:
					#key
					img = pygame.transform.scale(key_img, (tile_size, int(tile_size * 1.1)))
					screen.blit(img, (col * tile_size, row * tile_size - (tile_size // 2)))	
				if world_data[row][col] == 36:
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
					if world_data[y][x] > 36:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 36
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
