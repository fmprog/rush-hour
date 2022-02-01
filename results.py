import subprocess
import time
import csv
import matplotlib as plt
from code.algorithms import randomise
from code.algorithms import depth_first
from code.algorithms import breadth_first
from code.algorithms import hill_climber

start = time.time()
n_runs = 1
header = []
paths = []
file = "code/algorithms/randomise.py"
game = "Rushhour6x6_1.csv"

while time.time() - start < 3600:

    header.append(f'Run {n_runs}')

    code = subprocess.call(["timeout", "60", "python3", "results.py"])
    # # code = subprocess.call(["ping", "www.yahoo.com"])

    path = 0
    paths.append(path)


    with open(f'results.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(paths)

    n_runs += 1

    # # --------------------------- Histogram ---------------------
    # results = []
    # random = randomise.Randomise(game)
    # random.run()
    # solution = random.return_solution()
    # for i in range(100):
    #     print(i)
    #     hill = hill_climber.HillClimber(game, solution)
    #     hill.run(100)

    #     result = hill.solution_len
    #     results.append(result)

    # print(f"{game} resultaten: {results}")
    # # Make bar plot
    # plt.hist(results, color="blue", bins=range(100))

    # plt.xlabel("Lengte Pad")
    # plt.ylabel("Frequentie lengte pad")
    # plt.title(f"Resultaten Rush Hour {game}")

    # # Show graphic
    # plt.savefig("9x9 bord")