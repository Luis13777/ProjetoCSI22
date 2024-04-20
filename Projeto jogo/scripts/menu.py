import pygame
from scripts.dados import *


# Função para o menu principal
def mainMenu(tela):


    # Carregar a imagem de fundo do menu
    fundo = tela.elementosParaRenderizar['backGround']
    larguraDaImagemFundo = fundo.image.get_width()


    # Criar um retângulo para o botão "Start"
    start_button = imagens['box']['imagemPyGame']
    original_image_width, original_image_height = start_button.get_size()
    final_image_width = dimensions["WIDTH"] * 0.2
    final_image_height = original_image_height * final_image_width / original_image_width
    start_button = pygame.transform.scale(start_button, (final_image_width, final_image_height))

    center_x = (dimensions['WIDTH'] - final_image_width) // 2
    center_y = (dimensions['HEIGHT'] - final_image_height) // 2

    # Loop principal do menu
    running = True
    while running:

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                button_rect = pygame.Rect(center_x, center_y, int(final_image_width), int(final_image_height))
                if button_rect.collidepoint(mouse_x, mouse_y):
                    return





        # Desenhar os fundos na tela
        tela.SCREEN.blit(fundo.image, (fundo.positionX, fundo.positionY))
        tela.SCREEN.blit(fundo.image, (fundo.positionX + larguraDaImagemFundo, fundo.positionY))
        tela.SCREEN.blit(fundo.image, (fundo.positionX + 2*larguraDaImagemFundo, fundo.positionY))
        tela.SCREEN.blit(fundo.image, (fundo.positionX + 3*larguraDaImagemFundo, fundo.positionY))

        fundo.positionX -= tela.speedMenu
        if fundo.positionX <= -larguraDaImagemFundo:
            fundo.positionX = 0

        # Desenha o botão no centro da tela
        tela.SCREEN.blit(start_button, (center_x, center_y))
        
        # Desenhar texto no botão "Start"
        font = fontes['fonteScore']['fontePyGame']
        start_text = font.render("Start", True, (255, 255, 255))
        text_rect = start_text.get_rect()
        # Para centralizar o texto no botão
        text_rect.center = (center_x + final_image_width // 2, center_y + final_image_height // 2)
        # Desenha o texto na posição centralizada
        tela.SCREEN.blit(start_text, text_rect)


        pygame.display.flip()

