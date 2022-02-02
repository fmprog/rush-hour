import random
import copy


class Randomise:
    """
    A Random Algorithm that solves the Rush Hour puzzle by moving random vehicles in random directions until car X is located in front of the exit.
    """
    def __init__(self, game):
        self.current_game = game
        self.solution = []


    def run(self):
        """
        Method to play moves with randomly selected vehicles and direction as long as the puzzle is not solved.
        """
        while self.current_game.is_solved() == False:
    
            # Randomly select a vehicle to move
            possibilities_vehicles = list(self.current_game.vehicles.keys())
            select_vehicle = random.choice(possibilities_vehicles)

            # Randomly select a direction to move to
            possibilities_direction = self.current_game.possible_direction(select_vehicle)
            
            if len(possibilities_direction) > 0:
                select_direction = random.choice(possibilities_direction)

                # Create acopy of the game and play the move
                copy_game = copy.deepcopy(self.current_game)
                copy_game.move(select_vehicle, select_direction)
                
                # Add the move and the resulting board to the solution
                self.solution.append([copy_game, [select_vehicle, select_direction]])

                # Update the current game
                self.current_game = copy_game


    def return_solution(self):
        """
        Returns all moves and corresponding boards that lead to the solution.
        """
        return self.solution
