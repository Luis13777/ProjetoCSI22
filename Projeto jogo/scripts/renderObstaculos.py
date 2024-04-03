from scripts.dados import *
from scripts.objetos import *
import random

def novoObstaculo(tela):
    novoObstaculo = Obstaculo()
    if 'obstaculo' in tela.elementosParaRenderizar:
        tela.elementosParaRenderizar['obstaculo'].append(novoObstaculo)
    else:
        tela.elementosParaRenderizar['obstaculo'] = [novoObstaculo]
    grupo_sprites.add(novoObstaculo)

def renderObstaculos(tela, score):
    for obstaculo in tela.elementosParaRenderizar['obstaculo']:
      
        tela.SCREEN.blit(obstaculo.image, (obstaculo.positionX, obstaculo.positionY))

        obstaculo.positionX -= tela.speed