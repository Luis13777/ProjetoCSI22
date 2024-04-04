from scripts.dados import *

def aumentarDificuldade(tela):
    if tela.score%100 == 0 and tela.score != 0:
        tela.elementosParaRenderizar['mainCharacter'].speed *= 1.1
        tela.speed *= 1.01
        velocidades['obstaculoSpeed'] *= 1.1
        velocidades['taxaDeGeracaoDeObstaculos'] *= 0.9
        pygame.time.set_timer(eventosTemporarios['gerarObstaculo'], int(velocidades['taxaDeGeracaoDeObstaculos']))
        
   
