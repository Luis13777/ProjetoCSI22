import pygame
from scripts.dados import *
from scripts.funcoesAuxiliares import *
from scripts.telaDePause import *

def renderizarMenuTopo(tela):
    for i in range(tela.elementosParaRenderizar['mainCharacter'].vidas):
        tela.SCREEN.blit(tela.elementosParaRenderizar['mainCharacter'].imageVidaCheia, (i * tela.elementosParaRenderizar['mainCharacter'].imageVidaCheia.get_width(), 0))
    for i in range(tela.elementosParaRenderizar['mainCharacter'].maxVidas - tela.elementosParaRenderizar['mainCharacter'].vidas):
        tela.SCREEN.blit(tela.elementosParaRenderizar['mainCharacter'].imageVidaVazia, ((i + tela.elementosParaRenderizar['mainCharacter'].vidas) * tela.elementosParaRenderizar['mainCharacter'].imageVidaCheia.get_width(), 0))

    # # Renderizar o texto "Score:" na tela
    fonte = fontes['fonteScore']['fontePyGame']

    texto_score = fonte.render("Score: " + str(int(tela.scores['score'])), True, (255, 255, 255))
    largura_texto = texto_score.get_width()
    
    pauseButton = tela.elementosParaRenderizar['pauseButton']
    rectPauseButton = pauseButton.get_rect()
    rectPauseButton.right = dimensions['WIDTH']*0.99 
    rectPauseButton.top = dimensions['HEIGHT']*0.01

    # Desenhar o texto no topo e no meio da tela
    tela.SCREEN.blit(texto_score, ((dimensions['WIDTH'] - largura_texto) // 2, 0))

    tela.SCREEN.blit(pauseButton, rectPauseButton)


