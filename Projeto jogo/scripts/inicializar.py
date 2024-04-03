import pygame
from scripts.dados import *
from scripts.objetos import *

def startGame ():
    # Iniciar jogo
    pygame.init()

    # Pegar dimensões do display
    info = pygame.display.Info()
    dimensions["WIDTH"], dimensions["HEIGHT"] = info.current_w, info.current_h

    # Criar tela de jogo
    SCREEN = pygame.display.set_mode((dimensions["WIDTH"], dimensions["HEIGHT"]), pygame.FULLSCREEN)

    pygame.display.set_caption(gameName)
    clock = pygame.time.Clock()
    tela = janela(SCREEN, clock)
    tela.SCREEN = SCREEN
    tela.clock = clock

    # Carregar a imagem do fundo
    fundo = backGround ()

    tela.elementosParaRenderizar['backGround'] = fundo
    tela.elementosParaRenderizar['mainCharacter'] = MainCaracter()
    grupo_sprites.add(tela.elementosParaRenderizar['mainCharacter'])


    return tela


