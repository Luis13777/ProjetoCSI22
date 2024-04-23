import pygame
from scripts.dados import *
from scripts.renderBackground import *
# from scripts.renderObstaculos import *
from scripts.checkCollision import *
from scripts.funcoesRunGame import *
from scripts.renderizarMenuTopo import *
from scripts.aumentarDificuldade import *
# from scripts.poderes import *
# from scripts.iniciarBoss import *
from scripts.finalizarJogo import *





def runGame(tela):
    player = tela.elementosParaRenderizar['mainCharacter']
    
    running = True

    # Loop principal do jogo
    while running:

        aumentarScore(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Preenchendo a tela com a cor branca
        tela.SCREEN.fill(BLACK)

        renderBackground(tela)
        playerActions(player)

        eventosJogo(tela)

        checkCollision(tela)
        renderizarMenuTopo(tela)
        aumentarDificuldade(tela)
        
        # Atualize a posição dos sprites

        all_sprites.update()

        estrelas.draw(tela.SCREEN)
        elementosDefundo.draw(tela.SCREEN)
        poderes_grupo.draw(tela.SCREEN)
        inimigosGroup.draw(tela.SCREEN)
        meteoros.draw(tela.SCREEN)
        tirosInimigos.draw(tela.SCREEN)
        tiros.draw(tela.SCREEN)
        mainCharacter.draw(tela.SCREEN)
        explosaoGroup.draw(tela.SCREEN)
        # Renderize os sprites na tela
        # all_sprites.draw(tela.SCREEN)

        # Atualizar a tela
        pygame.display.flip()
        
        # Controlando a taxa de quadros
        tela.clock.tick(60)

        if player.morto():
            gameOver(tela)
            finalizarJogo(tela)
            return
        
    # Finalizar o Pygame
    pygame.quit()
