from scripts.dados import *

def aumentarDificuldade(tela):

    # Aumenta a velocidade vertical do personagem
    if tela.scoreParaAumentarVelocidade > velocidades['scoreParaAumentarVelocidade'] and tela.elementosParaRenderizar['mainCharacter'].speed < velocidades['maxMainCharacterSpeed']:
        tela.elementosParaRenderizar['mainCharacter'].speed *= 1.1
        tela.scoreParaAumentarVelocidade = 1

    # Aumenta a velocidade do fundo
    if tela.speed < velocidades['maxTelaSpeed']:
        tela.speed *= 1.0001

    # Aumenta a velocidade dos obstaculos
    if tela.scoreParaAumentarVelocidadeObstaculo > velocidades['scoreParaAumentarVelocidadeObstaculo'] and velocidades['obstaculoSpeed'] < velocidades['maxObstaculoSpeed']:
        velocidades['obstaculoSpeed'] *= 1.1
        tela.scoreParaAumentarVelocidadeObstaculo = 1

    # Diminui a quantidade de pontos necessarios para gerar um obstaculo
    if tela.scoreParaAumentarVelocidadeGeracaoObstaculo > velocidades['scoreParaAumentarVelocidadeGeracaoObstaculo'] and velocidades['pontosParaGerarObstaculo'] > velocidades['minPontosParaGerarObstaculo']:
        velocidades['pontosParaGerarObstaculo'] *= 0.9
        tela.scoreParaAumentarVelocidadeGeracaoObstaculo = 1
        
   
