import pygame
from dados import *

def renderBackground (tela):
    
    fundo = tela.elementosParaRenderizar['backGround']
    larguraDaImageRua = fundo.image.get_width()
    fundo.positionX -= fundo.speed
    if fundo.positionX <= -larguraDaImageRua:
        fundo.positionX = 0
    

    # Desenhar os fundos na tela
    tela.SCREEN.blit(fundo.image, (fundo.positionX, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + larguraDaImageRua, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + 2*larguraDaImageRua, fundo.positionY))