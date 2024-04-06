from scripts.dados import *
from scripts.objetos import *


# def checkCollision(tela):
#     for obstaculo in tela.elementosParaRenderizar['obstaculo']:
#         if obstaculo.positionX - tela.elementosParaRenderizar['mainCharacter'].image.get_width() < tela.elementosParaRenderizar['mainCharacter'].positionX and tela.elementosParaRenderizar['mainCharacter'].positionX  < obstaculo.positionX + obstaculo.image.get_width():
#             if obstaculo.positionY - tela.elementosParaRenderizar['mainCharacter'].image.get_height() < tela.elementosParaRenderizar['mainCharacter'].positionY and tela.elementosParaRenderizar['mainCharacter'].positionY < obstaculo.positionY + obstaculo.image.get_height():
#                 # Criar uma superfície para o círculo
#                 circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
#                 pygame.draw.circle(circle_surface, (255, 0, 0), (10, 10), 10)  # Desenhar um círculo vermelho

#                 # Definir as coordenadas do canto superior direito
#                 circle_position = (0, 0)

#                 # Blitar o círculo na tela principal
#                 tela.SCREEN.blit(circle_surface, circle_position)

def checkCollision(tela):
    for meteoro in meteoros:
        if pygame.sprite.collide_mask(tela.elementosParaRenderizar['mainCharacter'], meteoro):
            tela.elementosParaRenderizar['mainCharacter'].perderVida()
            


            # # Criar uma superfície para o círculo
            # circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
            # pygame.draw.circle(circle_surface, (255, 0, 0), (10, 10), 10)  # Desenhar um círculo vermelho

            # # Definir as coordenadas do canto superior direito
            # circle_position = (0, 0)

            # # Blitar o círculo na tela principal
            # tela.SCREEN.blit(circle_surface, circle_position)
        
    hits = pygame.sprite.groupcollide(tiros, meteoros, True, True)
    for hit in hits:
        laser = hit
        explosao = Explosao((laser.rect.right, laser.rect.centery), hits[hit])
        all_sprites.add(explosao)
        tela.score += 50

    for poder in poderes_grupo:
        if pygame.sprite.collide_mask(tela.elementosParaRenderizar['mainCharacter'], poder):
            if poder.tipo == 'vida' and tela.elementosParaRenderizar['mainCharacter'].vidas < tela.elementosParaRenderizar['mainCharacter'].maxVidas:
                tela.elementosParaRenderizar['mainCharacter'].vidas += 1
            elif poder.tipo == 'tiro':
                tela.elementosParaRenderizar['mainCharacter'].shoot_delay -= 100
            poder.kill()

    hits = pygame.sprite.groupcollide(tiros, inimigosGroup, True, False)
    for hit in hits:
        laser = hit
        explosao = Explosao((laser.rect.right, laser.rect.centery), hits[hit])
        all_sprites.add(explosao)
        for inimigo in inimigosGroup:
            inimigo.perderVida()
        tela.score += 50