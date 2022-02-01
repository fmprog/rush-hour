import random


class Randomise:
    """
    A Randomiser
    """
    def __init__(self, game):
        self.current_board = game
        self.solution = []

    def run(self):

        attempt = 1
    
        while self.current_board.is_solved() == False:
    
            # randomly select a vehicle to move
            possibilities_vehicles = list(self.current_board.vehicles.keys())
            select_vehicle = random.choice(possibilities_vehicles)

            # randomly select a direction to move to
            possibilities_direction = self.current_board.possible_direction(select_vehicle)
            
            if len(possibilities_direction) > 0:
                select_direction = random.choice(possibilities_direction)

                # move the selected vehicle to the selected direction
                self.current_board.move(select_vehicle, select_direction)
                
                # create a solution path
                self.solution.append([self.current_board, [select_vehicle, select_direction]])

                # print out information about the move and gameboard
                # self.current_board.show_board(select_vehicle, select_direction)

                # keep track of the attempts
                attempt += 1

        print(f"Solved the puzzle in {attempt} attempts.")

    def return_solution(self):
        '''
        Returns the path and the corresponding boards.
        '''
        return self.solution