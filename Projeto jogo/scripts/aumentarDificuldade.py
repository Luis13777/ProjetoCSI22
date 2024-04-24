from scripts.dados import *


def aumentarDificuldade(tela):

    # Aumenta a velocidade vertical do personagem
    if tela.scores['scoreParaAumentarVelocidade'] > velocidades['scoreParaAumentarVelocidade'] and tela.elementosParaRenderizar['mainCharacter'].speed < velocidades['maxMainCharacterSpeed']:
        tela.elementosParaRenderizar['mainCharacter'].speed *= 1.1
        tela.scores['scoreParaAumentarVelocidade'] = 1

    # Aumenta a velocidade do fundo
    if velocidades['janelaSpeed'] < velocidades['maxTelaSpeed']:
        velocidades['janelaSpeed'] *= 1.0001

    # Aumenta a velocidade dos obstaculos
    if tela.scores['scoreParaAumentarVelocidadeObstaculo'] > velocidades['scoreParaAumentarVelocidadeObstaculo'] and velocidades['obstaculoSpeed'] < velocidades['maxObstaculoSpeed']:
        velocidades['obstaculoSpeed'] *= 1.1
        tela.scores['scoreParaAumentarVelocidadeObstaculo'] = 1

    # Diminui a quantidade de pontos necessarios para gerar um obstaculo
    if tela.scores['scoreParaAumentarVelocidadeGeracaoObstaculo'] > velocidades['scoreParaAumentarVelocidadeGeracaoObstaculo'] and velocidades['pontosParaGerarObstaculo'] > velocidades['minPontosParaGerarObstaculo']:
        velocidades['pontosParaGerarObstaculo'] *= 0.9
        tela.scores['scoreParaAumentarVelocidadeGeracaoObstaculo'] = 1
        
   
