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
        self.move = self.movement('A', 'L')
        self.move = self.movement('C', 'L')
        self.move = self.movement('G', 'U')
        self.move = self.movement('A', 'R')
        self.move = self.movement('G', 'D')
        self.move = self.movement('A', 'U')
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

        # check orientation of vehicle
        if self.vehicles[id].orientation == 'H':

            # check direction of movement
            if move == 'R':
                
                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[id].position[-1][0] 
                front_col_coord = self.vehicles[id].position[-1][1] 

                # check if movement is possible
                if front_col_coord + 1 != self.length and self.board[front_row_coord][front_col_coord + 1] == 0:
        
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[id].position[0][0] 
                    back_col_coord = self.vehicles[id].position[0][1] 
                    
                    # set previous coordinates of vehicle to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[id].length):
                        self.vehicles[id].position[i][1] += 1
                    
                    # adjust postion of vehicle on the board
                    for i in self.vehicles[id].position:
                        self.board[i[0]][i[1]] = id
                    
                else: 
                    print("Out of bound")
                
                print(self.board)

            elif move == 'L':

                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[id].position[0][0] 
                front_col_coord = self.vehicles[id].position[0][1] 

                # check if movement is possible
                if front_col_coord - 1 >= 0 and self.board[front_row_coord][front_col_coord - 1] == 0:
                    
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[id].position[-1][0] 
                    back_col_coord = self.vehicles[id].position[-1][1] 
                    
                    # set previous coordinates to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[id].length):
                        self.vehicles[id].position[i][1] -= 1

                    # adjust postion of vehicle on the board
                    for i in self.vehicles[id].position:
                        self.board[i[0]][i[1]] = id
                    
                else: 
                    print("Out of bound")
                
                print(self.board)
                
            else:
                print("Invalid input")

        elif self.vehicles[id].orientation == 'V':

            if move == 'U':

                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[id].position[0][0] 
                front_col_coord = self.vehicles[id].position[0][1] 

                # check if movement is possible
                if self.vehicles[id].position[0][0] - 1 >= 0 and self.board[front_row_coord - 1][front_col_coord] == 0:
                
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[id].position[-1][0] 
                    back_col_coord = self.vehicles[id].position[-1][1] 
                    
                    # set previous coordinates to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[id].length):
                        self.vehicles[id].position[i][0] -= 1
                    
                    # adjust postion of vehicle on the board
                    for i in self.vehicles[id].position:
                        self.board[i[0]][i[1]] = id

                else: 
                    print("Out of bound")
                
                print(self.board)
     
            elif move == 'D':
                
                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[id].position[-1][0] 
                front_col_coord = self.vehicles[id].position[-1][1] 

                # check if movement is possible
                if self.vehicles[id].position[-1][0] + 1 != self.length and self.board[front_row_coord + 1][front_col_coord] == 0:
                    
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[id].position[0][0] 
                    back_col_coord = self.vehicles[id].position[0][1] 
                    
                    # set previous coordinates to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[id].length):
                        self.vehicles[id].position[i][0] += 1
                    
                    # adjust postion of vehicle on the board
                    for i in self.vehicles[id].position:
                        self.board[i[0]][i[1]] = id
                    
                else: 
                    print("Out of bound")
                
                print(self.board)

            else:
                print("Invalid input") 
        
        else:
            print("Invalid input") 

if __name__ == "__main__":
    # Game 1 
    game1 = Game(6, 3)
