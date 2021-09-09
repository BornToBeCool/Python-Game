from game import *
from team import *
import time

def  runGame():
    game = Game()
    game.AP_or_AR()
    while True:
        if (len(game.teams[0].alive_heroes) == 0 or len(game.teams[1].alive_heroes) == 0):
            break
        print("Round " + str(game.game_round()))
        print("---------------------------------------")
        print(" ")
        game.printHeroes()
        game.calculate_and_apply_damages()
        time.sleep(1)

    