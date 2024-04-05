# import pygame
# from scripts.dados import *
# from scripts.renderBackground import *
# from scripts.renderObstaculos import *
# from scripts.checkCollision import *
# from scripts.playerAction import *

# score = 0
# def runGame (tela): 




#     # Loop principal do jogo
#     player = tela.elementosParaRenderizar['mainCharacter']
#     running = True

#     while running:
#         threads = []
#         # Crie e inicie uma thread para cada função
#         thread2 = threading.Thread(target=checkCollision, args=(tela,))
#         thread3 = threading.Thread(target=all_sprites.update)
#         thread4 = threading.Thread(target=all_sprites.update)

#         tela.score += 1/FPS
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Preenchendo a tela com a cor branca
#         tela.SCREEN.fill(BLACK)

#         thread = threading.Thread(target=renderBackground, args=(tela,))
#         thread.start()
#         threads.append(thread)

#         # renderBackground(tela)

#         # Verificando teclas pressionadas
#         # keys = pygame.key.get_pressed()
#         # if keys[pygame.K_UP]:
#         #     player.moveUp()
#         # if keys[pygame.K_DOWN]:
#         #     player.moveDown()
#         # if keys[pygame.K_SPACE]:
#         #     player.shoot()

#         thread = threading.Thread(target=playerActions, args=(player,))
#         thread.start()
#         threads.append(thread)



#         # Desenhando a imagem na tela
#         # tela.SCREEN.blit(player.image, (player.positionX, player.positionY))
#         # if tela.score > 0.5:
#         #     tela.score = 0
#         #     tela.speed += 1
#         #     novoObstaculo(tela)
        
#         for evento in pygame.event.get():
#             if evento.type == eventosTemporarios['gerarObstaculo']:
#                 novoObstaculo(tela)
        
        
#         thread = threading.Thread(target=checkCollision, args=(tela,))
#         thread.start()
#         threads.append(thread)

#         # checkCollision(tela)
        
#         # Aguarde a conclusão de todas as threads (opcional)

#         # Atualize a posição dos sprites

#         thread = threading.Thread(target=all_sprites.update)
#         thread.start()
#         threads.append(thread)
        
#         # all_sprites.update()

#         for thread in threads:
#             thread.join()

#         # thread1.join()
#         # thread2.join()
#         # thread3.join()
        
#         # Renderize os sprites na tela
#         all_sprites.draw(tela.SCREEN)

#         # Atualizar a tela
#         pygame.display.flip()
        
#         # Controlando a taxa de quadros
#         tela.clock.tick(0)
        
#     # Finalizar o Pygame
#     pygame.quit()

import pygame
from scripts.dados import *
from scripts.renderBackground import *
from scripts.renderObstaculos import *
from scripts.checkCollision import *
from scripts.playerAction import *
from scripts.renderizarMenuTopo import *
from scripts.aumentarDificuldade import *
from scripts.poderes import *

def runGame (tela): 




    # Loop principal do jogo
    player = tela.elementosParaRenderizar['mainCharacter']
    running = True

    while running:


        tela.score += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Preenchendo a tela com a cor branca
        tela.SCREEN.fill(BLACK)


        renderBackground(tela)

        playerActions(player)
        
        # for evento in pygame.event.get():
        #     if evento.type == eventosTemporarios['gerarObstaculo']:
        #         novoObstaculo(tela)
        #     if evento.type == eventosTemporarios['gerarPowerUp']:
        #         novoPowerUp(tela)

        if tela.score % velocidades['pontosParaGerarObstaculo'] == 0:
            novoObstaculo(tela)
        if tela.score % velocidades['pontosParaGerarPoder'] == 0:
            novoPowerUp(tela)
        


        checkCollision(tela)
        renderizarMenuTopo(tela)
        aumentarDificuldade(tela)
        # Atualize a posição dos sprites


        
        all_sprites.update()


        
        # Renderize os sprites na tela
        all_sprites.draw(tela.SCREEN)

        # Atualizar a tela
        pygame.display.flip()
        
        # Controlando a taxa de quadros
        tela.clock.tick(60)
        
    # Finalizar o Pygame
    pygame.quit()