import pygame
 
import Constants
import Platforms

class Level():
    def __init__(self, player):
        self.doorLocation = []
        self.platform_list = None
        self.enemy_list = None
        self.door_list = None
        self.background = None
 
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.door_list = pygame.sprite.Group()
        self.player = player
 
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        screen.blit(self.background,(self.world_shift // 3,0))
 
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.door_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x
 
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
class Level_01(Level):
    def __init__(self, player):
 
        Level.__init__(self, player)

        self.background = pygame.image.load('Assets/img/background_Lvl1Poseidon.png').convert()
        self.background.set_colorkey(Constants.white)
        self.level_limit = -2500
 
        level = [ [Platforms.WATER_LEFT, 500, 500],
                  [Platforms.WATER_MIDDLE, 570, 500],
                  [Platforms.WATER_RIGHT, 640, 500],
                  [Platforms.WATER_LEFT, 800, 400],
                  [Platforms.WATER_MIDDLE, 870, 400],
                  [Platforms.WATER_RIGHT, 940, 400],
                  [Platforms.WATER_LEFT, 1000, 500],
                  [Platforms.WATER_MIDDLE, 1070, 500],
                  [Platforms.WATER_RIGHT, 1140, 500],
                  [Platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [Platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [Platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  [Platforms.STONE_PLATFORM_LEFT, 1830, 480],
                  [Platforms.STONE_PLATFORM_MIDDLE, 1900, 480],
                  [Platforms.STONE_PLATFORM_RIGHT, 1970, 480],
                  [Platforms.STONE_PLATFORM_LEFT, 2430, 480],
                  [Platforms.STONE_PLATFORM_MIDDLE, 2500, 480],
                  [Platforms.STONE_PLATFORM_RIGHT, 2570, 480],
                  ]
 
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = Platforms.MovingPlatform(Platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        doors = [ [Platforms.DOOR_UP, 2500, 345],
                  [Platforms.DOOR_DOWN, 2500, 410]
        ]

        door = Platforms.DOOR_UP
        for door_list in doors:
            self.door_list.add(door)
            self.doorLocation = b[0][1]            
 
class Level_02(Level):
    def __init__(self, player):
 
        Level.__init__(self, player)

        self.background = pygame.image.load('Assets/img/background_Lvl2Poseidon.png').convert()
        self.background.set_colorkey(Constants.white)
        self.level_limit = -2500
 
        level = [ [Platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [Platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [Platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [Platforms.WATER_LEFT, 800, 400],
                  [Platforms.WATER_MIDDLE, 870, 400],
                  [Platforms.WATER_RIGHT, 940, 400],
                  [Platforms.WATER_LEFT, 1000, 500],
                  [Platforms.WATER_MIDDLE, 1070, 500],
                  [Platforms.WATER_RIGHT, 1140, 500],
                  [Platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [Platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [Platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
 
        for platform in level:
            block = Platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            if platform[0] == Platforms.DOOR_UP or platform[0] == Platforms.DOOR_DOWN:
                a=(platform[1])
                self.doorLocation.append(a)
 
        block = Platforms.MovingPlatform(Platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_03(Level):
    pass
class Level_04(Level):
    pass
