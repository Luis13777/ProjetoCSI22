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
vidaCheia = "vidaCheia.png"
vidaVazia = "vidaVazia.png"

velocidades = {'mainCharacterSpeed': 20, 
               'janelaSpeed': 10,
               'obstaculoSpeed': 15,
               'tiro': 75,
               'powerUpSpeed': 7,
               'taxaDeGeracaoDeObstaculos': 2000,
               'taxaDeGeracaoDePowerUps': 200}



poderes = {
    'maisVida': vidaCheia,
    'tiroMaisRapido': 'tiro.png'
}

eventosTemporarios = {}

mainCharacter = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tiros = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
poderes_grupo = pygame.sprite.Group()