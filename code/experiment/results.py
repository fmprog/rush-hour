import subprocess
import time
import csv
import matplotlib as plt

start = time.time()
n_runs = 1
header = []
paths = []
file = "randomise.py"
game = "Rushhour6x6_1.csv"

while time.time() - start < 3600:

    header.append(f'Run {n_runs}')

    subprocess.call([f'code/algorithms/{file}', "timeout", "60", "python3", file])

    path = 0
    paths.append(path)


    with open(f'results{file}.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(paths)

    n_runs += 1

    # --------------------------- Histogram ---------------------
    results = []
    for i in range(100):
        print(i)
        hill = hill_climber.HillClimber(game, solution)
        hill.run(100)

        result = hill.solution_len
        results.append(result)

    print(f"{game} resultaten: {results}")
    # Make bar plot
    plt.hist(results, color="blue", bins=range(100))

    plt.xlabel("Lengte Pad")
    plt.ylabel("Frequentie lengte pad")
    plt.title(f"Resultaten Rush Hour {game}")

    # Show graphic
    plt.savefig("9x9 bord")