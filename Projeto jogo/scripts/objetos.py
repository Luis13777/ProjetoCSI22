import pygame
from scripts.dados import *
from scripts.getImage import getImagem
import random

class mainCaracter ():
    def __init__(self):
        self.positionX = 0
        self.positionY = 0
        self.speed = 15
        self.ImageLocation = getImagem(mainCharacterImage)
        self.image = None
        self.topLimit = 0

        # Carregar a imagem do personagem
        image = pygame.image.load(self.ImageLocation)
        originalImageWidth, originalImageHeight = image.get_size()
        finalImageWidth = dimensions["WIDTH"]*0.1
        finalImageHeight = originalImageHeight*finalImageWidth/originalImageWidth
        image = pygame.transform.scale(image, (finalImageWidth, finalImageHeight))

        self.image = image
        self.positionY = dimensions["HEIGHT"] // 2 - finalImageHeight/2
        self.bottomLimit = dimensions["HEIGHT"] - finalImageHeight
        self.topLimit = dimensions["HEIGHT"]*0.3

    def moveUp(self):
        if self.positionY > self.topLimit:
            self.positionY -= self.speed

    def moveDown(self):
        if self.positionY < self.bottomLimit:
            self.positionY += self.speed

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
        finalImageHeight = dimensions["HEIGHT"]*proporcaoDoResto
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

class obstaculo ():
    def __init__(self):
        self.positionX = dimensions['WIDTH']
        self.image = pygame.image.load(getImagem(obstaculoImage))
        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageWidth = dimensions["WIDTH"]*0.1
        finalImageHeight = originalImageHeight*finalImageWidth/originalImageWidth
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))
        self.positionY = random.uniform(dimensions['HEIGHT']*0.3, dimensions['HEIGHT'] - self.image.get_height())



