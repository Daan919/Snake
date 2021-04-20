def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])

    pygame.display.set_caption("De game van Daan")
    # create player
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []
