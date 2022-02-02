# Rush Hour
Rush Hour is a slide puzzle game in which a red car has to exit the board. This is not so easy, however, as the red car is blocked by multiple cars and trucks! The game's rules are simple - vehicles can only move in the direction of their orientation, are not allowed to turn, and cannot drive to spots where other vehicles are located - but finding the best solution to the puzzle is incredibly difficult, especially as the size of the gameboard increases!

Therefore, our team set out to develop a good algorithm for a computer to find a fast and short solution to rush hour puzzles.

## Getting Started
### Requirements
This codebase is written in Python 3.8.10. No additional packages are required to run the code. 

### Structure 
Alle Python scripts staan in de folder Code. In de map Data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.
- **/code:** contains all code for this project
  - **/code/algorithms:** contains all developed algorithms
    -**/code/algorithms/randomise.py**: finds a random solution to the puzzle by selecting at random vehicles and possible direction and playing these moves
    -**/code/algorithms/depth_first.py**: finds a depth first solution to the puzzle by vertically following one branch of moves until a solution is found
    -**/code/algorithms/breadh_first.py**: finds a breadth first solution to the puzzle horizontally by playing each possible move on every layer until a solution is found
    -**/code/algorithms/hill_climber.py**: improves a depth first or random solution by selection random parts of the solution and improving them with the breadth first algorithm
  - **/code/classes:** contains all classes
    -**/code/classes/vehicle.py**: contains all necessary attributes of a vehicle
    -*/code/classes/game.py*: contains functions to create the gameboard (grid), load the vehicles onto the board from a csv file, show the gameboard, find possible moves on the board and play moves, and a function to check if the current board is solved
  - */code/visualisation:* empty!

- */data:* contains csv files with data to load 7 different rush hour gameboards:
  - 3 games with a 6x6 gameboard
  - 3 games with a 9x9 gameboard
  - 1 game with a 12x12 gameboard

### Test
Om de code te draaien met de standaardconfiguratie (bv. brute-force en voorbeeld.csv) gebruik de instructie:

```bash
python main.py
```
## Auteurs
Fabienne van Baren, Fé de Haan en Emily Timmerman

## Dankwoord
StackOverflow
minor programmeren van de UvA
