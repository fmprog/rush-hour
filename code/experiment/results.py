import subprocess
import time
import csv

start = time.time()
n_runs = 0

while time.time() - start < 3600:
    print(f"run: {n_runs}")
    subprocess.call(["timeout", "60", "python3", "random_algorithm.py"])

    with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

    n_runs += 1