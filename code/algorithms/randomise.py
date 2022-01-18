import random
import copy


def random_solver(...):
        while True:

        if X.position[0][1] == 4:
            print("Hoera!")
            exit
    
        possibilities_vehicles = list(game1.vehicles.keys())
        select_vehicle = random.choice(possibilities_vehicles)

        if game1.vehicles[select_vehicle].orientation == 'H':
            possibilities_direction = ['L', 'R']
        else:
            possibilities_direction = ['U', 'D']
        select_direction = random.choice(possibilities_direction)

    #   select_vehicle = input("Select a vehicle to move: ")
    #   select_direction = input("Select a direction to move the vehicle towards (R, L, U, D): ")
        print(f"Move: {select_vehicle}|{select_direction}")
        game1.move(select_vehicle, select_direction)
        game1.show_board()