import os
import pygame
from scripts.dados import *

def carregarImagemRedimencionada (imagem, medida, redimensionarPelaLargura = True):

    if redimensionarPelaLargura:
        original_image_width, original_image_height = imagem.get_size()
        final_image_width = medida
        final_image_height = original_image_height * final_image_width / original_image_width
        imagem = pygame.transform.scale(imagem, (final_image_width, final_image_height))
    else:
        original_image_width, original_image_height = imagem.get_size()
        final_image_height = medida
        final_image_width = original_image_width * final_image_height / original_image_height
        imagem = pygame.transform.scale(imagem, (final_image_width, final_image_height))

    return imagem

def getEndereco (nomeDaImagem, pasta = 'image'):
    rel_path = f"./assets/{pasta}/{nomeDaImagem}"
    return rel_path
