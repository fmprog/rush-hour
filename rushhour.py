

# class Board:
#     def __init__(self, length, exit):
#         '''Creates an empty board'''
#         self.length = length
#         self.width = length
#         self.exit = exit


class Car:
    def __init__(self, unique_id, length, type, color, position, orientation):
        '''Creates a vehicle'''
        self.unique_id = unique_id
        self.length = length
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

    def grid(self):
        board = {}
        for row in range(self.length):
            for col in range(self.length):
                board[(row,col)] = "empty"

        if self.number_cars > 0:
            for car in range(self.number_cars):
                board[self.start_positions] = "car"

        # to print the board
        for i in range(self.length):
            for j in range(self.length):
                print(board[(i, j)], end ='   ')
         
            print()



if __name__ == "__main__":
    game1 = Game(1, (3, 1), 5, (3, 5))
