from scripts.dados import *
from scripts.objetos import *


def checkCollision(tela):
    for obstaculo in tela.elementosParaRenderizar['obstaculo']:
        if obstaculo.positionX - tela.elementosParaRenderizar['mainCharacter'].image.get_width() < tela.elementosParaRenderizar['mainCharacter'].positionX and tela.elementosParaRenderizar['mainCharacter'].positionX  < obstaculo.positionX + obstaculo.image.get_width():
            if obstaculo.positionY - tela.elementosParaRenderizar['mainCharacter'].image.get_height() < tela.elementosParaRenderizar['mainCharacter'].positionY and tela.elementosParaRenderizar['mainCharacter'].positionY < obstaculo.positionY + obstaculo.image.get_height():
                # Criar uma superfície para o círculo
                circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
                pygame.draw.circle(circle_surface, (255, 0, 0), (10, 10), 10)  # Desenhar um círculo vermelho

                # Definir as coordenadas do canto superior direito
                circle_position = (0, 0)

                # Blitar o círculo na tela principal
                tela.SCREEN.blit(circle_surface, circle_position)

# def checkCollision(tela):
#     personagem = tela.elementosParaRenderizar['mainCharacter']
    
#     for obstaculo in tela.elementosParaRenderizar['obstaculo']:
#         if pygame.sprite.collide_mask(personagem, obstaculo):
#             # Criar uma superfície para o círculo
#             circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
#             pygame.draw.circle(circle_surface, (255, 0, 0), (10, 10), 10)  # Desenhar um círculo vermelho

#             # Definir as coordenadas do canto superior direito
#             circle_position = (0, 0)

#             # Blitar o círculo na tela principal
#             tela.SCREEN.blit(circle_surface, circle_position)
