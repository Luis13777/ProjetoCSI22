import pygame

# dados brutos
gameName = "Jogo CSI22"
dimensions = {"WIDTH": 1920,
"HEIGHT": 1080}
FPS = 144

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
AMARELO = (255, 255, 0)
AZUL_CLARO = (173, 216, 230)

# características do layout
layout = {
    'proporcaoDoMenu': dimensions["HEIGHT"]*0.1,
    'proporcaoDoResto': dimensions["HEIGHT"]*0.9,
    'posicaoDaNaveX': dimensions["WIDTH"]*0.1,
    'posicaoDaNaveY': dimensions["HEIGHT"]*0.5,
    'limiteInferior': dimensions["HEIGHT"],
    'larguraCoracao': dimensions["WIDTH"]*0.05,
    'fundo': dimensions["HEIGHT"],
    'larguraTiro': dimensions["WIDTH"] * 0.1,
    'larguraDoPoder': dimensions["WIDTH"] * 0.05,
    'larguraDoBoss': dimensions["WIDTH"] * 0.1,
    'posicaoXBoss': dimensions["WIDTH"] * 0.9,
    'larguraBotaoStart': dimensions["WIDTH"] * 0.2,
}

infos = {
    'maxVidas': 3,
    'tempoDeExplosao': 100,
    'maxVidasBoss': 3,
    'pontosPorAcertarBoss': 100,
    'pontosPorDestruirObstaculo': 50,
    'tempoDeMenosDelayPowerUpTiro': 100,


}

# imagens para serem carregadas
imagens ={
    'mainCharacter': {'diretorio': 'nave.png', 'imagemPyGame': ''},
    'backGroundImage': {'diretorio': 'space.png', 'imagemPyGame': ''},
    'obstaculoImage': {'diretorio': 'meteoro.png', 'imagemPyGame': ''},
    'tiroImage': {'diretorio': 'tiro.png', 'imagemPyGame': ''},
    'explosaoImage': {'diretorio': 'explosao.png', 'imagemPyGame': ''},
    'vidaCheia': {'diretorio': 'vidaCheia.png', 'imagemPyGame': ''},
    'vidaVazia': {'diretorio': 'vidaVazia.png', 'imagemPyGame': ''},
    'boss': {'diretorio': 'inimigo1.png', 'imagemPyGame': ''},
    'bossDamaged': {'diretorio': 'inimigo1damaged.png', 'imagemPyGame': ''},
    'bossVeryDamaged': {'diretorio': 'inimigo1verydamaged.png', 'imagemPyGame': ''},
    'powerUpVida': {'diretorio': 'vidaCheia.png', 'imagemPyGame': ''},
    'powerUpTiro': {'diretorio': 'poderTiro.png', 'imagemPyGame': ''},
    'box': {'diretorio': 'box.png', 'imagemPyGame': ''},
    'box2': {'diretorio': 'box2.png', 'imagemPyGame': ''},
    'bigBox': {'diretorio': 'bigBox.png', 'imagemPyGame': ''},
    'mainCharacterTransparente': {'diretorio': 'naveTransparente.png', 'imagemPyGame': ''},


    }

# fontes para serem carregadas
arquivoFonte = 'ARCADE_N.TTF'  

fontes = {
    'fonteScore': {'diretorio': 'ARCADE_N.TTF',   'tamanho': 36, 'fontePyGame': ''},
    'fonteGameOver': {'diretorio': 'ARCADE_N.TTF', 'tamanho': 20, 'fontePyGame': ''},
    'fonteScoreGameOver': {'diretorio': 'ARCADE_N.TTF',   'tamanho': 45, 'fontePyGame': ''},
    'fonteGameOver': {'diretorio': 'ARCADE_N.TTF', 'tamanho': 20, 'fontePyGame': ''},
    'fonteBigGameOver': {'diretorio': 'ARCADE_N.TTF', 'tamanho': 70, 'fontePyGame': ''},
          }

# velocidades dos elementos
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
               'scoreParaAumentarVelocidadeGeracaoObstaculo': 300,
               'scoreParaGerarBoss': 300,
               'boss1Speed': 2,
               'menuSpeed': 1,
               'shootDelay': 1000,
               'scoreParaPerderOutraVida': 3000,
               'delayPiscada': 200,'tempoDeDelayTiroBoss': 1000,
               'scoreParaPerderOutraVidaBoss': 1000,



               }

# dicionario reserva para resetar o jogo
velocidadesDefault = velocidades.copy()

# poderes que podem ser adquiridos
poderes = {
    'maisVida': {'image': 'powerUpVida', 'tipo': 'vida', 'imageName': imagens['powerUpVida']['diretorio']},
    'tiroMaisRapido': {'image': 'powerUpTiro', 'tipo': 'tiro', 'imageName': imagens['powerUpTiro']['diretorio']}
}

# sons que podem ser tocados
sons = {
    'shot': {'diretorio': 'shot.wav', 'somPyGame': ''},
    'killPlayer': {'diretorio': 'killPlayer.wav', 'somPyGame': ''},
    'critical': {'diretorio': 'critical.mp3', 'somPyGame': ''},
    'warning': {'diretorio': 'warning.mp3', 'somPyGame': ''},
    'killObject': {'diretorio': 'killObject.mp3', 'somPyGame': ''},
    'powerup2': {'diretorio': 'powerup2.mp3', 'somPyGame': ''},
    'oneUp': {'diretorio': 'oneUp.mp3', 'somPyGame': ''}
}

# grupos de sprites
mainCharacter = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tiros = pygame.sprite.Group()
tirosInimigos = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
poderes_grupo = pygame.sprite.Group()
inimigosGroup = pygame.sprite.Group()

