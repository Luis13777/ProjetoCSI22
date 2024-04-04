import pygame

def playerActions(player):
    # Verificando teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.moveUp()
    if keys[pygame.K_DOWN]:
        player.moveDown()
    if keys[pygame.K_SPACE]:
        player.shoot()