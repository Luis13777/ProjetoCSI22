import pygame
from dados import *

def runGame (SCREEN, clock, caracters, bottomLimit, topLimit): 
    # Loop principal do jogo
    player = caracters['mainCaracter']
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Verificando teclas pressionadas
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and player.positionY > topLimit:
            player.moveUp()
        if keys[pygame.K_DOWN] and player.positionY < bottomLimit:
            player.moveDown()

        # Preenchendo a tela com a cor branca
        SCREEN.fill(WHITE)


        # Desenhando a imagem na tela
        SCREEN.blit(player.image, (player.positionX, player.positionY))
        
        
        # Atualizar a tela
        pygame.display.flip()

        # Controlando a taxa de quadros
        clock.tick(FPS)

    # Finalizar o Pygame
    pygame.quit()