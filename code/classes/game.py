from .vehicle import Vehicle

import numpy as np
import csv


class Game:
    def __init__(self, game, size, exit):
        '''Creates the game'''
        self.size = size
        self.exit = exit
        self.board = self.grid()
        self.vehicles = self.load_vehicles(game)
        
        # test if movement works:
        """
        self.moving = self.move('A', 'L')
        self.moving = self.move('C', 'L')
        self.moving = self.move('G', 'U')
        self.moving = self.move('A', 'R')
        self.moving = self.move('G', 'D')
        self.moving = self.move('A', 'U')
        self.moving = self.move('A', 'R')
        """


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
    

    def move(self, uid, move):
        """
        Moves vehicle in the given direction if move is valid
        """

        # check if vehicle is on the board
        if uid in self.vehicles.keys():

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