import numpy as np
import csv


class Car:
    def __init__(self, id, orientation, column, row, length, position):
        '''Creates a vehicle'''
        self.id = id
        self.orientation = orientation
        self.column = column
        self.row = row
        self.length = length
        self.position = position


class Game:
    def __init__(self, length, exit):
        '''Creates the game'''
        self.length = length
        self.exit = exit
        self.board = self.grid()
        self.vehicles = self.create_vehicles()
        self.move = self.movement('A', 'R')


    def grid(self):
        board = np.zeros((self.length, self.length), dtype='O')
        return board


    def create_vehicles(self):
        """
        creates vehicles using csv file
        """
        vehicles = {}

        with open("gameboards/Rushhour6x6_1.csv") as file:
            car_data = csv.DictReader(file)

            for line in car_data:
                id = line['car']
                orientation = line['orientation']
                column = int(line['col']) - 1
                row = int(line['row']) - 1
                length = int(line['length'])

                position = []
                position.append([row, column])

                for i in range(length - 1):
                    if orientation == 'H':
                        column += 1
                        position.append([row, column])
                    else:
                        row += 1
                        position.append([row, column])

                vehicles[id] = Car(id, orientation, column, row, length, position)

            for id in vehicles.keys():
                # access the positions for each car and add them to the board
                for i in vehicles[id].position:
                    self.board[i[0]][i[1]] = id
            print(self.board)

        return vehicles
    

    def movement(self, id, move):
        # check if movement is valid
        if self.vehicles[id].orientation == 'H':
            if move == 'R':
                print("R")
                # Check if movement is on the board
                if self.vehicles[id].position[-1][1] != (self.length - 1):
                    # Check if there is a car in the way
                    coordrow = self.vehicles[id].position[0][0]
                    coordcol = self.vehicles[id].position[-1][1] + 1
                    if self.board[coordrow][coordcol] == 0:
                        for i in range(self.vehicles[id].length):
                            self.vehicles[id].position[i][1] +=1
                    else:
                        print("car in the way")
                else: 
                    print("out of bound")
                
                

            elif move == 'L':
                print("L")

            else:
                print("Invalid input")
            
        else:
            if move == 'U' or move == 'D':
                print("valid")

            else:
                print("Invalid input")








if __name__ == "__main__":
    # Game 1 
    game1 = Game(6, 3)
