import pygame
import Constants
import Levels

from player import Player

def main(): 
    pygame.init()
    size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("THE ARES GAME")
 
    player = Player()
 
    level_list = []
    level_list.append(Levels.Level_01(player))
    level_list.append(Levels.Level_02(player))
 
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 340
    player.rect.y = Constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                    
        screen.fill((255,255,255))
        active_sprite_list.update()
        current_level.update()
 
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)
  
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
 
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
 
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        pygame.display.flip()
        clock.tick(60)

 
    pygame.quit()


if __name__ == "__main__":
    main()

