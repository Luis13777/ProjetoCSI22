import pygame
from scripts.dados import *

def renderizarMenuTopo(tela):
    for i in range(tela.elementosParaRenderizar['mainCharacter'].vidas):
        tela.SCREEN.blit(tela.elementosParaRenderizar['mainCharacter'].imageVidaCheia, (i * tela.elementosParaRenderizar['mainCharacter'].imageVidaCheia.get_width(), 0))
    for i in range(tela.elementosParaRenderizar['mainCharacter'].maxVidas - tela.elementosParaRenderizar['mainCharacter'].vidas):
        tela.SCREEN.blit(tela.elementosParaRenderizar['mainCharacter'].imageVidaVazia, ((i + tela.elementosParaRenderizar['mainCharacter'].vidas) * tela.elementosParaRenderizar['mainCharacter'].imageVidaCheia.get_width(), 0))

    # # Renderizar o texto "Score:" na tela
    fonte = fontes['fonteScore']['fontePyGame']

    texto_score = fonte.render("Score: " + str(int(tela.score)), True, (255, 255, 255))
    largura_texto = texto_score.get_width()
    altura_texto = texto_score.get_height()
    
    # Desenhar o texto no topo e no meio da tela
    tela.SCREEN.blit(texto_score, ((dimensions['WIDTH'] - largura_texto) // 2, 0))