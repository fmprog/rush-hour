from code.classes.game import Game
from code.classes.hill_climber_game import HillClimberGame
from code.algorithms import randomise
from code.algorithms import depth_first
from code.algorithms import breadth_first
from code.algorithms import hill_climber


if __name__ == "__main__":
    # Choose gameboard and gameboard size
    gameboard = "Rushhour6x6_1.csv"
    gamesize = 6

    # Create game from input
    game = Game(gameboard, gamesize)

    # --------------------------- Random Algorithm --------------------------
    #randomise.random_solver(game)

    # --------------------------- Breadth First Aglorithm -------------------
    # breadth = breadth_first.BreadthFirst(game)
    # breadth.run()

    # --------------------------- Depth First Algorithm ---------------------
    depth = depth_first.DepthFirst(game)
    depth.run()
    solution = depth.return_solution()

    # --------------------------- Hill Climber Algorithm ---------------------
    hill_climber = hill_climber.HillClimber(game, solution)
    hill_climber.run(10)