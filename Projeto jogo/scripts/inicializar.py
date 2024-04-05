import pygame
from scripts.dados import *
from scripts.objetos import *

def startGame ():

    # Iniciar jogo
    pygame.init()
    # Pegar dimensões do display
    info = pygame.display.Info()
    dimensions["WIDTH"], dimensions["HEIGHT"] = info.current_w, info.current_h

    # # Criar tela de jogo
    # SCREEN = pygame.display.set_mode((dimensions["WIDTH"], dimensions["HEIGHT"]), pygame.FULLSCREEN)

    # Crie a tela de jogo sem a opção pygame.FULLSCREEN
    SCREEN = pygame.display.set_mode((dimensions["WIDTH"], dimensions["HEIGHT"]))

    # Ou, se você ainda deseja uma tela cheia, mas sem pygame.FULLSCREEN, pode maximizar a janela:
    pygame.display.toggle_fullscreen()

    pygame.display.set_caption(gameName)
    clock = pygame.time.Clock()
    tela = janela(SCREEN, clock)
    tela.SCREEN = SCREEN
    tela.clock = clock

    # Carregar a imagem do fundo
    fundo = backGround ()

    tela.elementosParaRenderizar['backGround'] = fundo
    tela.elementosParaRenderizar['mainCharacter'] = MainCaracter()
    all_sprites.add(tela.elementosParaRenderizar['mainCharacter'])
    mainCharacter.add(tela.elementosParaRenderizar['mainCharacter'])


    # Defina o tipo de evento para gerar obstáculos
    # GERAR_OBSTACULOS_EVENTO = pygame.USEREVENT + 1

    # Configure o temporizador para gerar o evento com o intervalo inicial
    # pygame.time.set_timer(GERAR_OBSTACULOS_EVENTO, velocidades['taxaDeGeracaoDeObstaculos'])

    # eventosTemporarios['gerarObstaculo'] = GERAR_OBSTACULOS_EVENTO

    # # Defina o tipo de evento para gerar obstáculos
    # GERAR_PODER_EVENTO = pygame.USEREVENT + 1

    # # Configure o temporizador para gerar o evento com o intervalo inicial
    # pygame.time.set_timer(GERAR_PODER_EVENTO, velocidades['taxaDeGeracaoDePowerUps'])

    # eventosTemporarios['gerarPowerUp'] = GERAR_PODER_EVENTO 
    return tela


