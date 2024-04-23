import pygame

# dados brutos
gameName = "SPACE ITA"
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
    'larguraElementosDeFundo': dimensions["WIDTH"] * 0.07,
    'larguraEstrela': dimensions["WIDTH"] * 0.02,
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
    'obstaculoImage1': {'diretorio': 'meteoro.png', 'imagemPyGame': ''},
    'obstaculoImage2': {'diretorio': 'meteoro2.png', 'imagemPyGame': ''},
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
    'backgorundElement1': {'diretorio': 'backgorundElement1.png', 'imagemPyGame': ''},
    'backgorundElement2': {'diretorio': 'backgorundElement2.png', 'imagemPyGame': ''},
    'backgorundElement3': {'diretorio': 'backgorundElement3.png', 'imagemPyGame': ''},
    'backgorundElement4': {'diretorio': 'backgorundElement4.png', 'imagemPyGame': ''},
    'backgorundElement5': {'diretorio': 'backgorundElement5.png', 'imagemPyGame': ''},
    'estrela1': {'diretorio': 'estrela1.png', 'imagemPyGame': ''},
    'estrela2': {'diretorio': 'estrela2.png', 'imagemPyGame': ''},
    }

# fontes para serem carregadas
arquivoFonte = 'ARCADE_N.TTF'  

fontes = {
    'fonteScore': {'diretorio': 'ARCADE_N.TTF',   'tamanho': 36, 'fontePyGame': ''},
    'fonteGameOver': {'diretorio': 'ARCADE_N.TTF', 'tamanho': 20, 'fontePyGame': ''},
    'fonteScoreGameOver': {'diretorio': 'ARCADE_N.TTF',   'tamanho': 45, 'fontePyGame': ''},
    'fonteGameOver': {'diretorio': 'ARCADE_N.TTF', 'tamanho': 20, 'fontePyGame': ''},
    'fonteBigGameOver': {'diretorio': 'ARCADE_N.TTF', 'tamanho': 70, 'fontePyGame': ''},
    'fonteTituloJogo': {'diretorio': 'ARCADE_N.TTF', 'tamanho': 100, 'fontePyGame': ''},
          }

# scores que a tela estara contabilizando
scores = {
    'score': 1,
    'scoreParaGerarObstaculo': 1,
    'scoreParaGerarPoder': 1,
    'scoreParaAumentarVelocidade': 1,
    'scoreParaAumentarVelocidadeObstaculo': 1,
    'scoreParaAumentarVelocidadeGeracaoObstaculo': 1,
    'scoreParaGerarBoss': 1,
    'scoreParaPerderOutraVida': 1,
    'scoreParaPerderOutraVidaBoss': 1,
    'scoreParaGerarElementoDeFundo': 1,
    'scoreParaGerarEstrela': 1,
    'scoreParaGerarElementoDeFundo': 1,
    'scoreParaGerarEstrela': 1,
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
               'scoreParaGerarElementoDeFundo': 500,
               'scoreParaGerarEstrela': 50,

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
all_sprites = pygame.sprite.Group()
explosaoGroup = pygame.sprite.Group()
mainCharacter = pygame.sprite.Group()
tiros = pygame.sprite.Group()
tirosInimigos = pygame.sprite.Group()
meteoros = pygame.sprite.Group()
inimigosGroup = pygame.sprite.Group()
poderes_grupo = pygame.sprite.Group()
elementosDefundo = pygame.sprite.Group()
estrelas = pygame.sprite.Group()

