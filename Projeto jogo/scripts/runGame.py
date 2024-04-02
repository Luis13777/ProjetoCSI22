import pygame
from scripts.dados import *
from scripts.renderBackground import *
from scripts.renderObstaculos import *
from scripts.checkCollision import *


score = 0
def runGame (tela): 
    # Loop principal do jogo
    player = tela.elementosParaRenderizar['mainCharacter']
    running = True

    while running:
        tela.score += 1/FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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
        if tela.score > 0.5:
            tela.score = 0
            tela.speed += 1
            novoObstaculo(tela)
        if 'obstaculo' in tela.elementosParaRenderizar:
            renderObstaculos(tela, tela.score)
            checkCollision(tela)

        # Atualizar a tela
        pygame.display.flip()

        # Controlando a taxa de quadros
        tela.clock.tick(FPS)
        
    # Finalizar o Pygame
    pygame.quit()