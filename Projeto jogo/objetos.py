class mainCaracter ():
    def __init__(self, x, y, speed, image):
        self.positionX = x
        self.positionY = y
        self.speed = speed
        self.image = image
        
    def moveUp(self):
        self.positionY -= self.speed

    def moveDown(self):
        self.positionY += self.speed
        
