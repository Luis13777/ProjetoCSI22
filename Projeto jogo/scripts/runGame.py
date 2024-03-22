import pygame
from dados import *
from renderBackground import *

def runGame (tela): 
    # Loop principal do jogo
    player = tela.elementosParaRenderizar['mainCharacter']
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Verificando teclas pressionadas
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and player.positionY > 0:
            player.moveUp()
        if keys[pygame.K_DOWN] and player.positionY < player.image.get_height():
            player.moveDown()

        # Preenchendo a tela com a cor branca
        tela.SCREEN.fill(AZUL_CLARO)
        renderBackground(tela)

        # Verificando teclas pressionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.moveUp()
        if keys[pygame.K_DOWN]:
            player.moveDown()

        # Desenhando a imagem na tela
        tela.SCREEN.blit(player.image, (player.positionX, player.positionY))
        
        
        # Atualizar a tela
        pygame.display.flip()

        # Controlando a taxa de quadros
        tela.clock.tick(FPS)

    # Finalizar o Pygame
    pygame.quit()