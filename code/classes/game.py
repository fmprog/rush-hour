from .vehicle import Vehicle

import numpy as np
import csv


class Game:
    def __init__(self, game, size):
        '''Creates the game'''
        self.size = size
        self.board = self.grid()
        self.vehicles = self.load_vehicles(game)
        self.moves = {}
        

    def grid(self):
        """
        Returns an empty matrix size*size
        """
        board = np.zeros((self.size, self.size), dtype='O')
        return board


    def show_board(self):
        """
        Returns current state of board
        """
        for row in self.board:
            for item in row:
                print(" ", end="")
                print(item, end ="")
                print(" ", end="")
            print()


    def copy(self):
        """
        Returns a copy of self.
        """
        new = self

        # Update the board after copy
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                new.board[row][col] = self.board[row][col]

        return new


    def load_vehicles(self, game):
        """
        Loads vehicles from csv file into matrix
        """
        vehicles = {}

        with open(f"data/gameboards/{game}") as file:
            vehicle_data = csv.DictReader(file)

            for line in vehicle_data:
                uid = line['car']
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

                vehicles[uid] = Vehicle(uid, orientation, column, row, length, position)

            for uid in vehicles.keys():
                # access the positions for each car and add them to the board
                for i in vehicles[uid].position:
                    self.board[i[0]][i[1]] = uid

        return vehicles
    

    def possible_direction(self, select_vehicle):
        """
        text
        """
        possibilities_direction = []

        if self.vehicles[select_vehicle].orientation == 'H':

                # check if movement to the right is possible
                front_row_coord = self.vehicles[select_vehicle].position[-1][0]
                front_col_coord = self.vehicles[select_vehicle].position[-1][1]

                if front_col_coord + 1 != self.size and self.board[front_row_coord][front_col_coord + 1] == 0:
                    possibilities_direction.append('R')

                # check if movement to the left is possible
                front_row_coord = self.vehicles[select_vehicle].position[0][0]
                front_col_coord = self.vehicles[select_vehicle].position[0][1]

                if front_col_coord - 1 >= 0 and self.board[front_row_coord][front_col_coord - 1] == 0:
                    possibilities_direction.append('L')

        else:

                # check if movement up is possible
                front_row_coord = self.vehicles[select_vehicle].position[0][0]
                front_col_coord = self.vehicles[select_vehicle].position[0][1]

                # check if movement is possible
                if self.vehicles[select_vehicle].position[0][0] - 1 >= 0 and self.board[front_row_coord - 1][front_col_coord] == 0:
                    possibilities_direction.append('U')
                
                # check if movement down is possible
                front_row_coord = self.vehicles[select_vehicle].position[-1][0]
                front_col_coord = self.vehicles[select_vehicle].position[-1][1]

                # check if movement is possible
                if self.vehicles[select_vehicle].position[-1][0] + 1 != self.size and self.board[front_row_coord + 1][front_col_coord] == 0:
                    possibilities_direction.append('D')

        return possibilities_direction
 

    def move(self, uid, move):
        """
        Moves vehicle in the given direction if move is valid
        """

        # check orientation of vehicle
        if self.vehicles[uid].orientation == 'H':

            # check direction of movement
            if move == 'R':
                
                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[uid].position[-1][0] 
                front_col_coord = self.vehicles[uid].position[-1][1] 

                # check if movement is possible
                if front_col_coord + 1 != self.size and self.board[front_row_coord][front_col_coord + 1] == 0:
        
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[uid].position[0][0] 
                    back_col_coord = self.vehicles[uid].position[0][1] 
                    
                    # set previous coordinates of vehicle to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[uid].length):
                        self.vehicles[uid].position[i][1] += 1
                    
                    # adjust postion of vehicle on the board
                    for i in self.vehicles[uid].position:
                        self.board[i[0]][i[1]] = uid
                    
                else: 
                    print("Out of bound")
                

            elif move == 'L':

                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[uid].position[0][0] 
                front_col_coord = self.vehicles[uid].position[0][1] 

                # check if movement is possible
                if front_col_coord - 1 >= 0 and self.board[front_row_coord][front_col_coord - 1] == 0:
                    
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[uid].position[-1][0] 
                    back_col_coord = self.vehicles[uid].position[-1][1] 
                    
                    # set previous coordinates to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[uid].length):
                        self.vehicles[uid].position[i][1] -= 1

                    # adjust postion of vehicle on the board
                    for i in self.vehicles[uid].position:
                        self.board[i[0]][i[1]] = uid
                    
                else: 
                    print("Out of bound")

                
            else:
                print("Invalid input")

        elif self.vehicles[uid].orientation == 'V':

            if move == 'U':

                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[uid].position[0][0] 
                front_col_coord = self.vehicles[uid].position[0][1] 

                # check if movement is possible
                if self.vehicles[uid].position[0][0] - 1 >= 0 and self.board[front_row_coord - 1][front_col_coord] == 0:
                
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[uid].position[-1][0] 
                    back_col_coord = self.vehicles[uid].position[-1][1] 
                    
                    # set previous coordinates to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[uid].length):
                        self.vehicles[uid].position[i][0] -= 1
                    
                    # adjust postion of vehicle on the board
                    for i in self.vehicles[uid].position:
                        self.board[i[0]][i[1]] = uid

                else: 
                    print("Out of bound")
    
            elif move == 'D':
                
                # define coordinates of front of vehicle
                front_row_coord = self.vehicles[uid].position[-1][0] 
                front_col_coord = self.vehicles[uid].position[-1][1] 

                # check if movement is possible
                if self.vehicles[uid].position[-1][0] + 1 != self.size and self.board[front_row_coord + 1][front_col_coord] == 0:
                    
                    # define coordinates of back of vehicle
                    back_row_coord = self.vehicles[uid].position[0][0] 
                    back_col_coord = self.vehicles[uid].position[0][1] 
                    
                    # set previous coordinates to zero
                    self.board[back_row_coord][back_col_coord] = 0

                    # set new coordinates of vehicle after movement
                    for i in range(self.vehicles[uid].length):
                        self.vehicles[uid].position[i][0] += 1
                    
                    # adjust postion of vehicle on the board
                    for i in self.vehicles[uid].position:
                        self.board[i[0]][i[1]] = uid
                    
                else: 
                    print("Out of bound")

            else:
                print("Invalid input") 
        
        else:
            print("Invalid input") 

    else:
        print("Vehicle does not exist")


    def move_back(self, uid, move):
        """
        Moves vehicle back one step
        """
        if move == 'L' or move == 'R':
            if move == 'L':
                move = 'R'
            else:
                move = 'L'
        else:
            if move == 'D':
                move = 'U'
            else:
                move = 'D'

        self.move(uid, move)

    def is_solved(self):
        """
        Checks if red car is located in front of the exit and puzzle is solved
        """
        if self.size == 6:
            exit_column = 4
        elif self.size == 9:
            exit_column = 7
        elif self.size == 12:
            exit_column = 10
        
        if self.vehicles['X'].position[0][1] == exit_column:
            return True

        else:
            return False


