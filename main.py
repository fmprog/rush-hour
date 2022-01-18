from code.classes.game import Game
import random


if __name__ == "__main__":
    # Load game 1
    game1 = Game("Rushhour6x6_1.csv", 6, 3)
    game1.show_board()

    X = game1.vehicles['X']
    attempt = 1
    
    while X.position[0][1] != 4:
   
        possibilities_vehicles = list(game1.vehicles.keys())
        select_vehicle = random.choice(possibilities_vehicles)

        possibilities_direction = []
        if game1.vehicles[select_vehicle].orientation == 'H':


            # check if movement to the right is possible
            front_row_coord = game1.vehicles[select_vehicle].position[-1][0]
            front_col_coord = game1.vehicles[select_vehicle].position[-1][1]
            if front_col_coord + 1 != game1.size and game1.board[front_row_coord][front_col_coord + 1] == 0:
                possibilities_direction.append('R')

            # check if movement to the left is possible
            front_row_coord = game1.vehicles[select_vehicle].position[0][0]
            front_col_coord = game1.vehicles[select_vehicle].position[0][1]

            if front_col_coord - 1 >= 0 and game1.board[front_row_coord][front_col_coord - 1] == 0:
                possibilities_direction.append('L')

        else:
            # check if movement up is possible
            front_row_coord = game1.vehicles[select_vehicle].position[0][0]
            front_col_coord = game1.vehicles[select_vehicle].position[0][1]

            # check if movement is possible
            if game1.vehicles[select_vehicle].position[0][0] - 1 >= 0 and game1.board[front_row_coord - 1][front_col_coord] == 0:
                possibilities_direction.append('U')
            
            # check if movement down is possible
            front_row_coord = game1.vehicles[select_vehicle].position[-1][0]
            front_col_coord = game1.vehicles[select_vehicle].position[-1][1]

            # check if movement is possible
            if game1.vehicles[select_vehicle].position[-1][0] + 1 != game1.size and game1.board[front_row_coord + 1][front_col_coord] == 0:
                possibilities_direction.append('D')

        if len(possibilities_direction) > 0:
            select_direction = random.choice(possibilities_direction)

        # move with selected vehicle to selected direction
            game1.move(select_vehicle, select_direction)
            print(f"Move: Vehicle {select_vehicle} - Direction {select_direction}")
            game1.show_board()
            print('-------------------')
            attempt += 1

    print(f"Solved the puzzle in {attempt} attempts.")

