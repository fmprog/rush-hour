import random
import copy


class Randomise:
    """
    A Randomiser
    """
    def __init__(self, game):
        self.current_game = game
        self.solution = []


    def run(self):
    
        while self.current_game.is_solved() == False:
    
            # randomly select a vehicle to move
            possibilities_vehicles = list(self.current_game.vehicles.keys())
            select_vehicle = random.choice(possibilities_vehicles)

            # randomly select a direction to move to
            possibilities_direction = self.current_game.possible_direction(select_vehicle)
            
            if len(possibilities_direction) > 0:
                select_direction = random.choice(possibilities_direction)

                # move the selected vehicle to the selected direction
                copy_game = copy.deepcopy(self.current_game)

                # move the vehicle
                copy_game.move(select_vehicle, select_direction)
                
                # create a solution path
                self.solution.append([copy_game, [select_vehicle, select_direction]])

                # update the current game
                self.current_game = copy_game


    def return_solution(self):
        '''
        Returns the path and the corresponding boards.
        '''
        return self.solution