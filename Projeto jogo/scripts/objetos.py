import pygame
from scripts.dados import *
from scripts.funcoesAuxiliares import *
import random

# classe personagem principal
class MainCaracter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = velocidades['mainCharacterSpeed']

        self.image = carregarImagemRedimencionada(imagens['mainCharacter']['imagemPyGame'], dimensions["WIDTH"] * 0.05)
        self.imageTransparente = carregarImagemRedimencionada(imagens['mainCharacterTransparente']['imagemPyGame'], dimensions["WIDTH"] * 0.05)
        self.imageNormal = self.image

        self.transparente = False

        self.rect = self.image.get_rect()
        self.rect.left = layout['posicaoDaNaveX']
        self.rect.centery = layout['posicaoDaNaveY']
        self.top_limit = layout['proporcaoDoMenu']
        self.bottom_limit = layout['limiteInferior']

        self.last_shot = pygame.time.get_ticks()  # Armazena o momento do último tiro
        self.tempoPerdeuVida = pygame.time.get_ticks()

        self.shoot_delay = velocidades['shootDelay']
        self.maxVidas = infos['maxVidas']
        self.vidas = self.maxVidas

        self.imageVidaCheia  = carregarImagemRedimencionada(imagens['vidaCheia']['imagemPyGame'], layout['larguraCoracao'])

        self.imageVidaVazia = carregarImagemRedimencionada(imagens['vidaVazia']['imagemPyGame'], layout['larguraCoracao'])

        self.vidaDelay = velocidades['scoreParaPerderOutraVida']
        self.delayPiscada = velocidades['delayPiscada']

    def moveUp(self):
        if self.rect.top >= self.top_limit:
            self.rect.y -= self.speed


    def moveDown(self):
        if self.rect.bottom <= self.bottom_limit:
            self.rect.y += self.speed


    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            tiro = Tiro(self.rect.right, self.rect.centery)
            all_sprites.add(tiro)
            tiros.add(tiro)
            sons['shot']['somPyGame'].play()

    def perderVida(self):
        if pygame.time.get_ticks() - self.tempoPerdeuVida > self.vidaDelay:
            self.vidas -= 1
            self.transparente = True
            self.tempoPerdeuVida = pygame.time.get_ticks()
            if self.vidas == 0:
                sons['killPlayer']['somPyGame'].play()
            elif self.vidas == 1:
                sons['critical']['somPyGame'].play()
            elif self.vidas == 2:
                sons['warning']['somPyGame'].play()

    def morto(self):
        if self.vidas <= 0:
            return True
        return False


    def update(self):
        if (pygame.time.get_ticks() - self.tempoPerdeuVida < self.vidaDelay):
            if (pygame.time.get_ticks() - self.tempoPerdeuVida) % self.delayPiscada < self.delayPiscada/2:
                if self.transparente:
                    self.transparente = False
                    self.image = self.imageNormal
                else:
                    self.transparente = True
                    self.image = self.imageTransparente
        else:
            if self.transparente:
                self.transparente = False
                self.image = self.imageNormal


class janela():
    def __init__(self, SCREEN, clock):
        self.SCREEN = SCREEN
        self.clock = clock
        self.elementosParaRenderizar =  {}
        self.speed = velocidades['janelaSpeed']
        self.speedMenu = velocidades['menuSpeed']
        self.score = 1
        self.scoreParaGerarObstaculo = 1
        self.scoreParaGerarPoder = 1
        self.scoreParaAumentarVelocidadeObstaculo = 1
        self.scoreParaAumentarVelocidade = 1
        self.scoreParaAumentarVelocidadeGeracaoObstaculo = 1
        self.scoreParaGerarBoss = 1
        self.scoreParaGerarElementoDeFundo = 1
        self.scoreParaGerarEstrela = 1

    def reiniciarTela(self):
        self.elementosParaRenderizar =  {}
        self.speed = velocidades['janelaSpeed']
        self.speedMenu = velocidades['menuSpeed']
        self.score = 1
        self.scoreParaGerarObstaculo = 1
        self.scoreParaGerarPoder = 1
        self.scoreParaAumentarVelocidadeObstaculo = 1
        self.scoreParaAumentarVelocidade = 1
        self.scoreParaAumentarVelocidadeGeracaoObstaculo = 1
        self.scoreParaGerarBoss = 1
        self.scoreParaGerarElementoDeFundo = 1
        self.scoreParaGerarEstrela = 1


class backGround():
    def __init__(self):
        self.positionX = 0

        self.image = carregarImagemRedimencionada(imagens['backGroundImage']['imagemPyGame'],  layout['proporcaoDoResto'], redimensionarPelaLargura=False)

        self.positionY = dimensions["HEIGHT"] - self.image.get_height()

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Sorteia um número entre 2 e 5
        numero_aleatorio = random.randint(1, 2)

        self.image = carregarImagemRedimencionada(imagens[f'obstaculoImage{numero_aleatorio}']['imagemPyGame'], dimensions["WIDTH"] * random.uniform(0.05, 0.3))
        
        self.rect = self.image.get_rect()
        self.rect.left = dimensions['WIDTH']
        self.rect.y = random.randint(int(layout['proporcaoDoMenu']), int(dimensions['HEIGHT'] - self.rect.height))
        self.speed = velocidades['obstaculoSpeed']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


class ElementoBackGround(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Sorteia um número entre 2 e 5
        numero_aleatorio = random.randint(1, 5)


        self.image = carregarImagemRedimencionada(imagens[f'backgorundElement{numero_aleatorio}']['imagemPyGame'], layout['larguraElementosDeFundo'])
        
        self.rect = self.image.get_rect()
        self.rect.left = dimensions['WIDTH']
        self.rect.y = random.randint(int(layout['proporcaoDoMenu']), int(dimensions['HEIGHT'] - self.rect.height))
        self.speed = velocidades['janelaSpeed']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()


class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Sorteia um número entre 2 e 5
        numero_aleatorio = random.randint(1, 2)


        self.image = carregarImagemRedimencionada(imagens[f'estrela{numero_aleatorio}']['imagemPyGame'], layout['larguraEstrela'])
        
        self.rect = self.image.get_rect()
        self.rect.left = dimensions['WIDTH']
        self.rect.y = random.randint(int(layout['proporcaoDoMenu']), int(dimensions['HEIGHT'] - self.rect.height))
        self.speed = velocidades['janelaSpeed']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
        
class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = carregarImagemRedimencionada(imagens['tiroImage']['imagemPyGame'], layout['larguraTiro'])

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = velocidades['tiro']

    def update(self):
        self.rect.x += self.speed
    
        if self.rect.left > dimensions["WIDTH"]:  # Remova o tiro se ele sair da tela
            self.kill()
        
class Explosao(pygame.sprite.Sprite):
    def __init__(self, center, meteoro):
        super().__init__()

        self.image = carregarImagemRedimencionada(imagens['explosaoImage']['imagemPyGame'], meteoro[0].image.get_height(), redimensionarPelaLargura=False)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.explosionMoment = pygame.time.get_ticks()
        self.explosiomTime = infos['tempoDeExplosao']
        sons['killObject']['somPyGame'].play()

    def update(self):
        if pygame.time.get_ticks() - self.explosionMoment > self.explosiomTime:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        listaDePoderes = list(poderes)
        novoPoder = listaDePoderes[random.randint(0, len(listaDePoderes) - 1)]

        self.image = carregarImagemRedimencionada(imagens[poderes[novoPoder]['image']]['imagemPyGame'], layout['larguraDoPoder'])

        self.tipo = poderes[novoPoder]['tipo']
        self.rect = self.image.get_rect()
        self.rect.x = dimensions['WIDTH']
        self.rect.y = random.randint(int(layout['proporcaoDoMenu']), int(dimensions['HEIGHT'] - self.rect.height))
        self.speed = velocidades['powerUpSpeed']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = velocidades['boss1Speed']
        self.image = imagens['boss']['imagemPyGame']

        self.image = carregarImagemRedimencionada(imagens['boss']['imagemPyGame'], layout['larguraDoBoss'])
        
        self.top_limit = layout['proporcaoDoMenu']
        self.bottom_limit = layout['fundo']

        self.rect = self.image.get_rect()
        self.rect.left = dimensions["WIDTH"]
        self.rect.centery = dimensions["HEIGHT"] / 2
        self.last_shot = pygame.time.get_ticks()  # Armazena o momento do último tiro
        self.shoot_delay = velocidades['tempoDeDelayTiroBoss']  # Delay em milissegundos entre os tiros
        self.tempoPerdeuVida = pygame.time.get_ticks()
        self.vidas = infos['maxVidasBoss']
        self.vidaDelay = velocidades['scoreParaPerderOutraVidaBoss']
        self.subindo = True

    def moveUp(self):
        if self.rect.y > self.top_limit:
            self.rect.y -= self.speed

    def moveDown(self):
        if self.rect.bottom < self.bottom_limit:
            self.rect.y += self.speed

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.x -= self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            tiro = TiroInimigo(self.rect.right, self.rect.centery)
            sons['shot']['somPyGame'].play()
            all_sprites.add(tiro)
            tirosInimigos.add(tiro)

    def perderVida(self):
        if pygame.time.get_ticks() - self.tempoPerdeuVida > self.vidaDelay:
            self.vidas -= 1
            self.tempoPerdeuVida = pygame.time.get_ticks()

        if self.vidas == 2:
            self.image = carregarImagemRedimencionada(imagens['bossDamaged']['imagemPyGame'], layout['larguraDoBoss'])
           
        if self.vidas == 1:
            self.image = carregarImagemRedimencionada(imagens['bossVeryDamaged']['imagemPyGame'], layout['larguraDoBoss'])

        if self.vidas <= 0:
            self.kill()

    def update(self):
        self.shoot()
        if self.rect.right > layout['posicaoXBoss']:  
            self.rect.x -= self.speed
        if self.subindo:
            self.moveUp()
            if self.rect.top <= layout['proporcaoDoMenu']:
                self.subindo = False
        else:
            self.moveDown()
            if self.rect.bottom >= layout['fundo']:
                self.subindo = True

class TiroInimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = carregarImagemRedimencionada(imagens['tiroImage']['imagemPyGame'], layout['larguraTiro'])

        
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = velocidades['tiro']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:  
            self.kill()