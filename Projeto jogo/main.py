from scripts.inicializar import startGame
from scripts.runGame import *
from scripts.dados import  *
from scripts.menu import *


while True:
    tela = startGame()
    mainMenu (tela)
    runGame(tela)

