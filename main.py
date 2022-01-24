from code.classes.game import Game
import random
from code.algorithms import randomise
#from code.algorithms import depth_first


if __name__ == "__main__":
    # Load game 1
    game = Game("Rushhour6x6_1.csv", 6)
    #game.show_board()

    #depth_first.DepthFirst(game).print()

    randomise.random_solver(game)

