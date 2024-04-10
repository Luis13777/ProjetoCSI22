import os


def getEndereco (nomeDaImagem, pasta = 'image'):
    script_dir = os.path.dirname(__file__)
    rel_path = f"../assets/{pasta}/{nomeDaImagem}"
    image_path = os.path.join(script_dir, rel_path)
    return image_path
