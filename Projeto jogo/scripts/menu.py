import pygame
from scripts.dados import *
from scripts.objetos import *
from scripts.renderBackground import *

# Função para o menu principal
def mainMenu(tela):

    # Reiniciar velocidades
    for item in velocidades:
        velocidades[item] = velocidadesDefault[item]

    tela.reiniciarTela()
    
    # Carregar a imagem do fundo
    fundo = backGround()

    tela.elementosParaRenderizar['backGround'] = fundo
    tela.elementosParaRenderizar['mainCharacter'] = MainCharacter()
    all_sprites.add(tela.elementosParaRenderizar['mainCharacter'])
    mainCharacter.add(tela.elementosParaRenderizar['mainCharacter'])

    # Preenchendo a tela com a cor branca
    tela.SCREEN.fill(BLACK)
    
    # Carregar a imagem de fundo do menu
    fundo = tela.elementosParaRenderizar['backGround']

    start_button = carregarImagemRedimencionada(imagens['box']['imagemPyGame'], layout['larguraBotaoStart'])
    rectStartButton = start_button.get_rect()
    rectStartButton.centerx = dimensions['WIDTH']/ 2
    rectStartButton.centery = dimensions['HEIGHT']/ 2


    # Desenhar texto no botão "Start"
    font = fontes['fonteScore']['fontePyGame']
    start_text = font.render("Start", True, (255, 255, 255))
    text_rect = start_text.get_rect()
    # Para centralizar o texto no botão
    text_rect.center = rectStartButton.center
    # Desenha o texto na posição centralizada


    # Desenhar texto no botão "Start"
    font = fontes['fonteTituloJogo']['fontePyGame']
    nome_text = font.render(f"{gameName}", True, (255, 255, 255))
    nome_text_rect = nome_text.get_rect()
    # Para centralizar o texto no botão
    nome_text_rect.centerx = dimensions['WIDTH']/2
    nome_text_rect.top = dimensions['HEIGHT']*0.2
    # Desenha o texto na posição centralizada


    # Loop principal do menu
    running = True
    while running:

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if rectStartButton.collidepoint(mouse_x, mouse_y):
                    return
                
        renderBackground(tela, tela.speedMenu)

        # Desenha o botão no centro da tela
        tela.SCREEN.blit(start_button, (rectStartButton.x, rectStartButton.y))
        tela.SCREEN.blit(nome_text, (nome_text_rect.x, nome_text_rect.y))
        tela.SCREEN.blit(start_text, text_rect)

        pygame.display.flip()

