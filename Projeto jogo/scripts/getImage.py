import os


def getImagem (nomeDaImagem):
    script_dir = os.path.dirname(__file__)
    rel_path = f"../assets/image/{nomeDaImagem}"
    image_path = os.path.join(script_dir, rel_path)
    return image_path
