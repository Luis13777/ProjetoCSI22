import pygame
from scripts.getImage import getImagem

gameName = "Jogo CSI22"
dimensions = {"WIDTH": 1920,
"HEIGHT": 1080}

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL_CLARO = (173, 216, 230)

FPS = 144

proporcaoDoMenu = 0.1
proporcaoDoResto = 1 - proporcaoDoMenu

mainCharacterImage = 'nave.png'
backGroundImage = "space.png"
obstaculoImage = "meteoro.png"
tiroImage = "tiro.png"
explosaoImage = "explosao.png"
vidaCheia = "vidaCheia.png"
vidaVazia = "vidaVazia.png"
powerUpTiro = "poderTiro.png"
powerUpVida = "vidaCheia.png"

imagens ={}


arquivoFonte = 'assets/fontes/ARCADE_N.TTF'  
tamanho_fonte = 36



fontes = {'fonteScore': {'diretorio': 'assets/fontes/ARCADE_N.TTF', 'tamanho': 36, 'fontePyGame': ''}}


velocidades = {'mainCharacterSpeed': 10, 
               'janelaSpeed': 10,
               'obstaculoSpeed': 15,
               'tiro': 75,
               'powerUpSpeed': 7,
               'pontosParaGerarObstaculo': 100,
               'pontosParaGerarPoder': 500,
               'maxMainCharacterSpeed': 30,
               'maxTelaSpeed': 100,
               'maxObstaculoSpeed': 75,
               'minPontosParaGerarObstaculo': 9,
               'scoreParaAumentarVelocidade': 500,
               'scoreParaAumentarVelocidadeObstaculo': 500,
               'scoreParaAumentarVelocidadeGeracaoObstaculo': 400,}



poderes = {
    'maisVida': {'image': 'powerUpVida', 'tipo': 'vida', 'imageName': powerUpVida},
    'tiroMaisRapido': {'image': 'powerUpTiro', 'tipo': 'tiro', 'imageName': powerUpTiro}
}

eventosTemporarios = {}

mainCharacter = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tiros = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
poderes_grupo = pygame.sprite.Group()