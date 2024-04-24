import pygame
from scripts.dados import *
from scripts.objetos import *

def startGame():

    # Iniciar jogo
    pygame.init()

    # Iniciar sons
    pygame.mixer.init()

    # Pegar dimensões do display
    info = pygame.display.Info()
    dimensions["WIDTH"], dimensions["HEIGHT"] = info.current_w, info.current_h
    # Crie a tela de jogo
    SCREEN = pygame.display.set_mode((dimensions["WIDTH"], dimensions["HEIGHT"]))



    pygame.display.toggle_fullscreen()
    pygame.display.set_caption(gameName)
    clock = pygame.time.Clock()
    tela = janela(SCREEN, clock)
    tela.SCREEN = SCREEN
    tela.clock = clock

    # carregar imagens
    for imagem in imagens:
        imagens[imagem]['imagemPyGame'] = pygame.image.load(getEndereco(imagens[imagem]['diretorio'])).convert_alpha()
    # carregar imagens das skins
    for skin in skinsNave:
        skinsNave[skin]['imagemPyGame'] = pygame.image.load(getEndereco(skinsNave[skin]['diretorio'])).convert_alpha()


    # carregar imagem dos poderes
    for poder in poderes:
        imagens[poderes[poder]['image']]['imagemPyGame'] = pygame.image.load(getEndereco(poderes[poder]['imageName'])).convert_alpha()

    # carregar fontes
    for fonte in fontes:
        fontes[fonte]['fontePyGame'] = pygame.font.Font(getEndereco(fontes[fonte]['diretorio'], 'fontes'), fontes[fonte]['tamanho'])

    # carregar sons
    for som in sons:
        sons[som]['somPyGame'] = pygame.mixer.Sound(getEndereco(sons[som]['diretorio'], 'sounds'))

    return tela


