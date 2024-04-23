import pygame
from scripts.dados import *
from scripts.renderObstaculos import *
from scripts.poderes import *
from scripts.iniciarBoss import *


def aumentarScore(tela):
    tela.score += 1
    tela.scoreParaGerarObstaculo += 1
    tela.scoreParaAumentarVelocidade += 1
    tela.scoreParaAumentarVelocidadeObstaculo += 1
    tela.scoreParaGerarPoder += 1
    tela.scoreParaAumentarVelocidadeGeracaoObstaculo += 1
    tela.scoreParaGerarBoss += 1
    tela.scoreParaGerarElementoDeFundo += 1
    tela.scoreParaGerarEstrela += 1

def playerActions(player):
    # Verificando teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.moveUp()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.moveDown()
    if keys[pygame.K_SPACE]:
        player.shoot()

def eventosJogo(tela):
    if tela.scoreParaGerarObstaculo > velocidades['pontosParaGerarObstaculo']:
        novoObstaculo(tela)
        tela.scoreParaGerarObstaculo = 1
    if tela.scoreParaGerarPoder > velocidades['pontosParaGerarPoder']:
        novoPowerUp(tela)
        tela.scoreParaGerarPoder = 1
    if tela.scoreParaGerarBoss > velocidades['scoreParaGerarBoss']:
        iniciarBoss(tela)
        tela.scoreParaGerarBoss = 1
    if inimigosGroup:
        acoesBoss(tela)
