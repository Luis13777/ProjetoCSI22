import pygame
from scripts.dados import *
from scripts.getImage import getImagem
import random

class MainCaracter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 15
        self.image_location = getImagem(mainCharacterImage)
        self.image = pygame.image.load(self.image_location).convert_alpha()
        original_image_width, original_image_height = self.image.get_size()
        final_image_width = dimensions["WIDTH"] * 0.1
        final_image_height = original_image_height * final_image_width / original_image_width
        self.image = pygame.transform.scale(self.image, (final_image_width, final_image_height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = dimensions["HEIGHT"] // 2 - final_image_height / 2
        self.top_limit = dimensions["HEIGHT"] * 0.3
        self.bottom_limit = dimensions["HEIGHT"] - final_image_height

    def moveUp(self):
        if self.rect.y > self.top_limit:
            self.rect.y -= self.speed

    def moveDown(self):
        if self.rect.y < self.bottom_limit:
            self.rect.y += self.speed



class janela ():
    def __init__(self, SCREEN, clock):
        self.SCREEN = SCREEN
        self.clock = clock
        self.elementosParaRenderizar =  {}
        self.speed = 15
        self.score = 0

class backGround ():
    def __init__(self):
        self.positionX = 0
        self.positionY = 0

        self.image = pygame.image.load(getImagem(backGroundImage))

        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageHeight = dimensions["HEIGHT"]*0.7
        finalImageWidth = originalImageWidth*finalImageHeight/originalImageHeight
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))

        self.positionY = dimensions["HEIGHT"] - self.image.get_height()

        self.treeImage = pygame.image.load(getImagem("tree.png"))
        originalTreeWidth, originalTreeHeight = self.treeImage.get_size()
        finalTreeHeight = dimensions["HEIGHT"]*0.2
        finalTreeWidth = originalTreeWidth*finalTreeHeight/originalTreeHeight
        self.treeImage = pygame.transform.scale(self.treeImage, (finalTreeWidth, finalTreeHeight))

        self.treePosition = 0
        self.numeroDeArvores = 4



class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(getImagem(obstaculoImage)).convert_alpha()
        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"] * 0.1
        finalImageHeight = originalImageHeight * finalImageWidth / originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.rect = self.image.get_rect()
        self.rect.x = dimensions['WIDTH']
        self.rect.y = random.randint(dimensions['HEIGHT'] * 0.3, dimensions['HEIGHT'] - self.rect.height)
        self.speed = 15

    def update(self):
        self.rect.x -= self.speed

