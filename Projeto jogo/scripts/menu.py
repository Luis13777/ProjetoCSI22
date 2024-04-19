import pygame
from scripts.dados import *


# Função para o menu principal
def mainMenu(tela):


    # Carregar a imagem de fundo do menu
    fundo = tela.elementosParaRenderizar['backGround']
    larguraDaImagemFundo = fundo.image.get_width()

    # Calcular as coordenadas para centralizar o botão "Start"
    button_width = 200
    button_height = 50
    button_x = (dimensions['WIDTH'] - button_width) // 2
    button_y = (dimensions['HEIGHT'] - button_height) // 2

    # Criar um retângulo para o botão "Start"
    start_button = pygame.Rect(button_x, button_y, button_width, button_height)

    # Loop principal do menu
    running = True
    while running:
        # Desenhar os fundos na tela
        tela.SCREEN.blit(fundo.image, (fundo.positionX, fundo.positionY))
        tela.SCREEN.blit(fundo.image, (fundo.positionX + larguraDaImagemFundo, fundo.positionY))
        tela.SCREEN.blit(fundo.image, (fundo.positionX + 2*larguraDaImagemFundo, fundo.positionY))
        tela.SCREEN.blit(fundo.image, (fundo.positionX + 3*larguraDaImagemFundo, fundo.positionY))


        # Desenhar o botão "Start"
        pygame.draw.rect(tela.SCREEN, (255, 0, 0), start_button)

        # Desenhar texto no botão "Start"
        font = fontes['fonteScore']['fontePyGame']
        start_text = font.render("Start", True, (255, 255, 255))
        text_rect = start_text.get_rect(center=start_button.center)
        tela.SCREEN.blit(start_text, text_rect)

        pygame.display.flip()

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    return
