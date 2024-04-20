import pygame
from scripts.dados import *
from scripts.getImage import *
import random

class MainCaracter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = velocidades['mainCharacterSpeed']

        # self.image_location = getImagem(mainCharacterImage)
        # self.image = pygame.image.load(self.image_location).convert_alpha()
        self.image = imagens['mainCharacter']['imagemPyGame']
        original_image_width, original_image_height = self.image.get_size()
        final_image_width = dimensions["WIDTH"] * 0.05
        final_image_height = original_image_height * final_image_width / original_image_width
        self.image = pygame.transform.scale(self.image, (final_image_width, final_image_height))
        self.rect = self.image.get_rect()
        self.rect.x = dimensions["WIDTH"]*0.1
        self.rect.y = dimensions["HEIGHT"] // 2 - final_image_height / 2
        self.top_limit = dimensions["HEIGHT"] * proporcaoDoMenu
        self.bottom_limit = dimensions["HEIGHT"] - final_image_height
        self.last_shot = pygame.time.get_ticks()  # Armazena o momento do último tiro
        self.shoot_delay = 1000  # Delay em milissegundos entre os tiros
        self.tempoPerdeuVida = pygame.time.get_ticks()
        self.maxVidas = 3
        self.vidas = 3

        self.imageVidaCheia = imagens['vidaCheia']['imagemPyGame']
        # self.imageVidaCheia = pygame.image.load(getImagem(vidaCheia)).convert_alpha()

        original_image_width, original_image_height = self.imageVidaCheia.get_size()
        final_image_width = dimensions["WIDTH"] * 0.05
        final_image_height = original_image_height * final_image_width / original_image_width
        self.imageVidaCheia = pygame.transform.scale(self.imageVidaCheia, (final_image_width, final_image_height))

        self.imageVidaVazia = imagens['vidaVazia']['imagemPyGame']

        # self.imageVidaVazia = pygame.image.load(getImagem(vidaVazia)).convert_alpha()

        original_image_width, original_image_height = self.imageVidaVazia.get_size()
        final_image_width = dimensions["WIDTH"] * 0.05
        final_image_height = original_image_height * final_image_width / original_image_width
        self.imageVidaVazia = pygame.transform.scale(self.imageVidaVazia, (final_image_width, final_image_height))

        self.vidaDelay = 5000

    def moveUp(self):
        if self.rect.y > self.top_limit:
            self.rect.y -= self.speed

    def moveDown(self):
        if self.rect.y < self.bottom_limit:
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
            self.tempoPerdeuVida = pygame.time.get_ticks()
            if self.vidas == 0:
                sons['killPlayer']['somPyGame'].play()
            elif self.vidas == 1:
                sons['critical']['somPyGame'].play()
            elif self.vidas == 2:
                sons['warning']['somPyGame'].play()


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


class backGround():
    def __init__(self):
        self.positionX = 0
        self.positionY = 0
        self.image = imagens['backGroundImage']['imagemPyGame']


        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageHeight = dimensions["HEIGHT"]*proporcaoDoResto
        finalImageWidth = originalImageWidth*finalImageHeight/originalImageHeight
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))

        self.positionY = dimensions["HEIGHT"] - self.image.get_height()


class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = imagens['obstaculoImage']['imagemPyGame']

        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * random.uniform(0.05, 0.3)
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.rect = self.image.get_rect()
        self.rect.x = dimensions['WIDTH']
        self.rect.y = random.randint(int(dimensions['HEIGHT'] * proporcaoDoMenu), int(dimensions['HEIGHT'] - self.rect.height))
        self.speed = velocidades['obstaculoSpeed']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
        

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = imagens['tiroImage']['imagemPyGame']
        # self.image = pygame.image.load(getImagem(tiroImage)).convert_alpha()  
        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * 0.1
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.rect = self.image.get_rect()
        # self.rect.centerx = x + finalImageHeight/2
        # self.rect.centery = y
        self.rect.center = (x, y)
        self.speed = velocidades['tiro']

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > dimensions["WIDTH"]:  # Remova o tiro se ele sair da tela
            self.kill()
        

class Explosao(pygame.sprite.Sprite):
    def __init__(self, center, meteoro):
        super().__init__()

        self.image = imagens['explosaoImage']['imagemPyGame']
        # self.image = pygame.image.load(getImagem(explosaoImage)).convert_alpha()

        alturaFinal = meteoro[0].image.get_height()
        
        # width = self.image.get_width() * self.scale_factor
        # height = self.image.get_height() * self.scale_factor
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*alturaFinal/self.image.get_height(), alturaFinal))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.explosionMoment = pygame.time.get_ticks()
        self.explosiomTime = 100
        sons['killObject']['somPyGame'].play()

    def update(self):
        
        if pygame.time.get_ticks() - self.explosionMoment > self.explosiomTime:

            self.kill()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        listaDePoderes = list(poderes)
        novoPoder = listaDePoderes[random.randint(0, len(listaDePoderes) - 1)]

        self.image = imagens[poderes[novoPoder]['image']]['imagemPyGame']

        # self.image = pygame.image.load(getImagem(poderes[novoPoder]['image'])).convert_alpha()


        self.tipo = poderes[novoPoder]['tipo']
        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * 0.05
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.rect = self.image.get_rect()
        self.rect.x = dimensions['WIDTH']
        self.rect.y = random.randint(int(dimensions['HEIGHT'] * proporcaoDoMenu), int(dimensions['HEIGHT'] - self.rect.height))
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
        original_image_width, original_image_height = self.image.get_size()
        final_image_width = dimensions["WIDTH"] * 0.1
        final_image_height = original_image_height * final_image_width / original_image_width
        self.image = pygame.transform.scale(self.image, (final_image_width, final_image_height))
        self.top_limit = dimensions["HEIGHT"] * proporcaoDoMenu
        self.bottom_limit = dimensions["HEIGHT"]
        self.rect = self.image.get_rect()
        self.rect.left = dimensions["WIDTH"]
        self.rect.centery = dimensions["HEIGHT"] // 2
        self.last_shot = pygame.time.get_ticks()  # Armazena o momento do último tiro
        self.shoot_delay = 1000  # Delay em milissegundos entre os tiros
        self.tempoPerdeuVida = pygame.time.get_ticks()
        self.vidas = 3
        self.vidaDelay = 1000
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
            all_sprites.add(tiro)
            tirosInimigos.add(tiro)

    def perderVida(self):
        if pygame.time.get_ticks() - self.tempoPerdeuVida > self.vidaDelay:
            self.vidas -= 1
            self.tempoPerdeuVida = pygame.time.get_ticks()

        if self.vidas == 2:
            self.image = imagens['bossDamaged']['imagemPyGame']
            original_image_width, original_image_height = self.image.get_size()
            final_image_width = dimensions["WIDTH"] * 0.1
            final_image_height = original_image_height * final_image_width / original_image_width
            self.image = pygame.transform.scale(self.image, (final_image_width, final_image_height))

        if self.vidas == 1:
            self.image = imagens['bossVeryDamaged']['imagemPyGame']
            original_image_width, original_image_height = self.image.get_size()
            final_image_width = dimensions["WIDTH"] * 0.1
            final_image_height = original_image_height * final_image_width / original_image_width
            self.image = pygame.transform.scale(self.image, (final_image_width, final_image_height))

        if self.vidas <= 0:
            self.kill()

    def update(self):
        self.shoot()
        if self.rect.right > dimensions["WIDTH"]*0.9:  
            self.rect.x -= self.speed
        if self.subindo:
            self.moveUp()
            if self.rect.top <= self.top_limit*2:
                self.subindo = False
        else:
            self.moveDown()
            if self.rect.bottom >= self.bottom_limit - self.top_limit*2:
                self.subindo = True


class TiroInimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = imagens['tiroImage']['imagemPyGame']
        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * 0.1
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = velocidades['tiro']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:  
            self.kill()