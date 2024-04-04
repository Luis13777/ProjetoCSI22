from scripts.dados import *
from scripts.objetos import *
import random
import threading

def novoObstaculo(tela):
    novoObstaculo = Obstaculo()
    if 'obstaculo' in tela.elementosParaRenderizar:
        tela.elementosParaRenderizar['obstaculo'].append(novoObstaculo)
    else:
        tela.elementosParaRenderizar['obstaculo'] = [novoObstaculo]
    all_sprites.add(novoObstaculo)
    meteoros.add(novoObstaculo)

