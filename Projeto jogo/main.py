from scripts.inicializar import startGame
from scripts.runGame import *
from scripts.dados import  *
from scripts.menu import *


tela = startGame()
while True:
    mainMenu (tela)
    runGame(tela)

