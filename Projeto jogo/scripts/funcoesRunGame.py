import pygame
from scripts.dados import *
from scripts.renderObstaculos import *
from scripts.poderes import *
from scripts.iniciarBoss import *


def aumentarScore(tela):

    for score in tela.scores:
        tela.scores[score] += 1



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
    if tela.scores['scoreParaGerarObstaculo'] > velocidades['pontosParaGerarObstaculo']:
        novoObstaculo(tela)
        tela.scores['scoreParaGerarObstaculo'] = 1
    if tela.scores['scoreParaGerarPoder'] > velocidades['pontosParaGerarPoder']:
        novoPowerUp(tela)
        tela.scores['scoreParaGerarPoder'] = 1
    if tela.scores['scoreParaGerarBoss'] > velocidades['scoreParaGerarBoss']:
        iniciarBoss(tela)
        tela.scores['scoreParaGerarBoss'] = 1
    if inimigosGroup:
        acoesBoss(tela)
