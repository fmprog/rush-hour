from code.classes.game import Game
import random
from code.algorithms import randomise


if __name__ == "__main__":
    # Load game 1
    game = Game("Rushhour6x6_1.csv", 6)
    game.show_board()
    randomise.random_solver(game)

