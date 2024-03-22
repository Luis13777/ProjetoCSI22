import pygame
from dados import *
from objetos import *

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
    backgroundImage = pygame.image.load('./assets/image/rua.png')
    fundo = backGround (0, dimensions["HEIGHT"] - backgroundImage.get_height()/2, 5, backgroundImage)

    tela.elementosParaRenderizar['backGround'] = fundo
    tela.elementosParaRenderizar['mainCharacter'] = mainCaracter()

    return tela


