import pygame
from scripts.dados import *
from scripts.objetos import *
from scripts.renderBackground import *

def telaDePause(tela):

    quitButton = carregarImagemRedimencionada(imagens['box']['imagemPyGame'], dimensions['WIDTH']*0.4)

    quitButton.get_height()
    quitButton.get_width()

    rectQuit = quitButton.get_rect()

    rectQuit.centerx = dimensions['WIDTH']/ 2
    rectQuit.centery = dimensions['HEIGHT']/2


    font = fontes['fonteScore']['fontePyGame']
    goBackText = font.render("Go Back to the Game", True, (255, 255, 255))
    goBackTextRect = goBackText.get_rect()
    # Para centralizar o texto no botão
    goBackTextRect.center = rectQuit.center


    runningSkinScreen = True
    while runningSkinScreen:


        tela.SCREEN.blit(quitButton, rectQuit)
        # Desenha o texto na posição centralizada
        tela.SCREEN.blit(goBackText, goBackTextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if rectQuit.collidepoint(mouse_x, mouse_y):
                    runningSkinScreen = False

        pygame.display.flip()
    







