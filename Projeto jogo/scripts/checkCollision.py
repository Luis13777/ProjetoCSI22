from scripts.dados import *
from scripts.objetos import *


def checkCollision(tela):

    hits = pygame.sprite.groupcollide(mainCharacter, meteoros,  False, True)
    for hit in hits:
        nave = hit
        explosao = Explosao((nave.rect.right, nave.rect.centery), hits[hit])
        all_sprites.add(explosao)
        explosaoGroup.add(explosao)
        nave.perderVida()
        
    hits = pygame.sprite.groupcollide(tiros, meteoros, True, True)
    for hit in hits:
        laser = hit
        explosao = Explosao((laser.rect.right, laser.rect.centery), hits[hit])
        all_sprites.add(explosao)
        explosaoGroup.add(explosao)

        tela.scores['score'] += infos['pontosPorDestruirObstaculo']

    for poder in poderes_grupo:
        if pygame.sprite.collide_mask(tela.elementosParaRenderizar['mainCharacter'], poder):
            if poder.tipo == 'vida' and tela.elementosParaRenderizar['mainCharacter'].vidas < tela.elementosParaRenderizar['mainCharacter'].maxVidas:
                tela.elementosParaRenderizar['mainCharacter'].vidas += 1
                sons['oneUp']['somPyGame'].play()
            elif poder.tipo == 'tiro':
                tela.elementosParaRenderizar['mainCharacter'].shoot_delay -= infos['tempoDeMenosDelayPowerUpTiro']
                sons['powerup2']['somPyGame'].play()
            elif poder.tipo == 'invencibilidade':
                tela.elementosParaRenderizar['mainCharacter'].Invencibilidade()
                sons['cogumeloMario']['somPyGame'].play()
                tela.scores['score'] += 500
            
            poder.kill()

    hits = pygame.sprite.groupcollide(tiros, inimigosGroup, True, False)
    for hit in hits:
        laser = hit
        explosao = Explosao((laser.rect.right, laser.rect.centery), hits[hit])
        all_sprites.add(explosao)
        explosaoGroup.add(explosao)

        for inimigo in inimigosGroup:
            inimigo.perderVida()
        tela.scores['score'] += infos['pontosPorAcertarBoss']


    hits = pygame.sprite.groupcollide(tirosInimigos, mainCharacter, True, False)
    for hit in hits:
        laser = hit
        explosao = Explosao((laser.rect.left, laser.rect.centery), hits[hit])
        all_sprites.add(explosao)
        explosaoGroup.add(explosao)

        for character in mainCharacter:
            character.perderVida()