import pygame

gameName = "Jogo CSI22"
dimensions = {"WIDTH": 1920,
"HEIGHT": 1080}

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL_CLARO = (173, 216, 230)

FPS = 144

mainCharacterImage = 'nave.png'
proporcaoDoMenu = 0.1
proporcaoDoResto = 1 - proporcaoDoMenu
backGroundImage = "space.png"
obstaculoImage = "meteoro.png"
tiroImage = "tiro.png"
explosaoImage = "explosao.png"



all_sprites = pygame.sprite.Group()
tiros = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
# explosoes = pygame.sprite.Group()