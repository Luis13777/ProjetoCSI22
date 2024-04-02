import pygame
from scripts.dados import *

def renderBackground (tela):
    
    fundo = tela.elementosParaRenderizar['backGround']
    larguraDaImageRua = fundo.image.get_width()
    fundo.positionX -= tela.speed
    if fundo.positionX <= -larguraDaImageRua:
        fundo.positionX = 0
    
    # Desenhar os fundos na tela
    tela.SCREEN.blit(fundo.image, (fundo.positionX, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + larguraDaImageRua, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + 2*larguraDaImageRua, fundo.positionY))

    fundo.treePosition -= tela.speed*0.3
    if fundo.treePosition <= -dimensions['WIDTH']:
        fundo.treePosition = 0

    for i in range(fundo.numeroDeArvores*2):
        tela.SCREEN.blit(fundo.treeImage, (fundo.treePosition + dimensions['WIDTH']*(1/fundo.numeroDeArvores)*i, dimensions['HEIGHT']*0.3 - fundo.treeImage.get_height()))
