from scripts.inicializar import *
from scripts.runGame import *
from scripts.dados import  *
from scripts.menu import *

def main():
    tela = startGame()
    while True:
        mainMenu (tela)
        runGame(tela)

if __name__ == "__main__":
    main ()

