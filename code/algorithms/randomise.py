import random


def random_solver(game):

    attempt = 1
    
    while game.is_solved() == False:
   
        # randomly select a vehicle to move
        possibilities_vehicles = list(game.vehicles.keys())
        select_vehicle = random.choice(possibilities_vehicles)

        # randomly select a direction to move to
        possibilities_direction = game.possible_direction(select_vehicle)
        
        if len(possibilities_direction) > 0:
            select_direction = random.choice(possibilities_direction)

            # move the selected vehicle to the selected direction
            game.move(select_vehicle, select_direction)

            # print out information about the move and gameboard
            game.show_board(select_vehicle, select_direction)

            # keep track of the attempts
            attempt += 1

    print(f"Solved the puzzle in {attempt} attempts.")