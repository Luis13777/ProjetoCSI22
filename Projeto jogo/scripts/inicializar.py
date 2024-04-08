import pygame
from scripts.dados import *
from scripts.objetos import *

def startGame():

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

    imagens['mainCharacter'] = pygame.image.load(getImagem(mainCharacterImage)).convert_alpha()
    imagens['backGroundImage'] = pygame.image.load(getImagem(backGroundImage)).convert_alpha()
    imagens['obstaculoImage'] = pygame.image.load(getImagem(obstaculoImage)).convert_alpha()
    imagens['tiroImage'] = pygame.image.load(getImagem(tiroImage)).convert_alpha()
    imagens['explosaoImage'] = pygame.image.load(getImagem(explosaoImage)).convert_alpha()
    imagens['vidaCheia'] = pygame.image.load(getImagem(vidaCheia)).convert_alpha()
    imagens['vidaVazia'] = pygame.image.load(getImagem(vidaVazia)).convert_alpha()
    imagens['boss'] = pygame.image.load(getImagem(boss)).convert_alpha()
    imagens['bossDamaged'] = pygame.image.load(getImagem(bossDamaged)).convert_alpha()
    imagens['bossVeryDamaged'] = pygame.image.load(getImagem(bossVeryDamaged)).convert_alpha()

    for poder in poderes:
        imagens[poderes[poder]['image']] = pygame.image.load(getImagem(poderes[poder]['imageName'])).convert_alpha()

    for fonte in fontes:
        fontes[fonte]['fontePyGame'] = pygame.font.Font(fontes[fonte]['diretorio'], fontes[fonte]['tamanho'])

    # imagens['powerUpTiro'] = pygame.image.load(getImagem(powerUpTiro)).convert_alpha()

    # Carregar a imagem do fundo
    fundo = backGround()

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


