from scripts.dados import *
from scripts.funcoesAuxiliares import *

def gameOver(tela):

    gameOverScreen = True
    gameOverBox = carregarImagemRedimencionada(imagens['bigBox']['imagemPyGame'], dimensions['WIDTH']*0.5)
    center_x_big_box = (dimensions['WIDTH'] - gameOverBox.get_width()) // 2
    center_y_big_box = (dimensions['HEIGHT'] - gameOverBox.get_height()) // 2

    quitButton = carregarImagemRedimencionada(imagens['box2']['imagemPyGame'], dimensions['WIDTH']*0.2)


    quitButton.get_height()
    quitButton.get_width()

    center_x_box = (dimensions['WIDTH'] - quitButton.get_width()) // 2
    center_y_box = (dimensions['HEIGHT'] - quitButton.get_height()) // 2 + dimensions["WIDTH"] * 0.05

    while(gameOverScreen):

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                button_rect = pygame.Rect(center_x_box, center_y_box, int(quitButton.get_width()), int(quitButton.get_height()))
                if button_rect.collidepoint(mouse_x, mouse_y):
                    gameOverScreen = False

        # Desenha o botão no centro da tela
        tela.SCREEN.blit(gameOverBox, (center_x_big_box, center_y_big_box))
        # Desenha o botão no centro da tela
        tela.SCREEN.blit(quitButton, (center_x_box, center_y_box))
        

        font = fontes['fonteGameOver']['fontePyGame']
        start_text = font.render("Quit", True, (255, 255, 255))
        text_rect = start_text.get_rect()
        # Para centralizar o texto no botão
        text_rect.center = (center_x_box + quitButton.get_width() // 2, center_y_box + quitButton.get_height() // 2)
        # Desenha o texto na posição centralizada
        tela.SCREEN.blit(start_text, text_rect)


        font = fontes['fonteScoreGameOver']['fontePyGame']
        start_text = font.render(f"Score: {tela.scores['score']}", True, (255, 255, 255))
        text_rect = start_text.get_rect()
        # Para centralizar o texto no botão
        text_rect.center = (center_x_box + quitButton.get_width() // 2, dimensions['HEIGHT']*0.475)
        # Desenha o texto na posição centralizada
        tela.SCREEN.blit(start_text, text_rect)


        font = fontes['fonteBigGameOver']['fontePyGame']
        start_text = font.render("Game over", True, (255, 255, 255))
        text_rect = start_text.get_rect()
        # Para centralizar o texto no botão
        text_rect.center = (center_x_box + quitButton.get_width() // 2, dimensions['HEIGHT']*0.37)
        # Desenha o texto na posição centralizada
        tela.SCREEN.blit(start_text, text_rect)


        pygame.display.flip()

def finalizarJogo (tela):

    

    # del tela
    mainCharacter.empty()
    all_sprites.empty()
    explosaoGroup.empty()
    tiros.empty()
    tirosInimigos.empty()
    meteoros.empty()
    poderes_grupo.empty()
    inimigosGroup.empty()
    estrelas.empty()
    elementosDefundo.empty()