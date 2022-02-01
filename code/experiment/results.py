import subprocess
import time
import csv

start = time.time()
n_runs = 1
header = []
results = []

while time.time() - start < 3600:
    print(f"run: {n_runs}")
    header.append(('Run ') + str(n_runs))
    print(header)
    subprocess.call(["timeout", "60", "python3", "randomise.py"])

    result = 0
    results.append(result)


    with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(results)

    n_runs += 1