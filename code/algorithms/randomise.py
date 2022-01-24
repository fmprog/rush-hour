import random
import copy


def random_solver(game):

    X = game.vehicles['X']
    attempt = 1
    
    while game.is_solved() == False:
   
        possibilities_vehicles = list(game.vehicles.keys())
        select_vehicle = random.choice(possibilities_vehicles)

        possibilities_direction = game.possible_direction(select_vehicle)
        
        if len(possibilities_direction) > 0:
            select_direction = random.choice(possibilities_direction)

            # move with selected vehicle to selected direction
            game.move(select_vehicle, select_direction)
            print(f"Move: Vehicle {select_vehicle} - Direction {select_direction}")
            game.show_board()
            print('-------------------')
            attempt += 1

    print(f"Solved the puzzle in {attempt} attempts.")