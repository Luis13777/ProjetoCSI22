import pygame
from dados import *

class mainCaracter ():
    def __init__(self):
        self.positionX = 0
        self.positionY = 0
        self.speed = 10
        self.ImageLocation = 'image/bike.png'
        self.image = None
        self.topLimit = 0
        self.bottomLimit = 0

        # Carregar a imagem do personagem
        image = pygame.image.load(self.ImageLocation)
        originalImageWidth, originalImageHeight = image.get_size()
        finalImageWidth = dimensions["WIDTH"]*0.1
        finalImageHeight = originalImageHeight*finalImageWidth/originalImageWidth
        image = pygame.transform.scale(image, (finalImageWidth, finalImageHeight))

        self.image = image
        self.positionY = dimensions["HEIGHT"] // 2 - finalImageHeight/2
        self.bottomLimit = dimensions["HEIGHT"] - finalImageHeight

    def moveUp(self):
        if self.positionY > 0:
            self.positionY -= self.speed

    def moveDown(self):
        if self.positionY < self.bottomLimit:
            self.positionY += self.speed





class janela ():
    def __init__(self, SCREEN, clock):
        self.SCREEN = SCREEN
        self.clock = clock
        self.elementosParaRenderizar =  {}






class backGround ():
    def __init__(self, positionX, positionY, speed, image):
        self.positionX = positionX
        self.positionY = positionY
        self.speed = speed
        self.image = image

        originalImageWidth, originalImageHeight = self.image.get_size()
        finalImageHeight = dimensions["HEIGHT"]*0.7
        finalImageWidth = originalImageWidth*finalImageHeight/originalImageHeight
        self.image = pygame.transform.scale(self.image, (finalImageWidth, finalImageHeight))

        self.positionY = dimensions["HEIGHT"] - self.image.get_height()