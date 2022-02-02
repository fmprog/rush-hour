import time
import csv
import matplotlib.pyplot as plt
from code.algorithms import randomise
from code.algorithms import depth_first
from code.algorithms import breadth_first
from code.algorithms import hill_climber
from code.classes.game import Game

start = time.time()
n_runs = 1
results = []

start_time = time.time()
while n_runs <= 100:

    # choose gameboard and gameboard size
    algorithm_name = "Random"
    gameboard = "Rushhour6x6_1.csv"
    gamesize = 6

    # create game from input
    game = Game(gameboard, gamesize)
    algorithm_type = randomise.Randomise(game)
    algorithm_type.run()
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
    writer.writerow([f"Average time per run = {round((seconds / n_runs), 5)} seconds."])
    
# --------------------------- Histogram ---------------------

plt.hist(results, color = "blue", bins = 100)
plt.xlabel("Lengte Pad")
plt.ylabel("Frequentie lengte pad")
plt.title(f"Resultaten {algorithm_name} Algoritme {gameboard}")

# save graph
plt.savefig(f"{algorithm_name} {gameboard}")