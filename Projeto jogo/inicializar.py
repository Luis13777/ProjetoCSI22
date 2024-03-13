import pygame
from dados import *
from objetos import *

def startGame ():
    pygame.init()

    # Definindo as dimensões da tela
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo CSI22")

    clock = pygame.time.Clock()

    # Carregar a imagem
    image = pygame.image.load(imageLocation)
    originalImageWidth, originalImageHeight = image.get_size()

    finalImageWidth = WIDTH*0.1
    finalImageHeight = originalImageHeight*finalImageWidth/originalImageWidth

    image = pygame.transform.scale(image, (finalImageWidth, finalImageHeight))

    # Definindo as coordenadas iniciais do círculo
    x0 = 0
    y0 = HEIGHT // 2 - finalImageHeight/2

    bottomLimit = HEIGHT - finalImageHeight
    topLimit = 0

    player = mainCaracter(x0, y0, mainCaracterSpeed, image)

    caracters = {'mainCaracter': player}

    return SCREEN, clock, caracters, bottomLimit, topLimit


