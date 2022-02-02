from code.classes.game import Game
from code.algorithms import randomise
from code.algorithms import depth_first
from code.algorithms import breadth_first
from code.algorithms import hill_climber


if __name__ == "__main__":
    # ------------------ Select gameboard and create game -------------------
    gameboard = "Rushhour6x6_1.csv"
    gamesize = 6
    game = Game(gameboard, gamesize)


    # --------------------------- Random Algorithm --------------------------
    random = randomise.Randomise(game)
    random.run()

    solution = random.return_solution()


    # --------------------------- Breadth First Aglorithm -------------------
    #breadth = breadth_first.BreadthFirst(game)
    #breadth.run()

    #solution = breadth.return_solution()


    # --------------------------- Depth First Algorithm ---------------------
    #depth = depth_first.DepthFirst(game)
    #depth.run()

    #solution = depth.return_solution()


    # --------------------------- Hill Climber Algorithm ---------------------
    hill_climber = hill_climber.HillClimber(game, solution)
    hill_climber.run(100)

    solution = hill_climber.return_solution()

    # --------------------------- Results -------------------------------------
    print(f"Puzzle {gameboard} was solved in {len(solution)} moves.")