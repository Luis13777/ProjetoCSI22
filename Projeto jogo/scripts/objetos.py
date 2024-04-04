import pygame
from scripts.dados import *
from scripts.getImage import getImagem
import random

class MainCaracter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = velocidades['mainCharacterSpeed']
        self.image_location = getImagem(mainCharacterImage)
        self.image = pygame.image.load(self.image_location).convert_alpha()
        original_image_width, original_image_height = self.image.get_size()
        final_image_width = dimensions["WIDTH"] * 0.1
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
        self.imageVidaCheia = pygame.image.load(getImagem(vidaCheia)).convert_alpha()

        original_image_width, original_image_height = self.imageVidaCheia.get_size()
        final_image_width = dimensions["WIDTH"] * 0.05
        final_image_height = original_image_height * final_image_width / original_image_width
        self.imageVidaCheia = pygame.transform.scale(self.imageVidaCheia, (final_image_width, final_image_height))

        self.imageVidaVazia = pygame.image.load(getImagem(vidaVazia)).convert_alpha()

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

    def perderVida(self):
        if pygame.time.get_ticks() - self.tempoPerdeuVida > self.vidaDelay:
            self.vidas -= 1
            self.tempoPerdeuVida = pygame.time.get_ticks()
class janela ():
    def __init__(self, SCREEN, clock):
        self.SCREEN = SCREEN
        self.clock = clock
        self.elementosParaRenderizar =  {}
        self.speed = velocidades['janelaSpeed']
        self.score = 0

class backGround ():
    def __init__(self):
        self.positionX = 0
        self.positionY = 0

        self.image = pygame.image.load(getImagem(backGroundImage))

        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageHeight = dimensions["HEIGHT"]*proporcaoDoResto
        finalImageWidth = originalImageWidth*finalImageHeight/originalImageHeight
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))

        self.positionY = dimensions["HEIGHT"] - self.image.get_height()




class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(getImagem(obstaculoImage)).convert_alpha()
        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * random.uniform(0.05, 0.3)
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.rect = self.image.get_rect()
        self.rect.x = dimensions['WIDTH']
        self.rect.y = random.randint(dimensions['HEIGHT'] * proporcaoDoMenu, dimensions['HEIGHT'] - self.rect.height)
        self.speed = velocidades['obstaculoSpeed']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
        

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(getImagem(tiroImage)).convert_alpha()  # Carrega a imagem do tiro
        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * 0.1
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.rect = self.image.get_rect()
        self.rect.centerx = x + finalImageHeight/2
        self.rect.centery = y
        self.rect.center = (x, y)
        self.speed = velocidades['tiro']

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > dimensions["WIDTH"]:  # Remova o tiro se ele sair da tela
            self.kill()
        

class Explosao(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = pygame.image.load(getImagem(explosaoImage)).convert_alpha()
        self.scale_factor = 0.1  # Fator de escala inicial
        width = self.image.get_width() * self.scale_factor
        height = self.image.get_height() * self.scale_factor
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.explosionMoment = pygame.time.get_ticks()
        self.explosiomTime = 100
   

    def update(self):
        
        if pygame.time.get_ticks() - self.explosionMoment > self.explosiomTime:
   
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        listaDePoderes = list(poderes)
        print(listaDePoderes)
        novoPoder = poderes[listaDePoderes[random.randint(0, len(listaDePoderes) - 1)]]

        self.image = pygame.image.load(getImagem(poderes[novoPoder])).convert_alpha()

        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * 0.05
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.rect = self.image.get_rect()
        self.rect.x = dimensions['WIDTH']
        self.rect.y = random.randint(dimensions['HEIGHT'] * proporcaoDoMenu, dimensions['HEIGHT'] - self.rect.height)
        self.speed = velocidades['powerUpSpeed']

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
        