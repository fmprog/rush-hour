import numpy as np


# class Board:
#     def __init__(self, length, exit):
#         '''Creates an empty board'''
#         self.length = length
#         self.width = length
#         self.exit = exit


class Car:
    def __init__(self, unique_id, length, col, row, color, position, orientation):
        '''Creates a vehicle'''
        self.unique_id = unique_id
        self.length = length
        self.col = col
        self.row = row
        # self.type = self.type()
        self.color = color
        self.position = position (1,1)
        self.orientation = orientation

    #def type():


class Game:
    def __init__(self, number_cars, start_positions, length, exit):
        '''Creates the game'''
        self.number_cars = number_cars
        self.start_positions = start_positions
        self.length = length
        self.exit = exit
        self.grid = self.grid()
        self.vehicles = self.create_vehicles()


    def grid(self):
        y = np.zeros((self.length, self.length))
        print(y)

    def create_vehicles(self):
        """
        creates vehicles using csv file
        """
        vehicles = {}

        with open("/home/emily/programmeertheorie/gameboards/Rushhour6x6_1.csv") as file:
            car_data = csv.DictReader(file)

            for line in car_data:
                id = line['car']
                orientation = line['orientation']
                column = int(line['col'])
                row = int(line['row'])
                length = int(line['length'])

                position = []
                position.append((row, column))

                for i in range(length - 1):
                    if orientation == 'H':
                        column =+ 1
                        position.append((row, column))
                    else:
                        row =+ 1
                        position.append((row, column))

                vehicles[id] = Car(id, orientation, column, row, length, position)

        return vehicles





if __name__ == "__main__":
    # Game 1 
    game1 = Game(1, (3, 1), 5, (3, 5))
