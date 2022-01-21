import random
import copy


def random_solver(game):

    X = game.vehicles['X']
    attempt = 1
    states = {}
    
    while X.position[0][1] != game.exit:
   
        possibilities_vehicles = list(game.vehicles.keys())
        select_vehicle = random.choice(possibilities_vehicles)

        possibilities_direction = []
        if game.vehicles[select_vehicle].orientation == 'H':

            # check if movement to the right is possible
            front_row_coord = game.vehicles[select_vehicle].position[-1][0]
            front_col_coord = game.vehicles[select_vehicle].position[-1][1]

            if front_col_coord + 1 != game.size and game.board[front_row_coord][front_col_coord + 1] == 0:
                possibilities_direction.append('R')

            # check if movement to the left is possible
            front_row_coord = game.vehicles[select_vehicle].position[0][0]
            front_col_coord = game.vehicles[select_vehicle].position[0][1]

            if front_col_coord - 1 >= 0 and game.board[front_row_coord][front_col_coord - 1] == 0:
                possibilities_direction.append('L')

        else:

            # check if movement up is possible
            front_row_coord = game.vehicles[select_vehicle].position[0][0]
            front_col_coord = game.vehicles[select_vehicle].position[0][1]

            # check if movement is possible
            if game.vehicles[select_vehicle].position[0][0] - 1 >= 0 and game.board[front_row_coord - 1][front_col_coord] == 0:
                possibilities_direction.append('U')
            
            # check if movement down is possible
            front_row_coord = game.vehicles[select_vehicle].position[-1][0]
            front_col_coord = game.vehicles[select_vehicle].position[-1][1]

            # check if movement is possible
            if game.vehicles[select_vehicle].position[-1][0] + 1 != game.size and game.board[front_row_coord + 1][front_col_coord] == 0:
                possibilities_direction.append('D')

        if len(possibilities_direction) > 0:
            select_direction = random.choice(possibilities_direction)
            
            # check if state has been visited before
            copy_board = copy.deepcopy(game.board)
            print(copy_board)
            copy_board.move(select_vehicle, select_direction)
            print(copy_board)

            # if 

            # move with selected vehicle to selected direction
            game.move(select_vehicle, select_direction)
            print(f"Move: Vehicle {select_vehicle} - Direction {select_direction}")
            game.show_board()
            print(f"This is the deep copy {copy_board}")
            print('-------------------')
            states[attempt] = game.board
            attempt += 1

    print(f"Solved the puzzle in {attempt} attempts.")
    print(states)