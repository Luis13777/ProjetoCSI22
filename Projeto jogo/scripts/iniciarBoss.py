from scripts.dados import *
from scripts.objetos import *

def iniciarBoss(tela):
    inimigo = Boss()
    if 'boss' in tela.elementosParaRenderizar:
        tela.elementosParaRenderizar['boss'].append(inimigo)
    else:
        tela.elementosParaRenderizar['boss'] = [inimigo]
    all_sprites.add(inimigo)
    inimigosGroup.add(inimigo)

def acoesBoss(tela):
    tela.scoreParaGerarBoss = 1
    for boss in inimigosGroup:
        boss.update()
       