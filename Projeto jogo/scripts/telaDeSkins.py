import pygame
from scripts.dados import *
from scripts.objetos import *
from scripts.renderBackground import *

def telaDeSkins(tela):

    boxComSkins = carregarImagemRedimencionada(imagens['bigBox']['imagemPyGame'], dimensions['WIDTH']*0.8)
    boxRect = boxComSkins.get_rect()
    boxRect.centerx = dimensions['WIDTH']/ 2
    boxRect.centery = dimensions['HEIGHT']/ 2

    quitButton = carregarImagemRedimencionada(imagens['box2']['imagemPyGame'], dimensions['WIDTH']*0.3)

    quitButton.get_height()
    quitButton.get_width()

    rectQuit = quitButton.get_rect()

    rectQuit.centerx = dimensions['WIDTH']/ 2
    rectQuit.bottom = boxRect.bottom - boxComSkins.get_height() * 0.1


    font = fontes['fonteGameOver']['fontePyGame']
    goBackText = font.render("Go Back to the Menu", True, (255, 255, 255))
    goBackTextRect = goBackText.get_rect()
    # Para centralizar o texto no botão
    goBackTextRect.center = rectQuit.center

    coluna = -2
    j = -1
    for skin in skinsNave:
        skinsNave[skin]['imagemCarregada'] = carregarImagemRedimencionada(skinsNave[skin]['imagemPyGame'], boxComSkins.get_width()*0.15)

        rect = skinsNave[skin]['imagemCarregada'].get_rect()
        
        rect.centerx = boxRect.centerx + (boxRect.width * 0.175)*coluna

        rect.centery = boxRect.centery + (boxRect.height * 0.20)*j

        skinsNave[skin]['rect'] = rect

        coluna += 1
        if coluna > 2:
            coluna = -2
            j = 0.5


    
    runningSkinScreen = True
    while runningSkinScreen:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if rectQuit.collidepoint(mouse_x, mouse_y):
                    runningSkinScreen = False

                for skin in skinsNave:
                    if skinsNave[skin]['rect'].collidepoint(mouse_x, mouse_y):

                        mainCharacter.empty()
                        all_sprites.remove(tela.elementosParaRenderizar['mainCharacter'])

                        imagens['mainCharacter']['imagemPyGame'] = skinsNave[skin]['imagemPyGame']

                        tela.elementosParaRenderizar['mainCharacter'] = MainCharacter()
                        all_sprites.add(tela.elementosParaRenderizar['mainCharacter'])
                        mainCharacter.add(tela.elementosParaRenderizar['mainCharacter'])
                        runningSkinScreen = False





        tela.SCREEN.fill(BLACK)
        renderBackground(tela, tela.speedMenu)
        # Preenchendo a tela com a cor branca
        tela.SCREEN.blit(boxComSkins, boxRect)

        for skin in skinsNave:
            tela.SCREEN.blit(skinsNave[skin]['imagemCarregada'], skinsNave[skin]['rect'])

        tela.SCREEN.blit(quitButton, rectQuit)
        # Desenha o texto na posição centralizada
        tela.SCREEN.blit(goBackText, goBackTextRect)



        pygame.display.flip()





