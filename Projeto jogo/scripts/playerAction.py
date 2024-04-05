import pygame


def playerActions(player):
    # Verificando teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.moveUp()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.moveDown()
    if keys[pygame.K_SPACE]:
        player.shoot()
