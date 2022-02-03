import csv
import time 
import matplotlib.pyplot as plt
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

    # Select how many iterations you want the algorithm to run
    iterations = 3
 
    results = []
    start_time = time.time()
    n_runs = 0

    while n_runs < iterations:


        # --------------------------- Random Algorithm --------------------------
        algorithm_name = "Random Algorithm"
        random = randomise.Randomise(game)
        random.run()

        solution = random.return_solution()


        # --------------------------- Breadth First Aglorithm -------------------
        #algorithm_name = "Breadth First Algorithm"
        #breadth = breadth_first.BreadthFirst(game)
        #breadth.run()

        #solution = breadth.return_solution()


        # --------------------------- Depth First Algorithm ---------------------
        #algorithm_name = "Depth First Algorithm"
        #depth = depth_first.DepthFirst(game)
        #depth.run()

        #solution = depth.return_solution()

        # --------------------------- Hill Climber Algorithm ---------------------
        #algorithm_name = "Hill Climber Algorithm"
        #hill_climber = hill_climber.HillClimber(game, solution)
        #hill_climber.run(100)

        #solution = hill_climber.return_solution()

         # --------------------------- Results -------------------------------------

        results.append(len(solution))
        n_runs += 1

    end_time = time.time()
    run_time = end_time - start_time 

    # Save the results in a csv and store the directory results
    with open(f'code/results/Results{algorithm_name}{gameboard}', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        for value in range(len(results)):
            writer.writerow([f'Run {value + 1}', results[value]])
        writer.writerow([f"Total time = {round(run_time, 5)} seconds."])
    
# --------------------------- Histogram ---------------------

    plt.hist(results, color = "blue", bins = 100)
    plt.xlabel("Path length in steps")
    plt.ylabel("Frequency path length")
    plt.title(f"Results {algorithm_name} for {gameboard}")

    plt.savefig(f"code/visualisation/{algorithm_name} for {gameboard}.png")