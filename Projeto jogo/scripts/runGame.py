import pygame
from scripts.dados import *
from scripts.renderBackground import *
from scripts.renderObstaculos import *
from scripts.checkCollision import *
from scripts.playerAction import *
from scripts.renderizarMenuTopo import *
from scripts.aumentarDificuldade import *
from scripts.poderes import *
from scripts.iniciarBoss import *


def runGame(tela):
    # Loop principal do jogo
    player = tela.elementosParaRenderizar['mainCharacter']
    running = True

    while running:

        tela.score += 1
        tela.scoreParaGerarObstaculo += 1
        tela.scoreParaAumentarVelocidade += 1
        tela.scoreParaAumentarVelocidadeObstaculo += 1
        tela.scoreParaGerarPoder += 1
        tela.scoreParaAumentarVelocidadeGeracaoObstaculo += 1
        tela.scoreParaGerarBoss += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Preenchendo a tela com a cor branca
        tela.SCREEN.fill(BLACK)

        renderBackground(tela)
        playerActions(player)

        if tela.scoreParaGerarObstaculo > velocidades['pontosParaGerarObstaculo']:
            novoObstaculo(tela)
            tela.scoreParaGerarObstaculo = 1
        if tela.scoreParaGerarPoder > velocidades['pontosParaGerarPoder']:
            novoPowerUp(tela)
            tela.scoreParaGerarPoder = 1
        if tela.scoreParaGerarBoss > velocidades['scoreParaGerarBoss']:
            iniciarBoss(tela)
            tela.scoreParaGerarBoss = 1
        if inimigosGroup:
            acoesBoss(tela)

        checkCollision(tela)
        renderizarMenuTopo(tela)
        aumentarDificuldade(tela)
        # Atualize a posição dos sprites

        all_sprites.update()

        # Renderize os sprites na tela
        all_sprites.draw(tela.SCREEN)

        # Atualizar a tela
        pygame.display.flip()
        
        # Controlando a taxa de quadros
        tela.clock.tick(60)
        
    # Finalizar o Pygame
    pygame.quit()
