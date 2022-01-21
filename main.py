from code.classes.game import Game
import random
from code.algorithms import randomise
from code.algorithms import first_algorithm


if __name__ == "__main__":
    # Load game 1
    game = Game("Rushhour6x6_1.csv", 6)
    game.show_board()
    # randomise.random_solver(game)
    first_algorithm.random_solver(game)

