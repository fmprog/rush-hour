from code.classes.game import Game
from code.algorithms import randomise
from code.algorithms import depth_first
from code.algorithms import breadth_first


if __name__ == "__main__":
    # Choose gameboard and gameboard size
    gameboard = "Rushhour9x9_4.csv"
    gamesize = 9

    # Create game from input
    game = Game(gameboard, gamesize)

    # --------------------------- Random Algorithm --------------------------
    #randomise.random_solver(game)

    # --------------------------- Breadth First Aglorithm -------------------
    breadth = breadth_first.BreadthFirst(game)
    breadth.run()

    # --------------------------- Depth First Algorithm ---------------------
    #depth = depth_first.DepthFirst(game)
    #depth.run()