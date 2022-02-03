import time
import csv
import matplotlib.pyplot as plt
from code.algorithms import randomise
from code.algorithms import depth_first
from code.algorithms import breadth_first
from code.algorithms import hill_climber
from code.classes.game import Game

start = time.time()
n_runs = 0
results = []

start_time = time.time()
while n_runs < 1:

    # choose gameboard and gameboard size
    algorithm_name = "Hill Climber Depth First"
    gameboard = "Rushhour9x9_4.csv"
    gamesize = 9

    # create game from input
    game = Game(gameboard, gamesize)
    algorithm_type = depth_first.DepthFirst(game)
    algorithm_type.run()
    solution = algorithm_type.return_solution()
    algorithm_type = hill_climber.HillClimber(game, solution)
    algorithm_type.run(100)
    solution = algorithm_type.return_solution()

    results.append(len(solution))

    n_runs += 1

end_time = time.time()
seconds = end_time - start_time 

# save the results in a csv file
with open(f'Results{algorithm_name}{gameboard}', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)


    # write multiple rows
    for value in range(len(results)):
        writer.writerow([f'Run {value + 1}', results[value]])
    writer.writerow([f"Total time = {round(seconds, 5)} seconds."])
    
# --------------------------- Histogram ---------------------

plt.hist(results, color = "blue", bins = 100)
plt.xlabel("Lengte Pad")
plt.ylabel("Frequentie lengte pad")
plt.title(f"Resultaten {algorithm_name} Algoritme {gameboard}")

# save graph
plt.savefig(f"{algorithm_name} game 9x9 4")