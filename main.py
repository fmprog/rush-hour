from code.classes.game import Game


if __name__ == "__main__":
    # Load game 1
    game1 = Game("Rushhour6x6_1.csv", 6, 3)
    game1.show_board()

    while True:
        select_vehicle = input("Select a vehicle to move: ")
        select_direction = input("Select a direction to move the vehicle towards (R, L, U, D): ")
        game1.move(select_vehicle, select_direction)
        game1.show_board()