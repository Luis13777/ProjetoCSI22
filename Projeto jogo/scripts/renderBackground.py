import pygame
from scripts.dados import *


def renderBackground(tela, velocidade=0):
    fundo = tela.elementosParaRenderizar['backGround']
    larguraDaImagemFundo = fundo.image.get_width()

    if velocidade == 0:
        fundo.positionX -= tela.speed
    else:
        fundo.positionX -= velocidade
        
    if fundo.positionX <= -larguraDaImagemFundo:
        fundo.positionX = 0
    
    # Desenhar os fundos na tela
    tela.SCREEN.blit(fundo.image, (fundo.positionX, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + larguraDaImagemFundo, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + 2*larguraDaImagemFundo, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + 3*larguraDaImagemFundo, fundo.positionY))


