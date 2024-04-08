import pygame
from scripts.dados import *
from scripts.objetos import *


def novoPowerUp(tela):
    novoPoder = PowerUp()
    if 'poder' in tela.elementosParaRenderizar:
        tela.elementosParaRenderizar['poder'].append(novoPoder)
    else:
        tela.elementosParaRenderizar['poder'] = [novoPoder]
    all_sprites.add(novoPoder)
    poderes_grupo.add(novoPoder)