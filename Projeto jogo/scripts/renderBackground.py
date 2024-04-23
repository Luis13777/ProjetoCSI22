import pygame
from scripts.dados import *
from scripts.objetos import *


def renderBackground(tela, velocidade=0):
    fundo = tela.elementosParaRenderizar['backGround']
    larguraDaImagemFundo = fundo.image.get_width()

    if tela.scores['scoreParaGerarElementoDeFundo'] > velocidades['scoreParaGerarElementoDeFundo']:
        novoElementoBackGround = ElementoBackGround()
        all_sprites.add(novoElementoBackGround)
        elementosDefundo.add(novoElementoBackGround)
        tela.scores['scoreParaGerarElementoDeFundo'] = 1

    if tela.scores['scoreParaGerarEstrela'] > velocidades['scoreParaGerarEstrela']:
        novaEstrela = Estrela()
        all_sprites.add(novaEstrela)
        estrelas.add(novaEstrela)
        tela.scores['scoreParaGerarEstrela'] = 1
    

    if velocidade == 0:
        fundo.positionX -= velocidades['janelaSpeed']
    else:
        fundo.positionX -= velocidade
        
    if fundo.positionX <= -larguraDaImagemFundo:
        fundo.positionX = 0
    
    # Desenhar os fundos na tela
    tela.SCREEN.blit(fundo.image, (fundo.positionX, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + larguraDaImagemFundo, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + 2*larguraDaImagemFundo, fundo.positionY))
    tela.SCREEN.blit(fundo.image, (fundo.positionX + 3*larguraDaImagemFundo, fundo.positionY))


