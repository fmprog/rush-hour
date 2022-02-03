# Rush Hour
*Team: emilyfabife.py*

### The case

Rush Hour is a slide puzzle game in which a red car has to exit the board. This is not so easy, however, as the red car is blocked by multiple cars and trucks! The game's rules are simple - vehicles can only move in the direction of their orientation, are not allowed to turn, and cannot drive to spots where other vehicles are located - but finding the best solution to the puzzle is incredibly difficult, especially as the size of the gameboard increases!

Therefore, our team set out to develop a good algorithm for a computer to find a fast and short solution to rush hour puzzles.

### State Space
The state space in our case represents all different ways in which the vehicles can be aranged on the gameboard. To calculate the upper-bound of the state space, we count all (theoretically possible) positions of each vehicle and multiple these. 
A car is 2 spaces long and can therefore always take (size of gameboard) - 1 positions on the board. A truck is 3 spaces long and can therefore only take (size of gameboard - 2) positions on the gameboard.

This upper-bound is sure to exceed the actual state space as this formula does not take into account that vehicles are not allowed to exist on the same space.

The formula is:
```
((size_gameboard - 1) ^ number_of_cars) * ((size_gameboard - 2) ^ number_of_vehicles)
```

## Getting Started
### Requirements
This codebase is written in Python 3.8.10. No additional packages are required to run the code. 

### Instructions
The script can be executd by running the following code:
```
python main.py
```
In main.py in the section "Game" you can choose a gameboard by changing the gameboard and gamesize variables. By commenting out one of the algorithms, you can select an algorithm to run and the variable iterations allows you to choose how many times you want to run the algorithm. Keep in mind the hill climber algorithm requires a solution from the depth first or random algorithm to run!

The "results" section handles creating a CSV file with the results. The section "histogram" allows you to turn the data into a histogram.

### Structure 
- **/code:** contains all code for this project
  - **/code/algorithms:** contains all developed algorithms
    - **/code/algorithms/randomise.py**: finds a random solution to the puzzle by selecting at random vehicles and possible direction and playing these moves
    - **/code/algorithms/depth_first.py**: finds a depth first solution to the puzzle by vertically following one branch of moves until a solution is found
    - **/code/algorithms/breadh_first.py**: finds a breadth first solution to the puzzle horizontally by playing each possible move on every layer until a solution is found
    - **/code/algorithms/hill_climber.py**: improves a depth first or random solution by selection random parts of the solution and improving them with the breadth first algorithm
  - **/code/classes:** contains all classes
    - **/code/classes/vehicle.py**: contains all necessary attributes of a vehicle
    - **/code/classes/game.py**: contains functions to create the gameboard (grid), load the vehicles onto the board from a csv file, show the gameboard, find possible moves on the board and play moves, and a function to check if the current board is solved
  - **/code/visualisation:** empty!

- **/data:** contains csv files with data to load 7 different rush hour gameboards:
  - 3 games with a 6x6 gameboard
  - 3 games with a 9x9 gameboard
  - 1 game with a 12x12 gameboard

## Authors
- Fabienne van Baren
- Fé de Haan
- Emily Timmerman

## Acknowledgements
- StackOverflow
- Minor Programmering Universiteit van Amsterdam
